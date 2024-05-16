0x04. AirBnB clone - Web framework

## Task 0
1. import the Flask Class from flask
`from flask import Flask`
2. create an instatnce of that class, and pass the name of the module to it.

`app = Flask(__name__)`
3. create routesusing the decorator @route
```
@app.route("/")
def index():
    return "Hello Wolrd"
```
4. run the app to listen on 0.0.0.0 at port 5000
```
if __name__ == "__main__:
    app.run(host="0.0.0.0", port=5000)
```
