from yamello.yamello_token import Parser as _Parser, letter_all_chars, letter_and_digit_chars

from typing import Callable, Any


def deserialize(serial: str, vec_constructor: Callable = list) -> Any:
    pp: _Parser = _Parser(serial = serial)
    pp.tokenize()
    return pp.parse(vec_constructor = vec_constructor)


def _serialize(stuff: Any,
               indent: str,
               skip_indent_first_line: bool,
               suppress_quotes: bool,
               is_key: bool,
               list_allowed: bool,
               tuple_allowed: bool) -> str:
    if skip_indent_first_line: _indent: str = ''
    else: _indent: str = indent

    if isinstance(stuff, int): return f'{_indent}{stuff}'
    if isinstance(stuff, float): return f'{_indent}{stuff}'  # covers math.inf, numpy.inf
    if isinstance(stuff, bool): return f'{_indent}{stuff}'
    if isinstance(stuff, str):
        _filtered: str = '\\"'.join(stuff.split('"'))
        if suppress_quotes and is_key:
            _do: bool = True
            if len(_filtered.split(' ')) != 1: _do = False
            if not (_filtered[0] in letter_all_chars): _do = False
            for letter in _filtered:
                if not (letter in letter_and_digit_chars): _do = False
            if _do: return f'{_indent}{_filtered}'
        return f'{_indent}"{_filtered}"'
    if stuff is None: return f'{_indent}null'

    if isinstance(stuff, (tuple, list)):
        if not (list_allowed or tuple_allowed): raise AssertionError('placeholder')
        if isinstance(stuff, tuple) and (not tuple_allowed): raise AssertionError('placeholder')
        if isinstance(stuff, list) and (not list_allowed): raise AssertionError('placeholder')

        if len(stuff) == 0: return "[]"
        out: str = f'{_indent}['
        for entry in stuff:
            entry_str: str = _serialize(entry,
                                        indent = indent + "  ",
                                        skip_indent_first_line = False,
                                        suppress_quotes = suppress_quotes,
                                        is_key = False,
                                        list_allowed = list_allowed,
                                        tuple_allowed = tuple_allowed)
            out += f'\n{entry_str},'
            _indent = indent
        return out[:-1] + ']'

    if isinstance(stuff, dict):
        if len(stuff) == 0: return "{}"
        keys = list(stuff.keys())
        keys.sort()
        succ_indent: str = indent + "  "
        out: str = f'{_indent}' + '{'
        for key in keys:
            key_str: str = _serialize(key,
                                      indent = succ_indent,
                                      skip_indent_first_line = False,
                                      suppress_quotes = suppress_quotes,
                                      is_key = True,
                                      list_allowed = list_allowed,
                                      tuple_allowed = tuple_allowed)
            val_str: str = _serialize(stuff[key],
                                      indent = succ_indent,
                                      skip_indent_first_line = True,
                                      suppress_quotes = suppress_quotes,
                                      is_key = False,
                                      list_allowed = list_allowed,
                                      tuple_allowed = tuple_allowed)
            out += f'\n{key_str}: {val_str},'
            _indent = indent
        return out[:-1] + '}'

    raise AssertionError('placeholder')


def serialize(stuff: Any,
              suppress_quotes: bool = True,
              list_allowed: bool = True,
              tuple_allowed: bool = False) -> str:
    out = _serialize(stuff,
                     indent = '',
                     skip_indent_first_line = False,
                     suppress_quotes = suppress_quotes,
                     is_key = False,
                     list_allowed = list_allowed,
                     tuple_allowed = tuple_allowed)
    if out[-1] != '\n': out += '\n'
    return out
