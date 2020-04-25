# fakespy

A CLI tool to retrieve a message (command) from FakeSpy C2.

## Requirements

- Python 3 (tested with Python 3.8)
- [Poetry](https://python-poetry.org/)

## Install

```bash
git clone https://github.com/ninoseki/fakespy
cd fakespy
poetry install --no-root
```

## Usage

```bash
$ python cli.py --help
NAME
    cli.py

SYNOPSIS
    cli.py COMMAND C2 <flags>

POSITIONAL ARGUMENTS
    COMMAND
    C2

FLAGS
    --mobile_number=MOBILE_NUMBER

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS
```

- Supported commands:
  - GetMessage
  - [GetMessage2](https://github.com/ninoseki/fakespy/wiki#getmessage2)(`sendSms`)
  - [GetMoreMessage](https://github.com/ninoseki/fakespy/wiki#getmoremessage)(`sendAll`)
  - [GetMoreConMessge](https://github.com/ninoseki/fakespy/wiki#getmoreconmessage)(`sendCon`)

```bash
python cli.py GetMessage2 foo.bar.com
```
