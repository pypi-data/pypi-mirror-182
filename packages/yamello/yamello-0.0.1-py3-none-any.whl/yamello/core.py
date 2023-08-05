from typing import Union, Callable, Any, TypeAlias

import math


space_char: str = ' '
linebreak_char: str = '\n'
comment_char: str = '#'
#
define_alias_char: str = '&'
reference_alias_char: str = '*'
#
double_colon_char: str = ':'
bracket_left_char: str = '['
bracket_right_char: str = ']'
curly_left_char: str = '{'
curly_right_char: str = '}'
comma_char: str = ','
#
minus_or_dash_char: str = '-'
point_char: str = '.'
underscore_char: str = '_'
#
digits: str = '0123456789'
exponent_char: str = 'e'
#
str_delimiter: str = '"'
#
letters_lower: str = 'abcdefghijklmnopqrstuvwxyz'
letters_upper: str = letters_lower.upper()
letters_all = letters_lower + letters_upper
#
letters_and_digits = letters_all + underscore_char + digits
#
true: str = 'true'
false: str = 'false'
null: str = 'null'
inf: str = 'inf'
minf: str = '-inf'


content_t: TypeAlias = Union[int, float, str, bool, "Token", dict[str, "Token"],
                             list["Token"]] | None


class Token(object):

    class TType(object):  # token type
        STRING: str = 'string'
        INTEGER: str = 'int'
        FLOAT: str = 'float'
        BOOL: str = 'bool'
        NULL: str = 'null'
        INF: str = 'infinity'
        MINF: str = '-infinity'

        KEY: str = 'key'
        ALIAS: str = 'alias'
        ALIASREF: str = 'alias-reference'

        PAIR: str = 'key:val-pair'
        LIST: str = 'list'
        DICT: str = 'dict'

    ttype: str = None  # token type
    name: str | None = None
    content: content_t = None

    def __init__(self, ttype: str, *, name: str | None = None, content: content_t = None):
        self.ttype = ttype
        self.name = name
        self.content = content

    def __str__(self) -> str:
        if isinstance(self.content, Token): _c: str = self.content.ttype
        elif isinstance(self.content, str):
            _c: str = '"' + '\\n'.join(self.content.split('\n')) + '"'
        elif isinstance(self.content, list): _c: str = '<' + ', '.join(entry.ttype for entry in self.content) + '>'
        else: _c: str = str(self.content)
        return f'Token(ttype: {self.ttype}, name: {self.name}, content: {_c})'

    def __repr__(self) -> str: return self.__str__()


def key_token(name: str) -> Token:
    return Token(ttype = Token.TType.KEY, name = name)


def alias_token(name: str, content: Token) -> Token:
    return Token(ttype = Token.TType.ALIAS, name = name, content = content)


def alias_reference_token(name: str = '') -> Token: return Token(ttype = Token.TType.ALIASREF, name = name)


def string_token(content: content_t) -> Token: return Token(ttype = Token.TType.STRING, content = content)


def convert_token_key_to_string(key_token_inst: Token) -> Token:
    if key_token_inst.ttype != Token.TType.KEY: raise AssertionError('placeholder')
    return string_token(key_token_inst.name)


def convert_token_string_to_key(str_token_inst: Token) -> Token:
    if str_token_inst.ttype != Token.TType.STRING: raise AssertionError('placeholder')
    return key_token(str_token_inst.content)


def int_token(number: int) -> Token: return Token(ttype = Token.TType.INTEGER, content = number)


def float_token(number: float) -> Token: return Token(ttype = Token.TType.FLOAT, content = number)


def inf_token(positive: bool = True) -> Token:
    if positive: return Token(ttype = Token.TType.INF)
    return Token(ttype = Token.TType.MINF)


def bool_token(val: bool) -> Token: return Token(ttype = Token.TType.BOOL, content = val)


def null_token() -> Token: return Token(ttype = Token.TType.NULL)


def pair_token(key: Token, val: Token) -> Token:
    return Token(ttype = Token.TType.PAIR, content = dict(key = key, val = val))


def list_token(content: content_t) -> Token: return Token(ttype = Token.TType.LIST, content = content)


