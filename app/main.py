"""Entry point supporting both module and direct script execution."""

import argparse
from pathlib import Path
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def main():
    parser = argparse.ArgumentParser(description="e_retail: interfaz de ingreso de datos")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--seed", action="store_true", help="Ejecutar la generación masiva de datos")
    mode.add_argument("--check", action="store_true", help="Verificar dependencias e importaciones sin insertar datos")
    args = parser.parse_args()
    try:
        if args.check:
            from app import gui, runall
            import repo

            assert gui.main and runall.run_all and repo.ProductRepository
            print("OK: dependencias y módulos disponibles.")
        elif args.seed:
            from app.runall import run_all

            run_all()
        else:
            from app.gui import main as launch_gui

            launch_gui()
    except ModuleNotFoundError as exc:
        print(f"Falta el módulo: {exc.name}.\n"
              f'Instala las dependencias con: "{sys.executable}" -m pip install '
              f'-r "{Path(__file__).resolve().parents[1] / "requirements.txt"}"', file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
