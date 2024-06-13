import bottle
import json
import process
import os.path
import data
import csv

@bottle.route("/")
def index():
  indexFile = bottle.static_file("index.html", root=".")
  return indexFile

@bottle.route("/script.js")
def jsFile():
  js = bottle.static_file("script.js", root=".")
  return js

@bottle.route('/ajax.js')
def ajaxFile():
   return bottle.static_file("ajax.js", root=".")
  
@bottle.route('/bar')
def getBar():
  data2 = {}
  var = process.gen_dictionary(file,"year") #generates dictionary with year keys and sets value to 0
  for x in var:
    var[x] = process.total_matches(file,"year",x) #changes key values to the matches in the data
  var = process.remove_min(var,20)
  for x in var:  
    data2["x"] = data2.get("x",[]) + [x] #checks if x already exists, if not returns a list and adds the key to the list
    data2["y"] = data2.get("y",[]) + [var[x]] #same as above except adds the key value instead
  data2["type"] = "bar"
  return json.dumps([data2])

@bottle.route("/pi")
def getPi():
  data2 = {}
  var = process.gen_dictionary(file,"day_of_week")
  for x in var:
    var[x] = process.total_matches(file,"day_of_week",x)
  for x in var:  
    data2["labels"] = data2.get("labels",[]) + [x]
    data2["values"] = data2.get("values",[]) + [var[x]]
  data2["type"] = "pie"
  return json.dumps([data2])

@bottle.post("/line")
def getLine():
  post = bottle.request.body.read().decode()
  data2 = {}
  var = process.gen_dictionary(file,"year")
  for x in var:
    var[x] = process.total_matches_specific(file,"year",x,"hour_of_day", post)
  var = process.remove_min(var,20)
  var = sorted(var.items())
  placeholder = {}
  for x,y in var:
    placeholder[x] = y
  for x in placeholder:  
    data2["x"] = data2.get("x",[]) + [x]
    data2["y"] = data2.get("y",[]) + [placeholder[x]]
  data2["type"] = "lines"
  return json.dumps([data2])
  
  

def startup():
  csv_file = 'saved_data.csv'
  if not os.path.isfile(csv_file):
    url = 'https://data.buffalony.gov/resource/d6g9-xbgu.json?$limit=50000'
    info = data.json_loader(url)
    data.fix_data(info,"incident_datetime")
    heads =['year','month','hour_of_day','incident_type_primary','day_of_week']
    data.save_data(info, heads, csv_file)
startup()
file = data.load_data("saved_data.csv") #turns csv file to list of dictionaries
bottle.run(host="0.0.0.0", port=8080)