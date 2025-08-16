from flask import Flask, request

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
  title = "Are You a Robot??"
  page = ""
  f = open("template/areRobot.html","r")
  page = f.read()
  f.close()
  page = page.replace("{title}", title)
  return page

@app.route("/check", methods=["POST"])
def check():
  form = request.form
  if form ['metal'] == "yes":
    return "You Are A Robot!"
  elif "lots" in form['oilDrink'].lower() or "frequently" in form['oilDrink'].lower() or "oftn" in form['oilDrink'].lower() or "always" in form['oilDrink'].lower():
    return "You Are A Robot!"
  elif form['film'] == "irobot" or form['film'] == "robots" or form['film'] == "robocop":
    return "You Are A Robot!"
  else:
    return "You are a human (I think)"
  
    
  
  



app.run(host='0.0.0.0', port=81)
