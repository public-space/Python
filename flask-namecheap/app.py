from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
<div class='hello'>
<em>Hello, World!</em><br>
<strong>This is a Python Flask app.</strong>
<br><br>
After the URL, try adding a <em>name or word</em> in the address bar and refreshing the page!
<br><br>
</div>

This works great on my local machine<br> 
but as a HTTP GET request, it doesn't work on Namecheap's servers.<br>
Or am I just a complete noob?<br>
<style> 
body {
    font-family: Arial, sans-serif;
    background-color: #F0F0F0;
}
</style>
'''

@app.route("/<string:name>/")
def say_hello(name):
    return f"""Hello, {name}!"""

if __name__ == '__main__':
    app.run(debug=True)