def dict_token(content: content_t) -> Token:
    content.sort(key = lambda args: args.content['key'].name)
    return Token(ttype = Token.TType.DICT, content = content)


def retrieve_char(pointer: int, serial: str, reaction: Callable[[int, str], Any] | None = None):
    try: return serial[pointer]
    except IndexError:
        if reaction is None: raise AssertionError('placeholder')
        else: return reaction(pointer, serial)


def expect_chars_and_get_past(pointer: int, serial: str, expected: str):
    for char_expected in expected:
        char = retrieve_char(pointer, serial)
        if char != char_expected: raise AssertionError('placeholder')
        pointer += 1
    return pointer


def get_past_comment(pointer: int, serial: str) -> int:
    pointer = expect_chars_and_get_past(pointer, serial, comment_char)
    while True:
        char = retrieve_char(pointer, serial, lambda *args: None)
        if char is None: break
        if char == linebreak_char: break
        pointer += 1
    return pointer


def get_past_whitespace(pointer: int, serial: str, expect_at_least_one_space: bool = False) -> int:
    if expect_at_least_one_space: pointer = expect_chars_and_get_past(pointer, serial, space_char)
    while True:
        char = retrieve_char(pointer, serial, lambda *args: None)
        if char is None: break
        if char != space_char: break
        pointer += 1
    return pointer


def get_past_whitespace_and_linebreak(pointer: int, serial: str) -> int:
    while True:
        char = retrieve_char(pointer, serial, lambda *args: None)
        if char is None: break
        if char == comment_char: pointer = get_past_comment(pointer, serial)
        elif not (char in (space_char, linebreak_char)): break
        pointer += 1
    return pointer


def _gather_string(pointer: int, serial: str) -> tuple[int, Token]:
    pointer = get_past_whitespace(pointer, serial)

    if retrieve_char(pointer, serial) != str_delimiter: raise AssertionError('placeholder')
    out: str = ""
    while True:
        pointer += 1
        char = retrieve_char(pointer, serial)
        if (char == str_delimiter) and (serial[pointer - 1] != '\\'): break
        out += char
    return pointer + 1, string_token(content = out)


def _gather_int_or_float(pointer: int, serial: str) -> tuple[int, Token]:
    pointer = get_past_whitespace(pointer, serial)

    out: str = ''
    is_first_char: bool = True
    point_appeared: bool = False
    most_recent_char_was_digit: bool = False
    expect_one_more_digit: bool = False
    while True:
        char = retrieve_char(pointer, serial, lambda *args: None)
        if char is None: break
        elif char == minus_or_dash_char:
            if is_first_char:
                out += char
                most_recent_char_was_digit = False
                expect_one_more_digit = True
            else: raise AssertionError('placeholder')
        elif char in digits:
            out += char
            most_recent_char_was_digit = True
            expect_one_more_digit = False
        elif char == point_char:
            if not most_recent_char_was_digit: raise AssertionError('placeholder')
            if point_appeared: raise AssertionError('placeholder')
            out += char
            point_appeared = True
            most_recent_char_was_digit = False
            expect_one_more_digit = True
        elif char == underscore_char:
            if not most_recent_char_was_digit: raise AssertionError('placeholder')
            out += char
            most_recent_char_was_digit = False
            expect_one_more_digit = True
        elif char == exponent_char:
            if not most_recent_char_was_digit: raise AssertionError('placeholder')
            out += char
            point_appeared = True
            most_recent_char_was_digit = False
            expect_one_more_digit = True
        else: break  # raise AssertionError('placeholder')
        is_first_char = False
        pointer += 1

        if char in (space_char, linebreak_char): break
    if expect_one_more_digit: raise AssertionError('placeholder')
    if len(out) == 0: raise AssertionError('placeholder')

    if point_appeared: return pointer, float_token(number = float(out))
    return pointer, int_token(number = int(out))


