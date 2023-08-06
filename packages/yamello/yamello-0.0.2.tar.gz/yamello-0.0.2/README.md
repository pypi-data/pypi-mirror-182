# yamello

## author information
[codima](https://www.youtube.com/channel/UCwnthITQqkWgaHnz82U7WsA) (coding-mathmatics) on youtube

## Usage

this package can serialize as well as deserialize python 
data (`int`, `float`, `bool`, `str`, `math.inf`, `None`)
and data structures (`list` _or_ `tuple` & `dict`) into 
text-based files with suffix `.yamello` or `.yaml` or `.yml`.

As the last 2 suffixes indicate: **Yes, any** _yamello_ 
**file is supposed to satisfy the** _YAML_ **spec, too!**
Sometimes they can be valid _JSON_, too.

In comparision to the _Yaml_ file format, _yamello_ 
is way less capable to express exotic data and does purposefully 
not allow binary data dumps. 
The scope of _yamello_ is simply different and has 3 main goals:
 1. it essentially tries to feel like _JSON_ to users, but 
    mixed in with a bit of syntactic sugar
 2. the deserialization will respect or keep the ordering of 
    dictionary keys within _yamello_ files 
    (whatever ordering they may have in the first place)
 3. the serialization process of _yamello_ will order 
    dictionary keys alphabetically

Due to main goals 2 & 3 there is no canonicalization necessary 
when hashing serialized _yamello_ files; which (aside from
coding exploration) was the major reason to implement 
_yamello_ in the first place!

```python
from yamello import serialize, deserialize


''' deserialization '''
with open('demo_resources/demo.in.yaml', mode ='r') as in_stream:
    in_str = in_stream.read()
in_data = deserialize(in_str, vec_constructor = tuple)
print(in_data)

''' operations on the data '''
out_data = in_data

''' serialization '''
out_str: str = serialize(out_data)
with open('demo_resources/demo.out.yaml', mode ='w') as out_stream: 
    out_stream.write(out_str)
```

Please note: _yamello_ is written purely in _python_ and 
hence it was not developed with execution speed in mind.

## data

### int
`int` are composed of digits `0` to `9` (e.g. `1217`) 
and may include a leading minus `-` to indicate negative 
numbers (e.g. `-13`). 

**Caution:** numbers in scientific notation, e.g. `12e7`, will
be interpreted as `float`!

**Note:** one can write `inf` or `-inf` for infinity or 
negative infinity. 

**Note:** It is allowed to place underscores `_` in between digits for 
readability (e.g. `1_000_000` which is equivalent to 
`1_0_0000_0` as well as to `1000000`).

### float
`float` or floating point numbers. They are composed of 
digits `0` to `9`, including a point `.` as decimal seperator 
(e.g. `1.0` or `0.045` or `13.076`).
They may include a leading minus `-` to indicate negative 
numbers (e.g. `-70.09` or `-0.0007`).

**Note:** `float` can be written in scientific notation, 
i.e. in exponent notation including `e` (e.g. `1.4e-8` or 
`12e2` or `-0.3e2`)

**Note:** a decimal seperator is necessary, unless scientific
notion is in use.

**Note:** one can write `inf` or `-inf` for infinity or 
negative infinity. 

**Note:** It is allowed to place underscores `_` in between 
digits for readability (e.g. `1_000_000.0_0` or `1_0e2_0`).

**Caution:** decimal seperators `.` need to be 
surrounded by digits (e.g. `1.0` is valid as well as `0.01` 
whereas `1.` or `.01` are not)!

### bool
`bool` can be written as `True` or `False` (regardless of
upper and lower case, i.e. `true` is as much `True` as `tRuE`)

### str
`str` or strings always have to be enclosed by a pair of
double-quotes `"`, unless they are dictionary keys 
(see dictionaries) where they are optional.
Any composition of UTF-8 may appear in between a pair of 
double-quotes. 

**Note:** double quotes can be escaped using backslash `\"` 
to include double-quotes into strings.

**Caution:** single-quotes `'` are simply ignored during the 
deserialization process to decide whether something is a 
string or not. 

### None
`None` can be denoted by `null` (regardless of
upper and lower case, e.g. `NULL` or `Null` 
or `nuLL` are valid as well)

### infinity 
`inf` or `-inf` represent infinity or negative infinity 
(again regardless of lower and upper case).

**Note:** The serialization will convert `math.inf` (from the 
math library) or `numpy.inf` (from the numpy library) into
`inf`. 

**Note:** The deserialization will convert `inf` into 
`math.inf` (from the math library).

## data structures

### inline dict
Inline `dict` or dictionaries are enclosed by a pair of
curly-braces `{` and `}`. They are an **ordered** list of 
`key: value` pairs, seperated by commas `,`. Hence, the 
general structure follows:

```yaml
{ key1: value1, key2: value2, ... }
```
or
```yaml
{
  key1:
    value1,
  
  key2: value2 }
```
as linebreaks do not matter.

- `key` is either a string enclosed by a pair of double-quotes `"`
  or a (not enclosed) string containing characters `a` to `z`, 
  `A` to `Z`, underscore `_` and digits `0` to `9` 
  (provided the character is not a digit).
- `value` is any _data_ discussed above or another inline `dict` 
  or an inline `list`. 

```yaml
{
  valid_not_enclosed_key: 99,
  "quotes enclosed key due to white spaces": -17.02,
  _anotehr_valid_key: "message"
}
```

**Caution:** repeated `keys` within the same dictionary will 
overwrite each other (last one counts)! 

### (regular) dict
Regular aka "not inline" `dicts` are essentially equivalent to 
inline `dicts` (-> see inline `dicts`). The only two differences 
are the syntax and the fact that `values` 
(from the `key:value` pairs) can be another 
regular `dict` or a regular `list`, too.

Regarding the syntax: A regular `dict` is not surrounded 
by curly-braces. 
Instead, a line break followed by a consistent increase 
of indentation (in front of `keys`) mark the beginning, 
as well as a decrease (by the same amount of characters) 
of indentation mark the end of a regular `dict`.
The indentation of `values` (for those `values` that are 
put on one of the next lines) have to be consistent among `values`
and larger than that of their `keys`. 
Furthermore, line breaks replace commas to 
separate `key:value` pairs from one another. 

```yaml
upper_level_key1:  # regular structs (dict and list) require line break ...
  key1: value1  # ... hence a new (regular) dict starts here
  key2: value2

  key3:  # empty lines and ... 
    value3  # ... linebreaks between keys and values are allowed
  
  key4:  # also empty lines between keys and ...
    
    value4  # ... values are allowed
upper_level_key2: upper_level_value2
```

### inline list
Inline `list` or lists are enclosed by a pair of
brackets `[` and `]`. They are an **ordered** collection of 
`entries`, seperated by commas `,`. Hence, the 
general structure follows:

```yaml
[ value1, value2, ... ]
```
or
```yaml
[
  value1,
  
  value2 ]
```
as linebreaks again do not matter.

- `entry` is any _data_ discussed above or another inline `dict` 
  or an inline `list`.

### (regular) list
Regular aka "not inline" `lists` are essentially equivalent to 
inline `lists` (-> see inline `list`). The only two differences 
are the syntax and the
fact that `entries` can be another regular `dict` or a regular `list`, too.

Regarding the syntax: A regular `list` is not surrounded 
by brackets. 
Instead, a line break followed by a consistent increase 
of indentation mark the beginning, 
as well as a decrease (by the same amount of characters) 
of indentation mark the end of a regular `list`.
Every entry has to be introduced by a dash `-` followed by at least one 
space. The indentation of `entries` (for those `entries` that are 
put on one of the next lines) have to be consistent among such `entries`
and larger than that compared to the indentation of their dashes `-`. 
Furthermore, line breaks replace commas to 
separate `entries` from one another.

```yaml
upper_level_key1:  # following struct is equivalent to [value1, value2, value3, value4]
  - value1
  - value2

  - value3
  
  - # line breaks are valid, but require either a comment or your IDE not to delete trailing whitespaces
    value4
upper_level_key2:  # following struct is equivalent to [[value5, value6], [value7], value8]
  - - value5
    - value6
  - - value7
  - value9
upper_level_key3: upper_level_value3
```

## additional features

### comments
everything after `#` on any line is considered as a comment
and ignored by the parser during deserialization.

### alias
Any data as well as inline data struct can be aliased for re-use.
The definition of a new alias is introduced by `&` and the use of an 
alias is introduced by `*`. Using an alias requires it definition to take 
place further up the same document. The same alias can be defined only once. 

```yaml
upper_level_key1:
  &key1 "content"  # defines alias of name: "key1" with value: "content"
upper_level_key2:
  *key1  # substitutes the value: "content" stored under the alias with name: "key1"
&key2 upper_level_key3: &other_key [99, inf, null]  # defines to alias
upper_level_key4:
  - *key2  # substitutes the (string) value: "upper_level_key3"
  - *other_key  # substitutes the (inline list) value: [99, inf, null]
```

**Note:** rules for alias names are the same as for not (by double quotes) 
enclosed dictionary keys, i.e. upper, lower case letters, underscore.
Except for the first character also digits may be used within

## docs

... *under construction*

[//]: # ([https://berlinade.gitlab.io/tomarkdown/]&#40;https://berlinade.gitlab.io/tomarkdown/&#41;)

## TODOs
 
 - write MkDocs documentation
 - (maybe) write an actual spec
 - exchange all
    ```python 
        raise Assertion('palceholder')
    ```
   for proper Exceptions within the code!

#### informal info on license (english)
This repository is licensed under GPL-V3 (see LICENSE). You can refer to the author of this package as codima & ... .
