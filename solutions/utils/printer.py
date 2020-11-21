def pluralise(**kwargs) -> str:
    """Return plural of '{val}' '{unit}' depending on 'val'.
    kwargs is a singleton dictionary of unit=val."""

    assert len(kwargs) == 1

    [(unit, val)] = kwargs.items()
    if unit.endswith('s'):
        transform = lambda s: s
    elif unit.endswith('y'):
        transform = lambda s: f'{s[:-1]}ies'
    else:
        transform = lambda s: f'{s}s'

    return f'{val} {transform(unit)}'