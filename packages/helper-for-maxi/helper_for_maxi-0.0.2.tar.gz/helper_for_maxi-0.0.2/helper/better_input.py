from .better_print import better_print as BetterPrint


def better_input(text=' ', end=' ', delay=None):
    r"""Prints the given
    """
    if delay is not None:
        BetterPrint(text, delay)
    else:
        BetterPrint(text)
    res = input(end)
    return res