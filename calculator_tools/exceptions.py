def safe_divide(a: float, b: float) -> float:
    try:
        if b == 0:
            raise ValueError("Cannot divide by zero.")

        return a / b

    except TypeError:
        raise TypeError("Both inputs must be valid numbers.")
    except ValueError as e:
        raise ValueError(str(e))