"""Executa o pipeline local do Clube Analitico.

Por padrao, usa o banco SQLite existente como fonte de dados, valida o conteudo
e gera o dashboard. A recriacao do banco a partir dos arquivos-fonte e opcional
e precisa ser pedida explicitamente com --rebuild-from-sources.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parent
CLASSIFICACAO_XLSX = ROOT / "classificacao_codex.xlsx"


def run_step(label: str, args: list[str]) -> None:
    print(f"\n==> {label}")
    cmd = [sys.executable, *args]
    print("    " + " ".join(args))
    completed = subprocess.run(cmd, cwd=ROOT, check=False)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Valida o banco existente e gera o dashboard HTML."
    )
    parser.add_argument(
        "--rebuild-from-sources",
        action="store_true",
        help="Recria db/brasileirao.db a partir dos CSVs/wikitextos locais.",
    )
    parser.add_argument(
        "--from-year",
        type=int,
        help="Ano inicial para recriar o Brasileirao. Exige --rebuild-from-sources.",
    )
    parser.add_argument(
        "--to-year",
        type=int,
        help="Ano final para recriar o Brasileirao. Exige --rebuild-from-sources.",
    )
    parser.add_argument(
        "--skip-historico",
        action="store_true",
        help="Nao importa classificacao historica nacional ao recriar o banco.",
    )
    parser.add_argument(
        "--skip-copa",
        action="store_true",
        help="Nao importa dados da Copa do Brasil ao recriar o banco.",
    )
    parser.add_argument(
        "--skip-validacao",
        action="store_true",
        help="Nao executa validar_banco.py.",
    )
    parser.add_argument(
        "--skip-enriquecimento",
        action="store_true",
        help="Nao executa enriquecer_historico.py (grupos/criterios/pontos do Brasileiro antigo).",
    )
    parser.add_argument(
        "--skip-dashboard",
        action="store_true",
        help="Nao gera dashboard.html.",
    )
    parser.add_argument(
        "--skip-dashboard-check",
        action="store_true",
        help="Nao valida o payload do dashboard apos a geracao.",
    )
    args = parser.parse_args()

    if not args.rebuild_from_sources:
        if args.from_year is not None or args.to_year is not None:
            raise SystemExit("Use --from-year/--to-year apenas com --rebuild-from-sources.")
        if args.skip_historico or args.skip_copa:
            raise SystemExit("Use --skip-historico/--skip-copa apenas com --rebuild-from-sources.")
        if not args.skip_validacao:
            run_step("Validando banco existente", ["validar_banco.py"])
        if not args.skip_enriquecimento:
            run_step("Enriquecendo Brasileiro antigo (grupos/criterios/pontos)", ["enriquecer_historico.py"])
        if not args.skip_dashboard:
            run_step("Gerando dashboard HTML", ["gerar_dashboard_html.py"])
            if not args.skip_dashboard_check:
                run_step("Validando dashboard HTML", ["check_dashboard.py"])
        print("\nPipeline concluido.")
        return

    if not args.skip_historico and not CLASSIFICACAO_XLSX.exists():
        raise SystemExit(
            "classificacao_codex.xlsx nao encontrado. "
            "A recriacao por fontes substitui o banco e perderia a classificacao "
            "historica nacional. Adicione a planilha na raiz do projeto ou rode "
            "com --rebuild-from-sources --skip-historico para aceitar "
            "explicitamente esse build parcial."
        )

    criar_args = ["criar_banco_brasileirao.py", "--reset"]
    if args.from_year is not None or args.to_year is not None:
        if args.from_year is None or args.to_year is None:
            raise SystemExit("Use --from-year e --to-year juntos.")
        criar_args.extend(["--from", str(args.from_year), "--to", str(args.to_year)])
    else:
        criar_args.append("--all")

    run_step("Criando banco do Brasileirao", criar_args)

    if args.skip_historico:
        print("\n==> Classificacao historica nacional ignorada por opcao")
    else:
        run_step(
            "Importando classificacao historica nacional",
            ["importar_classificacao_historica_brasileirao.py"],
        )

    if args.skip_copa:
        print("\n==> Copa do Brasil ignorada por opcao")
    else:
        run_step(
            "Importando finais da Copa do Brasil",
            ["importar_finais_copa_brasil.py"],
        )
        run_step(
            "Importando edicoes da Copa do Brasil",
            ["importar_edicoes_copa_brasil.py"],
        )

    if not args.skip_validacao:
        run_step("Validando banco", ["validar_banco.py"])

    if not args.skip_enriquecimento:
        run_step("Enriquecendo Brasileiro antigo (grupos/criterios/pontos)", ["enriquecer_historico.py"])

    if not args.skip_dashboard:
        run_step("Gerando dashboard HTML", ["gerar_dashboard_html.py"])
        if not args.skip_dashboard_check:
            run_step("Validando dashboard HTML", ["check_dashboard.py"])

    print("\nPipeline concluido.")


if __name__ == "__main__":
    main()
