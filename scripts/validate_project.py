"""Dependency-free repository structure and syntax gate."""
from pathlib import Path
import ast, sys
ROOT=Path(__file__).resolve().parents[1]
required=["README.md","producer.py","consumer.py","dashboard.py","query.py","requirements.txt","docker-compose.yml","data/sample_orders.csv","tests/test_pipeline.py",".github/workflows/ci.yml"]
errors=[f"missing: {p}" for p in required if not (ROOT/p).is_file()]
for path in list(ROOT.glob("*.py"))+list((ROOT/"tests").glob("*.py")):
    try: ast.parse(path.read_text(encoding="utf-8"),filename=str(path))
    except SyntaxError as exc: errors.append(f"{path.relative_to(ROOT)}: {exc}")
readme=(ROOT/"README.md").read_text(encoding="utf-8").lower()
for term in ["why it exists","data flow","kafka","parquet","tests","results","limitations"]:
    if term not in readme: errors.append(f"README missing concept: {term}")
if errors: print("\n".join(f"ERROR {e}" for e in errors)); sys.exit(1)
print("PASS ecommerce structure, Python syntax, and documentation contract")
