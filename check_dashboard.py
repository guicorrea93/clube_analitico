"""Valida rapidamente o dashboard HTML gerado."""
from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).parent
DASHBOARD = ROOT / "dashboard.html"

MIN_COUNTS = {
    "matches": 9000,
    "goals": 10000,
    "cards": 20000,
    "stats": 18000,
    "class_rodada": 18000,
    "class_final_hist": 1800,
}


def main() -> None:
    if not DASHBOARD.exists():
        raise SystemExit(f"Dashboard nao encontrado: {DASHBOARD}")

    html = DASHBOARD.read_text(encoding="utf-8")
    match = re.search(r"const DATA = (\{.*?\});\n", html, flags=re.S)
    if not match:
        raise SystemExit("Payload DATA nao encontrado no dashboard.")

    data = json.loads(match.group(1))
    falhas = 0

    print(f"Dashboard: {DASHBOARD}")
    print(f"Tamanho: {DASHBOARD.stat().st_size / 1024 / 1024:.2f} MB")
    print()

    for key, minimum in MIN_COUNTS.items():
        value = len(data.get(key, []))
        ok = value >= minimum
        marker = "OK" if ok else "FALHA"
        print(f"{marker:<5} {key}: {value} (minimo {minimum})")
        if not ok:
            falhas += 1

    copa = data.get("copa_brasil", {})
    copa_checks = {
        "copa_brasil.finais": (len(copa.get("finais", [])), 37),
        "copa_brasil.edicoes": (len(copa.get("edicoes", [])), 37),
        "copa_brasil.participantes": (len(copa.get("participantes", [])), 1000),
    }
    for label, (value, minimum) in copa_checks.items():
        ok = value >= minimum
        marker = "OK" if ok else "FALHA"
        print(f"{marker:<5} {label}: {value} (minimo {minimum})")
        if not ok:
            falhas += 1

    if falhas:
        raise SystemExit(f"{falhas} falha(s) encontrada(s) no dashboard.")

    print("\nDashboard OK.")


if __name__ == "__main__":
    main()
