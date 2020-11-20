def pluralise(**kwargs) -> str:
    """Return plural of '{val}' '{unit}' depending on 'val'.
    kwargs is a singleton dictionary of unit=val."""

    assert len(kwargs) == 1

    [(unit, val)] = kwargs.items()
    suffix = 's' if not unit.endswith('s') else 'es'

    return f'{val} {unit}{suffix if val != 1 else ""}'