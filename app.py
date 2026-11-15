from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>This is the fizzbuzz website. Add /fizzbuzz to the address to see the results.</p>"


@app.route("/fizzbuzz")
def fizzbuzz():
    ordinary = []
    fizz = []
    buzz = []
    fizzbuzz_list = []

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz_list.append(f"{i} fizzbuzz")
        elif i % 3 == 0:
            fizz.append(f"{i} fizz")
        elif i % 5 == 0:
            buzz.append(f"{i} buzz")
        else:
            ordinary.append(str(i))

    return (
        "<h1>FizzBuzz 1 to 100</h1>"
        f"<h2>Fizzbuzz (divisible by 3 and 5)</h2><p>{', '.join(fizzbuzz_list)}</p>"
        f"<h2>Fizz (divisible by 3)</h2><p>{', '.join(fizz)}</p>"
        f"<h2>Buzz (divisible by 5)</h2><p>{', '.join(buzz)}</p>"
        f"<h2>Other numbers</h2><p>{', '.join(ordinary)}</p>"
    )


if __name__ == "__main__":
    app.run(debug=True)
