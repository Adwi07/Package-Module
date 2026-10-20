from numbers import Real
import statistics as stats


def _validate_data(data):
    if isinstance(data, (str, bytes)):
        raise TypeError("Input must be a collection of numbers.")

    try:
        values = list(data)
    except TypeError as exc:
        raise TypeError(
            "Input must be an iterable of numbers."
        ) from exc

    if not values:
        raise ValueError("The data collection cannot be empty.")

    for value in values:
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("All values must be numeric.")

    return values


def calculate_mean(data):
    values = _validate_data(data)
    return stats.mean(values)


def calculate_median(data):
    values = _validate_data(data)
    return stats.median(values)


def calculate_mode(data):
    values = _validate_data(data)
    return stats.multimode(values)


def calculate_standard_deviation(data, sample=True):
    values = _validate_data(data)

    if sample and len(values) < 2:
        raise ValueError(
            "Sample standard deviation requires at least two values."
        )

    if not sample and len(values) < 1:
        raise ValueError("Data cannot be empty.")

    if sample:
        return stats.stdev(values)

    return stats.pstdev(values)