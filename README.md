# Sauce Demo Login Tests

Automated login test suite for [saucedemo.com](https://www.saucedemo.com) 
built with Playwright and pytest.

![Tests](https://github.com/ElanLeonard/sauce-demo-tests/actions/workflows/tests.yml/badge.svg)

## What This Tests
- Valid login
- Wrong password
- Locked out user
- Empty fields
- SQL injection attempt
- Inventory page loads after login

## Project Structure
```
pages/         # Page Object Model
tests/         # Test files
conftest.py    # pytest fixtures
```

## How To Run Locally
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
pytest tests/ -v
```
```


