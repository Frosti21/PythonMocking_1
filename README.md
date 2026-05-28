# PythonMocking

A simple temperature-based fan controller to illustrate unit testing using Mocks.

## Setup

Install the dependencies:

```bash
pip install -r requirements.txt
```

On Debian/Ubuntu (and other systems that enforce PEP 668), plain `pip install` is blocked. Add `--break-system-packages` to override it:

```bash
pip install -r requirements.txt --break-system-packages
```

## How to Run

```bash
python main.py
```


## How to Test

```bash
pytest . -v
```

