"""Run all solution tests in the repo."""
import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).parent
SKIP_DIRS = {"templates", ".git", "__pycache__", ".venv"}


def discover_and_run():
    files = sorted(
        p for p in REPO.rglob("*.py")
        if p.name != "run_tests.py"
        and not any(part in SKIP_DIRS for part in p.parts)
    )

    passed, failed = 0, 0
    for filepath in files:
        module_name = filepath.stem
        spec = importlib.util.spec_from_file_location(module_name, filepath)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            if hasattr(module, "test"):
                module.test()
                passed += 1
        except Exception as e:
            print(f"FAIL: {filepath.relative_to(REPO)} - {e}")
            failed += 1

    print(f"\nResults: {passed} passed, {failed} failed")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    discover_and_run()
