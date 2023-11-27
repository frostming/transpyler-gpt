# transpyler-gpt

A GPT-powered Python transpiler that makes your Python code run on older versions

Runs on Python 3.7+

## Installation

```bash
pip install git+https://github.com/frostming/transpyler-gpt.git
```

## Usage

Set `OPENAI_API_KEY` environment variable to your OpenAI API key.

Given a script `test.py` with the following Python 3.10+ code:


```python
def print_point(p: tuple[int, int]) -> None:
    match p:
        case (0, 0):
            print("origin")
        case (x, 0):
            print(f"point at x-axis {x}")
        case (0, y):
            print(f"point at y-axis {y}")
        case (x, y) if x == y:
            print(f"point at diagonal {x}")
        case (x, y):
            print(f"point at {x}, {y}")


print_point((0, 0))
print_point((10, 0))
print_point((0, 10))
print_point((10, 10))
print_point((10, 20))
```

Run `transpyle --target 3.7 test.py`, it prints:

```python
def print_point(p):
    if p == (0, 0):
        print("origin")
    elif p[1] == 0:
        print(f"point at x-axis {p[0]}")
    elif p[0] == 0:
        print(f"point at y-axis {p[1]}")
    elif p[0] == p[1]:
        print(f"point at diagonal {p[0]}")
    else:
        print(f"point at {p[0]}, {p[1]}")


print_point((0, 0))
print_point((10, 0))
print_point((0, 10))
print_point((10, 10))
print_point((10, 20))
```

which can be run on Python 3.7.


You can even make a script runnable on old Python versions without an explicit transpiling step. Just add the encoding line to the top of your script:

```python
# -*- coding: transpyler -*-
...
```

And you are able to run with older version directly:

```bash
python3.7 test.py
```

> **Note**
> You need to install `transpyler-gpt` into the target Python. For example, if you want to run the transpiled code on Python 3.7, you need to install `transpyler-gpt` into Python 3.7.


## License

MIT.
