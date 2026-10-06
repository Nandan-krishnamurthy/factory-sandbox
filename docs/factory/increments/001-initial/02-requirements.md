# Requirements: 001-initial

## Functional
- **REQ-001** (PRD §Functional requirements 1): Running `python -m tempconv <celsius>` with one number prints that temperature in degrees Fahrenheit (`F = C × 9/5 + 32`) as a decimal number on standard output and exits with status 0; for example, `100` prints `212.0`.
- **REQ-002** (PRD §Functional requirements 2): A negative input is converted correctly; for example, `-40` prints `-40.0`.
- **REQ-003** (PRD §Functional requirements 2): A decimal input is converted and the result is rounded to two decimal places; for example, `36.6` prints `97.88`.
- **REQ-004** (PRD §Functional requirements 3): Running the tool with no argument prints a short error message to standard error, prints nothing to standard output, and exits with status 2.
- **REQ-005** (PRD §Functional requirements 3): Running the tool with an argument that is not a number (for example `abc`) prints a short error message to standard error, prints nothing to standard output, and exits with status 2.

## Non-functional
- **REQ-006** (PRD §Non-functional requirements): The tool runs on Python 3.10 or later and uses only the standard library; the project declares no third-party dependencies.
- **REQ-007** (PRD §Non-functional requirements): The tests use the standard library's `unittest` and the whole suite runs with `python -m unittest` from the repository root.

## Assumptions
- "As a decimal number" means Python's `float` text form of the result after rounding to two decimal places: whole results keep one decimal place (`212.0`, `32.0`) and trailing zeros beyond that are not added (`97.88`, `34.21`, not `34.210`).
- Rounding uses Python's built-in `round(value, 2)`.
- Any text that Python's `float()` accepts counts as a number (for example `1e2`), except `nan` and `inf` values, which are rejected like any other non-number (REQ-005).
- More than one argument is treated like a missing or invalid argument: an error on standard error and exit status 2.
- The project is a single package `tempconv` at the repository root, run with `python -m tempconv`.

## Out of scope
- Other units, such as Kelvin, or converting Fahrenheit to Celsius (PRD §Out of scope): excluded by the PRD.
- Packaging, publishing, CI and deployment (PRD §Out of scope): excluded by the PRD.

## Open questions
- Should more than one argument be an error (assumed), or should the extra arguments be ignored?
- Should `nan` and `inf` be rejected (assumed), or printed as Python prints them?

## PRD coverage
| PRD section | Requirements |
|---|---|
| Requirements: Temperature converter | REQ-001–REQ-007 |
| Goal | REQ-001 |
| Users | REQ-001 |
| Functional requirements | REQ-001, REQ-002, REQ-003, REQ-004, REQ-005 |
| Non-functional requirements | REQ-006, REQ-007 |
| Out of scope | Out of scope |