def _gather_false_true_null_inf(pointer: int, serial: str) -> tuple[int, Token]:
    pointer = get_past_whitespace(pointer, serial)
    special: str = ''
    while True:
        special += retrieve_char(pointer, serial)
        for keyword in (true, false, null, inf, minf):
            if special.lower() in keyword: break
        else: raise AssertionError('placeholder')
        pointer += 1
        if special.lower() == true:
            token: Token = bool_token(True)
            break
        if special.lower() == false:
            token: Token = bool_token(False)
            break
        if special.lower() == null:
            token: Token = null_token()
            break
        if special.lower() == inf:
            token: Token = inf_token()
            break
        if special.lower() == minf:
            token: Token = inf_token(positive = False)
            break
    return pointer, token


def gather_base_datatype(pointer: int, serial: str, am: "AliasManager") -> tuple[int, Token]:
    pointer = get_past_whitespace(pointer, serial)
    char = retrieve_char(pointer, serial)

    if char == str_delimiter: return _gather_string(pointer, serial)
    if char in letters_upper + letters_lower + minus_or_dash_char:
        try: return _gather_false_true_null_inf(pointer, serial)
        except AssertionError: pass
    if char == define_alias_char: return am.gather_alias_on_make(pointer, serial)
    if char == reference_alias_char:
        pointer, out = am.gather_alias_reference(pointer, serial)
        if out.ttype == Token.TType.KEY: out = convert_token_key_to_string(out)
        return pointer, out
    return _gather_int_or_float(pointer, serial)


def gather_key(pointer: int, serial: str, am: "AliasManager") -> tuple[int, Token]:
    pointer = get_past_whitespace(pointer, serial)
    key: str = ''
    is_first_char: bool = True
    while True:
        char = retrieve_char(pointer, serial, lambda *args: None)
        if char is None: break
        if not (char in letters_and_digits): break

        if is_first_char:
            if char in digits: raise AssertionError('placeholder')
            is_first_char = False
        key += serial[pointer]
        pointer += 1
    if len(key) == 0:
        if char == str_delimiter: return _gather_string(pointer, serial)
        elif char == define_alias_char: return am.gather_alias_on_make(pointer, serial)
        elif char == reference_alias_char: return am.gather_alias_reference(pointer, serial)
        raise AssertionError('placeholder')
    return pointer, key_token(name = key)


def gather_key_value_pair(pointer: int,
                          serial: str,
                          pre_token: Token,
                          am: "AliasManager") -> tuple[int, Token]:
    pointer = expect_chars_and_get_past(pointer, serial, double_colon_char)
    if pre_token.ttype == Token.TType.STRING: pre_token = convert_token_string_to_key(pre_token)
    if pre_token.ttype != Token.TType.KEY: raise AssertionError('placeholder')
    pointer = get_past_whitespace_and_linebreak(pointer, serial)
    char = retrieve_char(pointer, serial)
    if char in (bracket_left_char, curly_left_char): pointer, value = gather_inline_seq(pointer, serial, am)
    else: pointer, value = gather_base_datatype(pointer, serial, am)
    return pointer, pair_token(key = pre_token, val = value)


def gather_inline_seq(pointer: int, serial: str, am: "AliasManager") -> tuple[int, Token]:
    char = retrieve_char(pointer, serial)
    if char == bracket_left_char:
        expected_right = bracket_right_char
        seq_type: str = Token.TType.LIST
    elif char == curly_left_char:
        expected_right = curly_right_char
        seq_type: str = Token.TType.DICT
    else: raise AssertionError('placeholder')
    pointer += 1

    contents: list[Token] = list()
    while True:
        pointer = get_past_whitespace_and_linebreak(pointer, serial)
        char = retrieve_char(pointer, serial)
        if seq_type == Token.TType.DICT:
            pointer, key = gather_key(pointer, serial, am)
            pointer = get_past_whitespace(pointer, serial)
            pointer, entry = gather_key_value_pair(pointer, serial, key, am)
        elif seq_type == Token.TType.LIST:
            if char in (bracket_left_char, curly_left_char): pointer, entry = gather_inline_seq(pointer, serial, am)
            else: pointer, entry = gather_base_datatype(pointer, serial, am)
        else: raise AssertionError('placeholder')
        contents.append(entry)

        pointer = get_past_whitespace_and_linebreak(pointer, serial)
        char = retrieve_char(pointer, serial)
        if char == expected_right: break
        pointer = expect_chars_and_get_past(pointer, serial, comma_char)

    if seq_type == Token.TType.LIST: return pointer + 1, list_token(content = contents)
    elif seq_type == Token.TType.DICT: return pointer + 1, dict_token(content = contents)
    raise AssertionError('placeholder')


