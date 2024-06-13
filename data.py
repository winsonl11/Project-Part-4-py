import csv
import json
import urllib.request

def list_dic_gen(stringList,listList):
  list = []
  for x in listList:
    index = 0
    dict = {}
    for y in stringList:
      dict[y] = x[index]
      index = index + 1
    list.append(dict)
  return list

def read_values(file):
  list = []
  with open(file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
      list.append(row)
  return list

def list_gen(dictList, stringList):
  returned = []
  for x in dictList:
    arr = []
    for y in stringList:
      arr.append(x[y])
    returned.append(arr)
  return returned

def write_values(listList, file):
  with open(file, "a") as f:
    writer = csv.writer(f)
    for x in listList:
      writer.writerow(x)

def split_date(date):
  arr = []
  arr.append(int(date[0:4]))
  arr.append(int(date[5:7]))
  return arr

def fix_data(lod,k):
  for x in lod:
    val = split_date(x[k])
    x["year"] = val[0]
    x["month"] = val[1]
  return lod

def json_loader(url):
  request = urllib.request.urlopen(url)
  content = request.read().decode()
  return json.loads(content)

def make_values_numeric(listKeys,dict):
  for x in listKeys:
    dict[x] = float(dict[x])
  return dict

def save_data(lod, keys, fileName):
  with open(fileName, "a") as f:
    writer = csv.writer(f)
    writer.writerow(keys)
    for x in lod:
      arr = []
      for y in keys:
        arr.append(x[y])
      writer.writerow(arr)

def load_data(file):
  arr = []
  with open(file,"r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for x in reader:
      dict = {}
      for y in range(len(header)):
        dict[header[y]] = x[y]
      arr.append(dict)
  return arr
