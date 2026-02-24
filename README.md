# flake8-no-chained-assignments

[![Tests](https://github.com/mrsndmn/flake8-no-model-forward-call/actions/workflows/tests.yml/badge.svg)](https://github.com/mrsndmn/flake8-no-model-forward-call/actions/workflows/tests.yml)
[![PyPI version](https://img.shields.io/pypi/v/flake8-no-chained-assignments.svg)](https://pypi.org/project/flake8-no-chained-assignments/)
[![Python versions](https://img.shields.io/pypi/pyversions/flake8-no-chained-assignments.svg)](https://pypi.org/project/flake8-no-chained-assignments/)
[![License](https://img.shields.io/pypi/l/flake8-no-chained-assignments.svg)](https://github.com/mrsndmn/flake8-no-model-forward-call/blob/main/LICENSE)

A [flake8](https://flake8.pycqa.org/) plugin that prohibits chained assignments.

Chained assignments (`a = b = value`) can obscure intent and lead to subtle bugs when mutable objects are involved. This plugin makes them a lint error, encouraging explicit, readable assignments instead.

## Error codes

| Code   | Description                          |
|--------|--------------------------------------|
| NCA001 | Chained assignments are prohibited   |

## Example

```python
# Bad — triggers NCA001
a = b = 0
x = y = z = []

# Good
a = 0
b = 0
```

## Installation

```bash
pip install flake8-no-chained-assignments
```

Or add it to your project's dev dependencies:

```bash
pip install -e ".[dev]"
```

## Usage

Once installed, flake8 picks up the plugin automatically:

```bash
flake8 your_code.py
```

Example output:

```
your_code.py:3:1: NCA001 Chained assignments are prohibited
```

### Configuration

You can ignore the rule per-line with the standard flake8 mechanism:

```python
a = b = 0  # noqa: NCA001
```

Or disable it project-wide in `setup.cfg` / `.flake8`:

```ini
[flake8]
extend-ignore = NCA001
```

## Development

```bash
git clone https://github.com/mrsndmn/flake8-no-model-forward-call
cd flake8-no-model-forward-call
pip install -e ".[dev]"
pytest tests/ -v
```

## License

[Apache-2.0](LICENSE)
