from flask import Flask,render_template, request
import datetime, json

app = Flask(__name__)
date = datetime.datetime.now()
h = date.hour
m = date.minute
s = date.second
time = date.strftime("%Y%m%d%H%M%S")

@app.route('/' , methods=['GET', 'POST'])
def index():
  post=None
  result = None
  filename = './Data/post.json'
  new_filename = './Data/'+time+".json"
  if request.method == 'POST':
    result = request.form
    secret = hash(result['secret'])
    if secret == hash('123'):

      # Read JSON file
      with open(filename) as fp:
        listObj = json.load(fp)

      post = result['post']

      listObj.append(post)
      with open(filename, 'w') as posts:
        json.dump(listObj, posts, 
                            indent=4,  
                            separators=(',',': '))
      # Verify updated list
      print(listObj)
      
      with open(new_filename, 'w') as json_file:
          json.dump(post, json_file, 
                              indent=4,  
                              separators=(',',': '))



    


  return render_template('index.html', result=result, post=post,  heure = h, minute = m, seconde = s)

@app.route("/blog")
def hello_blog():
    return "<p>Hello, Blog!</p>"