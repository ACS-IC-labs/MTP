# MTP

Keys in One-time pad encryption (OTP) should only be used once, when they get reused we can do a Many-time pad attack.

MTP Interactive uses automated cryptanalysis to present a partial decryption which can be solved interactively.

## Install

Python 3.11+ required

```
pip3 install .
```

## Usage

Start a new decryption session:

```
mtp ciphertext.txt
```

Resume a previous session from a saved result file:

```
mtp ciphertext.txt --load result.json
```

Specify a custom output filename:

```
mtp ciphertext.txt -o custom_output.json
```

[![asciicast](https://asciinema.org/a/204705.png)](https://asciinema.org/a/204705)

### Instructions

Cursor movement is similar to Sublime Text:
 - Left, Right, Up and Down for simple movement
 - Home, End, Page Up and Page Down for larger movement
 - Left Click for jumping to mouse cursor

Letters can be entered using the keyboard any time.

The menu can be opened with the escape key. The "Export" button in the menu
will write the JSON state of the decryption to a file named 'result.json' by default. Use the -o flag to specify the desired filename for export.

You can resume a previous session at any time by using the `-l` or `--load` flag with the exported result file path.

You can exit the program cleanly using the "Quit" menu button.

Window resizing and text size changes are supported.

## Development

Use a Python +3.11 virtual environment to develop on this project

```
virtualenv venv -p python3.11
source ./venv/bin/activate
pip install -e .
```

Pull Requests and Issues welcome!
