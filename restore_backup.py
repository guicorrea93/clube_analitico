"""Restaura backups criados por backup.py.

Por seguranca, a restauracao exige --confirm. Sem argumentos, lista os backups
locais disponiveis em backups/.
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


ROOT = Path(__file__).parent
BACKUPS = ROOT / "backups"


def list_backups() -> list[Path]:
    if not BACKUPS.exists():
        return []
    return sorted([p for p in BACKUPS.iterdir() if p.is_dir()], reverse=True)


def restore(src: Path) -> None:
    for child in src.iterdir():
        dst = ROOT / child.name
        if child.is_dir():
            shutil.copytree(child, dst, dirs_exist_ok=True)
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(child, dst)


def main() -> None:
    backups = list_backups()

    parser = argparse.ArgumentParser(description="Restaura backup local do projeto.")
    parser.add_argument(
        "backup",
        nargs="?",
        help="Nome da pasta em backups/ ou caminho completo do backup.",
    )
    parser.add_argument(
        "--confirm",
        action="store_true",
        help="Confirma a restauracao e sobrescrita dos arquivos existentes.",
    )
    args = parser.parse_args()

    if not args.backup:
        print("Backups disponiveis:")
        if not backups:
            print("  nenhum backup encontrado")
            return
        for path in backups:
            total_files = sum(1 for p in path.rglob("*") if p.is_file())
            total_bytes = sum(p.stat().st_size for p in path.rglob("*") if p.is_file())
            print(f"  {path.name} ({total_files} arquivos, {total_bytes / 1024 / 1024:.2f} MB)")
        print("\nPara restaurar:")
        print("  python .\\restore_backup.py <nome_do_backup> --confirm")
        return

    src = Path(args.backup)
    if not src.is_absolute():
        src = BACKUPS / src
    if not src.exists() or not src.is_dir():
        raise SystemExit(f"Backup nao encontrado: {src}")
    if not args.confirm:
        raise SystemExit(
            "Restauracao cancelada. Rode novamente com --confirm para sobrescrever arquivos."
        )

    restore(src)
    print(f"Backup restaurado de: {src}")


if __name__ == "__main__":
    main()
