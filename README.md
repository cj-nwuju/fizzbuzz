# FizzBuzz Web App

A small Flask web app that goes through the numbers 1 to 100 and sorts them into four groups:

- **fizzbuzz**: divisible by both 3 and 5
- **fizz**: divisible by 3 only
- **buzz**: divisible by 5 only
- **other**: not divisible by 3 or 5

## Requirements

- Python 3.8 or newer
- Flask (listed in `requirements.txt`)

## How to run

1. Clone or download this repository and open a terminal in its folder.
2. (Optional) Create a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # macOS / Linux
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Start the app:
   ```
   python app.py
   ```
5. Open the address shown in the terminal, usually http://127.0.0.1:5000

## Pages

| Address | What it shows |
|---|---|
| `/` | A welcome message |
| `/fizzbuzz` | The numbers 1 to 100 sorted into the four groups |

## Files

- `app.py`: the Flask application and the fizzbuzz logic
- `requirements.txt`: the Python packages the app needs

## What I learned

Routing in Flask, using loops and the modulo operator (`%`), building strings with f-strings, and returning HTML from a route.
