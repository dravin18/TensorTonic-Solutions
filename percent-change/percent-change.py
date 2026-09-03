def percent_change(series: list) -> list:
    """
    Returns the fractional change between consecutive values.
    """
    # Write code here
    return [
        0.0 if series[index - 1] == 0
        else (num - series[index - 1]) / series[index - 1]
        for index, num in enumerate(series)
        if index != 0
    ]