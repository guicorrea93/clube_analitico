"""Cria backups locais do projeto.

Por padrao, copia os artefatos criticos para restauracao rapida:
db/, dashboard.html e scripts/documentos principais. Use --full para copiar
quase todo o projeto, ignorando caches, .git e backups anteriores.
"""
from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).parent
BACKUPS = ROOT / "backups"

CRITICAL_FILES = [
    ".gitignore",
    "README.md",
    "requirements.txt",
    "build.py",
    "backup.py",
    "status_db.py",
    "criar_banco_brasileirao.py",
    "gerar_dashboard_html.py",
    "validar_banco.py",
    "importar_classificacao_historica_brasileirao.py",
    "importar_finais_copa_brasil.py",
    "importar_edicoes_copa_brasil.py",
    "dashboard.html",
]

CRITICAL_DIRS = [
    "db",
    "sql",
]

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "env",
    "backups",
}


def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def copy_file(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)


def copy_dir(src: Path, dst: Path) -> None:
    if not src.exists():
        return
    shutil.copytree(src, dst, dirs_exist_ok=True)


def ignore_full(dir_path: str, names: list[str]) -> set[str]:
    return {name for name in names if name in IGNORE_DIRS}


def backup_critical(dst: Path) -> None:
    for name in CRITICAL_FILES:
        copy_file(ROOT / name, dst / name)
    for name in CRITICAL_DIRS:
        copy_dir(ROOT / name, dst / name)


def backup_full(dst: Path) -> None:
    shutil.copytree(ROOT, dst, ignore=ignore_full, dirs_exist_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Cria backup local do projeto.")
    parser.add_argument(
        "--full",
        action="store_true",
        help="Copia quase todo o projeto, exceto .git, caches e backups anteriores.",
    )
    args = parser.parse_args()

    BACKUPS.mkdir(exist_ok=True)
    mode = "full" if args.full else "critical"
    dst = BACKUPS / f"clube_analitico_{mode}_{timestamp()}"

    if args.full:
        backup_full(dst)
    else:
        dst.mkdir(parents=True, exist_ok=True)
        backup_critical(dst)

    total_files = sum(1 for p in dst.rglob("*") if p.is_file())
    total_bytes = sum(p.stat().st_size for p in dst.rglob("*") if p.is_file())

    print(f"Backup criado em: {dst}")
    print(f"Arquivos: {total_files}")
    print(f"Tamanho: {total_bytes / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    main()
