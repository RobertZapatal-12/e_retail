"""Minimal desktop data-entry application. Run with python -m app.gui."""

import queue
from pathlib import Path
import sys
import threading
import tkinter as tk
from tkinter import messagebox, ttk

import psycopg2

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.forms import GROUPS, LABELS, OPTIONAL, OPTIONAL_TEXT, fields, validate
from connection.database import get_connection

BG = "#f4f4f0"
INK = "#202a25"
MUTED = "#677269"
LINE = "#d6dcd6"
ACCENT = "#245b43"


class DataEntryApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("e_retail · Ingreso de datos")
        self.geometry("1100x790")
        self.minsize(820, 600)
        self.configure(bg=BG)
        self.option_add("*Font", "{Segoe UI} 10")
        self.busy = False
        self.inputs = {}
        self.results = queue.Queue()
        self.saved = 0
        self.group = "Catálogo"
        self.entity = tk.StringVar(value="Productos")
        self.protocol("WM_DELETE_WINDOW", self.close)
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TCombobox", padding=8, fieldbackground="white")

        sidebar = tk.Frame(self, bg=INK, width=210)
        sidebar.pack(side="left", fill="y")
        sidebar.pack_propagate(False)
        tk.Label(sidebar, text="e_retail", bg=INK, fg="white",
                 font=("Segoe UI", 25, "bold")).pack(anchor="w", padx=26, pady=(35, 0))
        tk.Label(sidebar, text="GESTIÓN DE DATOS", bg=INK, fg="#a4b7aa",
                 font=("Segoe UI", 9)).pack(anchor="w", padx=28, pady=(4, 44))
        self.nav = {}
        for index, group in enumerate(GROUPS, 1):
            button = tk.Button(sidebar, text=f"0{index}   {group}", anchor="w",
                               command=lambda g=group: self.select_group(g),
                               relief="flat", bd=0, padx=28, pady=15,
                               activebackground=ACCENT, activeforeground="white")
            button.pack(fill="x", pady=2)
            self.nav[group] = button
        tk.Label(sidebar, text="ADMINISTRACIÓN\nIngreso manual de registros", justify="left",
                 bg=INK, fg="#a4b7aa", font=("Segoe UI", 9)).pack(
                     side="bottom", anchor="w", padx=26, pady=28)

        main = tk.Frame(self, bg=BG)
        main.pack(side="left", fill="both", expand=True, padx=34, pady=30)
        tk.Label(main, text="ESPACIO DE TRABAJO  /  NUEVO REGISTRO", bg=BG, fg=MUTED,
                 font=("Segoe UI", 9)).pack(anchor="w")
        self.heading = tk.Label(main, bg=BG, fg=INK, font=("Segoe UI", 28, "bold"))
        self.heading.pack(anchor="w", pady=(16, 4))
        tk.Label(main, text="Completa los datos y guarda el registro en tu base de datos.",
                 bg=BG, fg=MUTED).pack(anchor="w", pady=(0, 22))
        selector = tk.Frame(main, bg=BG)
        selector.pack(fill="x", pady=(0, 20))
        tk.Label(selector, text="TIPO DE REGISTRO", bg=BG, fg=MUTED,
                 font=("Segoe UI", 9)).pack(side="left", padx=(0, 18))
        self.select = ttk.Combobox(selector, textvariable=self.entity, state="readonly", width=29)
        self.select.pack(side="left")
        self.select.bind("<<ComboboxSelected>>", lambda event: self.render_form())

        panel = tk.Frame(main, bg="white", highlightbackground=LINE, highlightthickness=1)
        panel.pack(fill="both", expand=True)
        self.canvas = tk.Canvas(panel, bg="white", highlightthickness=0)
        scroll = ttk.Scrollbar(panel, orient="vertical", command=self.canvas.yview)
        scroll.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.configure(yscrollcommand=scroll.set)
        self.form = tk.Frame(self.canvas, bg="white", padx=24, pady=22)
        self.window = self.canvas.create_window((0, 0), window=self.form, anchor="nw")
        self.canvas.bind("<Configure>", lambda e: self.canvas.itemconfigure(self.window, width=e.width))
        self.form.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.bind_all("<MouseWheel>", self.scroll)

        self.status = tk.Label(main, bg=BG, fg=MUTED, anchor="w", justify="left", wraplength=620)
        self.status.pack(fill="x", pady=(14, 10))
        actions = tk.Frame(main, bg=BG)
        actions.pack(fill="x")
        self.counter = tk.Label(actions, text="0 registros guardados en esta sesión", bg=BG, fg=MUTED)
        self.counter.pack(side="left")
        self.save_button = tk.Button(actions, text="Guardar registro  →", command=self.save,
                                     bg=ACCENT, fg="white", activebackground=INK,
                                     activeforeground="white", relief="flat", padx=20, pady=12)
        self.save_button.pack(side="right")
        self.clear_button = tk.Button(actions, text="Limpiar", command=self.clear,
                                      bg=BG, fg=INK, relief="flat", padx=16, pady=12)
        self.clear_button.pack(side="right", padx=8)
        self.bind("<Control-Return>", lambda e: self.save())
        self.select_group(self.group)
        self.after(100, self.poll)

    def scroll(self, event):
        if self.canvas.winfo_containing(event.x_root, event.y_root) in (self.select,):
            return
        self.canvas.yview_scroll(int(-event.delta / 120), "units")

    def select_group(self, group):
        if self.busy:
            return
        self.group = group
        names = list(GROUPS[group][1])
        self.select.configure(values=names)
        self.entity.set(names[0])
        for name, button in self.nav.items():
            button.configure(bg=ACCENT if name == group else INK,
                             fg="white" if name == group else "#b9c7bd")
        self.render_form()

    def render_form(self):
        for widget in self.form.winfo_children():
            widget.destroy()
        self.inputs.clear()
        self.heading.configure(text=self.entity.get())
        self.repository, methods = GROUPS[self.group]
        self.method = methods[self.entity.get()]
        self.parameters = fields(self.repository, self.method)
        tk.Label(self.form, text="01  /  Información del registro", bg="white", fg=INK,
                 font=("Segoe UI", 13, "bold")).grid(row=0, column=0, columnspan=2, sticky="w")
        tk.Label(self.form, text="* Obligatorio · Los ID relacionados deben existir.",
                 bg="white", fg=MUTED).grid(row=1, column=0, columnspan=2, sticky="w", pady=(6, 20))
        for index, field in enumerate(self.parameters):
            row, column = divmod(index, 2)
            cell = tk.Frame(self.form, bg="white")
            cell.grid(row=row + 2, column=column, sticky="nsew", padx=(0, 20), pady=(0, 18))
            optional = field.name in OPTIONAL | OPTIONAL_TEXT
            title = LABELS.get(field.name, field.name) + ("" if optional else " *")
            tk.Label(cell, text=title, bg="white", fg=INK).pack(anchor="w", pady=(0, 7))
            entry = tk.Entry(cell, relief="flat", bg="#f7f8f5", fg=INK,
                             highlightthickness=1, highlightbackground=LINE,
                             highlightcolor=ACCENT, insertbackground=ACCENT)
            entry.pack(fill="x", ipady=9)
            self.inputs[field.name] = entry
            if field.name.endswith("_at"):
                tk.Label(cell, text="AAAA-MM-DD HH:MM", bg="white", fg=MUTED,
                         font=("Segoe UI", 8)).pack(anchor="w", pady=(4, 0))
        self.form.columnconfigure((0, 1), weight=1, uniform="field")
        self.canvas.yview_moveto(0)
        self.status.configure(text="Listo para ingresar datos.  Ctrl + Enter para guardar.", fg=MUTED)
        next(iter(self.inputs.values())).focus_set()

    def clear(self):
        if not self.busy:
            for entry in self.inputs.values():
                entry.delete(0, "end")
            next(iter(self.inputs.values())).focus_set()
            self.status.configure(text="Formulario limpio. Puedes ingresar un nuevo registro.", fg=MUTED)

    def save(self):
        if self.busy:
            return
        try:
            values = validate(self.parameters, {name: entry.get() for name, entry in self.inputs.items()})
        except ValueError as exc:
            self.status.configure(text=str(exc), fg="#a03128")
            return
        self.set_busy(True)
        self.status.configure(text="Guardando registro…", fg=MUTED)
        threading.Thread(target=self.insert, args=(self.repository, self.method, values), daemon=True).start()

    def set_busy(self, busy):
        self.busy = busy
        state = "disabled" if busy else "normal"
        for widget in [*self.inputs.values(), *self.nav.values(), self.save_button, self.clear_button]:
            widget.configure(state=state)
        self.select.configure(state="disabled" if busy else "readonly")
        self.save_button.configure(text="Guardando…" if busy else "Guardar registro  →")

    def insert(self, repository, method, values):
        conn = None
        try:
            conn = get_connection()
            with conn.cursor() as cursor:
                cursor.execute("SET statement_timeout = '15s'")
            getattr(repository(conn), method)(**values)
            self.results.put((True, "Registro guardado correctamente."))
        except Exception as exc:
            if conn is not None:
                conn.rollback()
            if isinstance(exc, psycopg2.IntegrityError):
                message = {
                    "23505": "Ya existe un registro con ese ID o valor único.",
                    "23503": "Un ID relacionado no existe. Crea primero el registro de referencia.",
                    "23502": "La base de datos requiere un campo que está vacío.",
                    "23514": "Los valores no cumplen las restricciones de la base de datos.",
                }.get(exc.pgcode, "Revisa los datos y las restricciones de la tabla.")
            elif isinstance(exc, psycopg2.OperationalError):
                message = "No se pudo conectar con PostgreSQL. Revisa el servicio y la configuración de conexión."
            elif isinstance(exc, psycopg2.Error):
                message = "No se pudo guardar: " + (exc.diag.message_primary or "error de base de datos.")
            else:
                message = "No se pudo guardar el registro. " + str(exc)
            self.results.put((False, message))
        finally:
            if conn is not None:
                conn.close()

    def poll(self):
        try:
            success, message = self.results.get_nowait()
        except queue.Empty:
            pass
        else:
            self.set_busy(False)
            if success:
                self.saved += 1
                self.clear()
                self.counter.configure(text=f"{self.saved} registros guardados en esta sesión")
            self.status.configure(text=message, fg=ACCENT if success else "#a03128")
        self.after(100, self.poll)

    def close(self):
        if self.busy:
            messagebox.showinfo("Guardado en curso", "Espera a que termine el guardado antes de cerrar.")
        else:
            self.destroy()


def main():
    DataEntryApp().mainloop()


if __name__ == "__main__":
    main()
