# EasyNERTag: Easy tagging for annotate NER corpus

> Easy tagging for annotate NER corpus

This is tool for helping you to create named entity recognition corpus in conll2002 format. It wants just a tag like [BBCoode](https://en.wikipedia.org/wiki/BBCode).

## Install

> pip install easynertag

## How to use

```
I will see you at 10.04 A.M.
10.04 A.M. is the time for me.
```

From simple data, I want to build NER corpus for time tagging. It wants the time tag. I just add [time] before the start entity and [\time] after the end entity. like this;

```
I will see you at [TIME]10.04 A.M.[/TIME]
[TIME]10.04 A.M.[/TIME] is the time for me.
```

Next, build the NER Corpus

```python
data = """I will see you at [TIME]10.04 A.M.[/TIME]
[TIME]10.04 A.M.[/TIME] is the time for me."""

list_data = data.splitlines()

# Next EasyNERTag
from easynertag import Engine
build = Engine()

conll2002_list = []

for i in list_data:
    conll2002_list.append(build.text2conll2002(i))

print('\n'.join(conll2002_list))
```

output:

```
I       O
will    O
see     O
you     O
at      O
        O
10.04   B-TIME
A.M.    I-TIME

10.04   B-TIME
A.M.    I-TIME
        O
is      O
the     O
time    O
for     O
me.     O
```

You can custome the `word_tokenize` and the `pos_tag` in the Engine class.

```
Engine(
    word_tokenize = function for do word tokenize (default is white_space_split),
    pos_tag: function for do part of speech tagging
)
```

You can see the custome `pos_tag` in `tests/test_make_tag.py`.


## License

```
   Copyright 2022 Wannaphong Phatthiyaphaibun

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 ```
