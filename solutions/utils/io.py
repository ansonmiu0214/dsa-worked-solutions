from typing import Callable, List, TypeVar

StringFunc = Callable[[], str]
T = TypeVar('T')
Constructor = Callable[[], T]

def get(of: Constructor[T], *,
        stdin: StringFunc = input,
        strip: bool = True) -> T:
    """Get value of type 'of' from 'stdin'."""

    raw_input = stdin().strip() if strip else stdin()
    return of(raw_input)

def get_list(of: Constructor[T], *,
             stdin: StringFunc = input,
             strip: bool = True,
             delimiter: str = ' ') -> List[T]:
    """Get list of values of type 'of' from 'stdin'."""
    
    raw_input = stdin().strip() if strip else stdin()
    delimited_raw_input = raw_input.split(delimiter)
    return list(map(of, delimited_raw_input))
    

