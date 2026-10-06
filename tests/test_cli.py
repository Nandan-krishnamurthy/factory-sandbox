import ast
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def run(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-m", "tempconv", *args], cwd=ROOT,
                          capture_output=True, text=True)


class CommandLineTest(unittest.TestCase):
    def assert_prints(self, arg: str, expected: str):
        result = run(arg)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout, expected + "\n")
        self.assertEqual(result.stderr, "")

    def test_10_ac1_prints_212_for_100(self):
        """#10 AC1: python -m tempconv 100 prints 212.0 and exits 0."""
        self.assert_prints("100", "212.0")

    def test_10_ac2_prints_minus_40_for_minus_40(self):
        """#10 AC2: python -m tempconv -40 prints -40.0."""
        self.assert_prints("-40", "-40.0")

    def test_10_ac3_prints_97_88_for_36_6(self):
        """#10 AC3: python -m tempconv 36.6 prints 97.88."""
        self.assert_prints("36.6", "97.88")


class ProjectTest(unittest.TestCase):
    def test_10_ac4_imports_only_the_standard_library(self):
        """#10 AC4: every module in tempconv imports only stdlib modules or tempconv itself."""
        allowed = set(sys.stdlib_module_names) | {"tempconv"}
        for path in (ROOT / "tempconv").glob("*.py"):
            for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
                names = []
                if isinstance(node, ast.Import):
                    names = [a.name for a in node.names]
                elif isinstance(node, ast.ImportFrom) and node.level == 0:
                    names = [node.module or ""]
                for name in names:
                    self.assertIn(name.split(".")[0], allowed, f"{path.name} imports {name}")

    def test_10_ac5_config_commands(self):
        """#10 AC5: commands.test is python -m unittest; the other commands stay null."""
        config = json.loads((ROOT / ".factory" / "config.json").read_text(encoding="utf-8"))
        commands = config["commands"]
        self.assertEqual(commands["test"], "python -m unittest")
        for name in ("install", "build", "lint", "typecheck"):
            self.assertIsNone(commands[name], name)


if __name__ == "__main__":
    unittest.main()
