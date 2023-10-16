from flask import Flask
app = Flask(__name__)
@app.route("/fizzbuzz")
def fizzbuzz ():
    nonfizzbuzz = []

    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0 :
            print(f"{i} fizzbuzz")
        elif i % 3 == 0 :
            print(f"{i} fizz")
        elif i % 5 == 0 :
            print(f"{i} buzz")
        else:
            nonfizzbuzz.append(i)

    return nonfizzbuzz