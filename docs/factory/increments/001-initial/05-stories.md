# Stories: 001-initial

Stories are cut from [04-implementation-plan.md](04-implementation-plan.md), in build order. Each is meant to be reviewable in about 15 minutes and to leave `main` working. `Blocked by` lists the stories that must be merged first.

## M1: Walking skeleton and conversion

### STORY-001: Walking skeleton: convert Celsius to Fahrenheit
- Traces to: REQ-001, REQ-002, REQ-003, REQ-006, REQ-007
- Blocked by: None
- Milestone: M1
#### Story
As a developer at a terminal, I want `python -m tempconv <celsius>` to print the temperature in Fahrenheit so that I can convert a temperature without doing the arithmetic myself.
#### Acceptance criteria
- AC1: Given the argument `100`, when `python -m tempconv 100` runs, then it prints `212.0` and exits with status 0.
- AC2: Given the argument `-40`, when the tool runs, then it prints `-40.0`.
- AC3: Given the argument `36.6`, when the tool runs, then it prints `97.88` (rounded to two decimal places).
- AC4: Given the repository, when `python -m unittest` runs from its root, then the tests run and pass, and the package imports only standard-library modules.
- AC5: Given `.factory/config.json`, when this story is merged, then `commands.test` is `python -m unittest`, and `commands.install`, `commands.build`, `commands.lint` and `commands.typecheck` stay `null`.
#### Out of scope
- Missing, extra or invalid arguments (the next story).
- Other units, packaging, CI and deployment.
#### Technical notes
- Files: `tempconv/__init__.py` (empty), `tempconv/convert.py` (`celsius_to_fahrenheit`), `tempconv/__main__.py` (`main(argv)`), `tests/__init__.py`, `tests/test_convert.py`, `tests/test_cli.py`.
- Round with `round(value, 2)` and print the `float` as is (`03-architecture.md`, decision 3).
- No third-party dependencies and no dependency file (REQ-006).
#### Test plan
- Unit: `celsius_to_fahrenheit` for 100, -40 and 36.6.
- End-to-end: run `python -m tempconv` with `sys.executable` as a subprocess for each PRD example, and check standard output and the exit status.

## M2: Invalid input

### STORY-002: Reject a missing or invalid argument
- Traces to: REQ-004, REQ-005
- Blocked by: STORY-001
- Milestone: M2
#### Story
As a developer at a terminal, I want a clear error when I forget the temperature or mistype it so that I know what went wrong instead of seeing a traceback.
#### Acceptance criteria
- AC1: Given no argument, when `python -m tempconv` runs, then it prints a short error message to standard error, nothing to standard output, and exits with status 2.
- AC2: Given the argument `abc`, when the tool runs, then it prints a short error message to standard error, nothing to standard output, and exits with status 2.
- AC3: Given the argument `nan` or `inf`, when the tool runs, then it is rejected in the same way as `abc`.
- AC4: Given two arguments, when the tool runs, then it prints a short error message to standard error and exits with status 2.
#### Out of scope
- Accepting units or other formats in the argument.
#### Technical notes
- Only `tempconv/__main__.py` and `tests/test_cli.py` change. Use `math.isfinite` for the `nan`/`inf` check.
#### Test plan
- End-to-end: subprocess tests for no argument, `abc`, `nan`, `inf` and two arguments, checking standard error, empty standard output and exit status 2.
