# fakespy

A CLI tool to retrieve a message (command) from FakeSpy C2 and analyze a FakeSpy apk.

## Requirements

- Python 3 (tested with Python 3.8)
- [Poetry](https://python-poetry.org/)

## Install

```bash
git clone https://github.com/ninoseki/fakespy
cd fakespy
poetry install
```

## Usage

```bash
$ python cli.py
Usage: cli.py [OPTIONS] COMMAND [ARGS]...

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.

  --help                          Show this message and exit.

Commands:
  analyze-apk
  send-command
```

### analyze-apk

This command analyzes a given APK and extracts C2 urls.

```bash
$ python cli.py analyze-apk /tmp/foo.apk
{
  "c2": [
    "http://xxx.club/",
    "http://yyy.club/"
  ]
}
```

### send-command

This command sends a request to a C2.

- Supported commands:
  - GetMessage
  - [GetMessage2](https://github.com/ninoseki/fakespy/wiki#getmessage2)(`sendSms`)
  - [GetMoreMessage](https://github.com/ninoseki/fakespy/wiki#getmoremessage)(`sendAll`)
  - [GetMoreConMessge](https://github.com/ninoseki/fakespy/wiki#getmoreconmessage)(`sendCon`)

```bash
python cli.py send-co0mmand GetMessage2 foo.bar.com
```
