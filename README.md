# UwU++

Automata Project for 3rd Year

## Get Started

1. Create a virtual environment `python -m venv .env`
2. Activate environment For CMD `./.env/Scripts/activate.bat` For bash `source ./.env/Scripts/activate`
3. Install dependencies using pip `python -m pip install -r requirements.txt`

## Unit Testing

1. For unit testing, we'll be using `pytest`
2. To create a test file, simply follow these file formats: `test_*.py` or `*_test.py`
3. For more information, please refer to the official [Pytest documentation](https://docs.pytest.org/en/7.1.x/getting-started.html#)

## UwU IDE Package Manager

1. To install | uninstall packages from `requirements.txt`

```bash
python -m run install
python -m run uninstall
```

2. To install | uninstall individual packages

```bash
python -m run install < package name >
python -m run uninstall < package name >
```

3. To run all tests `python -m run test`
4. To run a specific test

```bash
python -m run test test_*
python -m run test *_test
```

5. To build UwU IDE `python -m run build`
