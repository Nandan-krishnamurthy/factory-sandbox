"""Command line: ``python -m tempconv <celsius>`` prints the temperature in Fahrenheit."""

import sys

from tempconv.convert import celsius_to_fahrenheit


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    print(celsius_to_fahrenheit(float(args[0])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
