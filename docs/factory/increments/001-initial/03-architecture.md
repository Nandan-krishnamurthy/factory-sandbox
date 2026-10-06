# Architecture: 001-initial

## Overview
`tempconv` is a single Python package with no dependencies. A pure conversion function does the arithmetic, and a thin command-line entry point parses the one argument, calls it and prints the result. `python -m tempconv <celsius>` runs `tempconv/__main__.py`.

```text
python -m tempconv 36.6
        │
        ▼
tempconv/__main__.py ── main(argv) ── parse & validate argument ──► error: stderr, exit 2
        │
        ▼
tempconv/convert.py ── celsius_to_fahrenheit(c) ── round(c * 9 / 5 + 32, 2)
        │
        ▼
stdout: 97.88, exit 0
```

## Components
| Component | Responsibility | Interface |
|---|---|---|
| `tempconv/convert.py` | The conversion: `F = C × 9/5 + 32`, rounded to two decimal places. Pure, no I/O. | `celsius_to_fahrenheit(celsius: float) -> float` |
| `tempconv/__main__.py` | The command line: checks that there is exactly one argument and that it is a finite number, prints the result, or prints an error to standard error and returns status 2. | `main(argv: list[str] \| None = None) -> int`, called as `sys.exit(main())` |
| `tempconv/__init__.py` | Marks the package. Empty. | none |
| `tests/` | `unittest` tests for both modules. The command-line tests run `python -m tempconv` as a subprocess, so they check the real output and exit status. | `python -m unittest` |

## Data model
None. The tool takes one number and prints one number.

## Key decisions
1. **Parse the argument by hand, not with `argparse`.**
   Options: `argparse`, or checking `sys.argv` directly. `argparse` exits with status 2 on a missing argument, but its error text includes a usage block, and a number type with a custom error still needs the same finite-number check. With one argument, a direct check is shorter and makes every error path explicit. *Chosen: direct check.*
2. **Separate the conversion from the command line.**
   This keeps the arithmetic unit-testable without subprocesses, and the command line testable as the user runs it.
3. **Round with the built-in `round(value, 2)` and print the `float` as is.**
   This gives `212.0`, `-40.0` and `97.88`, as the PRD's examples show. *Chosen over* `format(value, '.2f')`, which would print `212.00`.
4. **Reject `nan` and `inf`.** `float()` accepts them, but they are not temperatures (assumption in `02-requirements.md`).

## Technology choices
- **Language:** Python 3.10 or later (REQ-006).
- **Dependencies:** none. Standard library only (REQ-006).
- **Tests:** the standard library's `unittest`, discovered by `python -m unittest` from the repository root (REQ-007).
- **Lint and type checking:** none are added in this increment. No requirement asks for them, and they would add dependencies. `commands.lint` and `commands.typecheck` stay `null`, and the PRs say these gates are skipped (rule H4).
- **No CI, packaging or deployment** (PRD §Out of scope; rules S5, S8).

## Requirement mapping
| Requirement | Component(s) |
|---|---|
| REQ-001 | `tempconv/convert.py`, `tempconv/__main__.py` |
| REQ-002 | `tempconv/convert.py` |
| REQ-003 | `tempconv/convert.py` |
| REQ-004 | `tempconv/__main__.py` |
| REQ-005 | `tempconv/__main__.py` |
| REQ-006 | whole project (no dependencies) |
| REQ-007 | `tests/` |
