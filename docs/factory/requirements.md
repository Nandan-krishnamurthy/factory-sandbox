# Requirements: Temperature converter

## Goal
A tiny command-line tool that converts a temperature from Celsius to Fahrenheit. It exists only to exercise the AI Software Factory, so it should be as small as possible.

## Users
One developer running the tool in a terminal.

## Functional requirements
1. Running `python -m tempconv 100` prints `212.0`. In general, given one number in degrees Celsius, the tool prints the value in degrees Fahrenheit (`F = C × 9/5 + 32`), as a decimal number.
2. Negative and decimal inputs work, e.g. `-40` prints `-40.0` and `36.6` prints `97.88` (rounded to two decimal places).
3. If the argument is missing or is not a number, the tool prints a short error message to standard error and exits with status 2.

## Non-functional requirements
- Python 3.10 or later, standard library only: no third-party dependencies.
- Tests use the standard library's `unittest` (`python -m unittest`).

## Out of scope
- Other units (Kelvin, Fahrenheit to Celsius).
- Packaging, publishing, CI and deployment.
