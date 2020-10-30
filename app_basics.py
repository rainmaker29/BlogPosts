from flask import Flask,render_template

app = Flask(__name__)
posts = [
    {
    'title':'Post 1',
    'content':'This is post1',
    'author':'Guddu Bhaiya'

    },
    {
    'title':'Post 2',
    'content':'This is post2',

    }

]



# Check how to pass strings
@app.route('/home/<string:name>')
def hello(name):
  return "<h1>Hello</h1> "+name

#Check rendering and inheriting templates
@app.route('/index')
def index():
    return render_template('index.html')

#Check GET
@app.route('/onlyget',methods=['GET'])
def onlyget():
    return "This can only get"

#Check POST
@app.route('/onlypost',methods=['POST'])
def onlypost():
    return "This can only post"

# Using jinja loops,conditionals
@app.route('/post')
def post():
    return render_template('posts.html',posts=posts)



#Main
if __name__ == '__main__':
  app.run(debug=True)
