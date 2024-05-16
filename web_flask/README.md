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

@app.route("/hbnb")
def hbnb_page():
    return "HBNB"

```

4. run the app to listen on 0.0.0.0 at port 5000
```
if __name__ == "__main__:
    app.run(host="0.0.0.0", port=5000)
```

## escaping
this is done to avoid injection
import escape function
use the escape to sanitize the input from users
```
from markupsafe import escape
@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    display “C ” followed by the value of the text variable
    (replace underscore _ symbols with a space)
    """
    txt = text.replace('_', ' ')
    return f"C {escape(txt)}"
```