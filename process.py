def gen_dictionary(data,key):
  dict = {}
  for x in data: #loops through array of dicts
    for i in x: #loops through dict keys
      if(key == i):
        v = x[i]
        dict[v] = 0
  return dict

def total_matches(lod,k,v):
  num = 0.0
  for x in lod:
    if(x.get(k) == v):
      num = num + 1.0
  return num

def total_matches_specific(lod,k,v,k2,v2):
  num = 0.0
  for x in lod:
    if(x.get(k) == v):
      if(x.get(k2) == v2):
        num = num + 1.0
  return num

def remove_min(data,min):
  dict = {}
  for x in data:
     if(data.get(x) > min):
        dict[x] = data.get(x)
  return dict