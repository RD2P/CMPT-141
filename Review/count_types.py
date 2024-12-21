db = {
  "pika": {
    "name": "pikachu",
    "type": "electric",
    "level": 77
  },
  "bulba": {
    "name": "bulba",    
    "type": "grass",
    "level": 88
  },
  "veno": {
    "name": "veno",    
    "type": "grass",
    "level": 99
  },
}

def count_types(db):
  return len(set(x["type"] for x in db.values()))

print(count_types(db))