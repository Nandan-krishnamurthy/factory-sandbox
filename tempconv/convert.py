"""Temperature conversion. Pure functions, no I/O."""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Degrees Celsius to degrees Fahrenheit, rounded to two decimal places."""
    return round(celsius * 9 / 5 + 32, 2)
