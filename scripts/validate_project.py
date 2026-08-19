"""Dependency-free repository smoke test."""
from pathlib import Path
import ast, sys

ROOT=Path(__file__).resolve().parents[1]
required=["README.md","producer.py","consumer.py","dashboard.py","query.py","requirements.txt"]
errors=[f"missing: {p}" for p in required if not (ROOT/p).is_file()]
for path in ROOT.glob("*.py"):
    try: ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc: errors.append(f"{path.name}: {exc}")
readme=(ROOT/"README.md").read_text(encoding="utf-8").lower()
for term in ["business","architecture","kafka","cassandra","reproducibility","methodology"]:
    if term not in readme: errors.append(f"README missing concept: {term}")
if errors:
    print("\n".join(f"ERROR {e}" for e in errors)); sys.exit(1)
print("PASS repository structure, Python syntax, and README contract")
