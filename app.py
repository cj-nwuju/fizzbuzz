from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>This is the fizzbuzz website, add (/fizzbuzz) t</p>"

@app.route("/fizzbuzz")
def fizzbuzz ():
    nonfizzbuzz = []
    fizz = []
    buzz = []
    fizzbuzz = []

    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0 :
            print(f"{i} fizzbuzz")
            a = f("{i} fizzbuzz")
            fizzbuzz.append(a)
        elif i % 3 == 0 :
            print(f"{i} fizz")
            b = f("{i} fizz")
            fizz.append(b)
        elif i % 5 == 0 :
            print(f"{i} buzz")
            c = f("{i} buzz")
            buzz.append(c)
        else:
            nonfizzbuzz.append(i)

    return (nonfizzbuzz, fizz, buzz, fizzbuzz,)