# Implementation plan: 001-initial

## Milestones

### M1: Walking skeleton and conversion
- **Goal:** create the `tempconv` package and the `unittest` test suite, and make `python -m tempconv <celsius>` print the converted temperature for valid input. This is the walking skeleton: the scaffold, the test runner and passing tests.
- **Requirements:** REQ-001, REQ-002, REQ-003, REQ-006, REQ-007
- **Demo:** `python -m tempconv 100` prints `212.0`, `-40` prints `-40.0`, `36.6` prints `97.88`; `python -m unittest` runs and passes.

### M2: Invalid input
- **Goal:** reject a missing argument, extra arguments and anything that is not a finite number, with a short message on standard error and exit status 2.
- **Requirements:** REQ-004, REQ-005
- **Demo:** `python -m tempconv` and `python -m tempconv abc` each print an error to standard error, nothing to standard output, and exit with status 2.

## Dependencies
```text
M1 walking skeleton + conversion ──► M2 invalid input
```
M2 changes the command-line entry point and the test suite that M1 creates.

## Testing approach
| What | Kind | How |
|---|---|---|
| The conversion and rounding (REQ-001–REQ-003) | Unit | `unittest` tests of `celsius_to_fahrenheit` |
| Output and exit status of the command (REQ-001–REQ-005) | End-to-end | `unittest` tests that run `python -m tempconv` as a subprocess with `sys.executable`, and check standard output, standard error and the exit status |
| Standard library only (REQ-006) | Static check | A test that the package imports only standard-library modules, plus review: no dependency file is added |
| The suite runs with `python -m unittest` (REQ-007) | Command | Running the test command itself |

`.factory/config.json` has every `commands` value `null` today. The first M1 story introduces the test command (`python -m unittest`) and sets `commands.test` after running it successfully. `build`, `lint` and `typecheck` stay `null`: the project has no build step, linter or type checker (see `03-architecture.md`).

## Requirement coverage
| Requirement | Milestone |
|---|---|
| REQ-001 | M1 |
| REQ-002 | M1 |
| REQ-003 | M1 |
| REQ-004 | M2 |
| REQ-005 | M2 |
| REQ-006 | M1 |
| REQ-007 | M1 |

## Risks
- **Floating-point output differs from the examples** (for example `97.88000000000001`). *Mitigation:* round with `round(value, 2)`, and test each PRD example exactly.
- **The subprocess tests use a different Python from the one running the suite.** *Mitigation:* start the subprocess with `sys.executable`, from the repository root.
- **Open questions answered differently at Gate A** (extra arguments, `nan`/`inf`). *Mitigation:* each affects only the M2 story, and can be revised in this PR before any code exists.