class AliasManager(object):
    all_alias: dict[str, Token] = None

    def __init__(self): self.all_alias = dict()

    def gather_alias_on_make(self, pointer: int, serial: str) -> tuple[int, Token]:
        pointer = expect_chars_and_get_past(pointer, serial, define_alias_char)
        pointer, key = gather_key(pointer, serial, self)
        pointer = get_past_whitespace(pointer, serial, expect_at_least_one_space = True)
        try: pointer, content = gather_base_datatype(pointer, serial, self)
        except AssertionError:
            try: pointer, content = gather_key(pointer, serial, self)
            except AssertionError: pointer, content = gather_inline_seq(pointer, serial, self)

        if key.name in self.all_alias: raise AssertionError('placeholder')  # each alias can be defined once only!
        self.all_alias[key.name] = alias_token(name = key.name, content = content)
        return pointer, self.all_alias[key.name].content

    def gather_alias_reference(self, pointer: int, serial: str) -> tuple[int, Token]:
        pointer = expect_chars_and_get_past(pointer, serial, reference_alias_char)
        pointer, key = gather_key(pointer, serial, self)

        if not (key.name in self.all_alias): raise AssertionError('placeholder')  # has to be defined already!
        return pointer, self.all_alias[key.name].content


def _deserialize(token: Token, vc: Callable = list) -> Any:
    if token.ttype == Token.TType.INTEGER: return token.content
    if token.ttype == Token.TType.FLOAT: return token.content
    if token.ttype == Token.TType.INF: return math.inf
    if token.ttype == Token.TType.MINF: return -math.inf
    if token.ttype == Token.TType.STRING: return token.content
    if token.ttype == Token.TType.BOOL: return token.content
    if token.ttype == Token.TType.NULL: return None
    if token.ttype == Token.TType.LIST: return vc(_deserialize(entry, vc = vc) for entry in token.content)
    if token.ttype == Token.TType.DICT:
        return {pair.content['key'].name: _deserialize(pair.content['val'], vc = vc) for pair in token.content}
    raise AssertionError('placeholder')


def deserialize(serial: str, vec_constructor: Callable = list) -> Any:
    if len(serial.strip()) == 0: return None
    alias_manager = AliasManager()
    pointer: int = 0
    try: pointer, outer = gather_base_datatype(pointer, serial, alias_manager)
    except AssertionError: pointer, outer = gather_inline_seq(pointer, serial, alias_manager)
    return _deserialize(outer, vc = vec_constructor)


def _serialize(stuff: Any,
               indent: str,
               skip_indent_first_line: bool,
               suppress_quotes: bool,
               is_key: bool) -> str:
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
            if not (_filtered[0] in letters_all): _do = False
            for letter in _filtered:
                if not (letter in letters_and_digits): _do = False
            if _do: return f'{_indent}{_filtered}'
        return f'{_indent}"{_filtered}"'
    if stuff is None: return f'{_indent}null'

    if isinstance(stuff, list): stuff = tuple(stuff)
    if isinstance(stuff, tuple):
        if len(stuff) == 0: return "[]"
        out: str = f'{_indent}['
        for entry in stuff:
            entry_str: str = _serialize(entry,
                                        indent = indent + "  ",
                                        skip_indent_first_line = False,
                                        suppress_quotes = suppress_quotes,
                                        is_key = False)
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
                                      is_key = True)
            val_str: str = _serialize(stuff[key],
                                      indent = succ_indent,
                                      skip_indent_first_line = True,
                                      suppress_quotes = suppress_quotes,
                                      is_key = False)
            out += f'\n{key_str}: {val_str},'
            _indent = indent
        return out[:-1] + '}'

    raise AssertionError('placeholder')


def serialize(stuff: Any, suppress_quotes: bool = True) -> str:
    out = _serialize(stuff,
                     indent = '',
                     skip_indent_first_line = False,
                     suppress_quotes = suppress_quotes,
                     is_key = False)
    if out[-1] != '\n': out += '\n'
    return out
