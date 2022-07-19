from textwrap import indent
from tinydb import TinyDB, Query, where
db = TinyDB('data.json', indent=4)

#db.insert ({"name": "Eki", "score": 0})

db.update({"score": 20}, where('name') == 'Eki')