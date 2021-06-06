#! python3
# mongotest.py - testing mongo examples from chapter 3 of
# Data Visualization with Python and Javascript

from mongo_utils import get_mongo_database, mongo_coll_to_dicts

DB_NOBEL_PRIZE = 'nobel_prize'
COLL_WINNERS = 'winners'



nobel_winners = [
{'category': 'Physics',
 'name': 'Albert Einstein',
 'nationality': 'Swiss',
 'sex': 'male',
 'year': 1921},
{'category': 'Physics',
 'name': 'Paul Dirac',
 'nationality': 'British',
 'sex': 'male',
 'year': 1933},
{'category': 'Chemistry',
 'name': 'Marie Curie',
 'nationality': 'Polish',
 'sex': 'female',
 'year': 1911}
]

db = get_mongo_database(DB_NOBEL_PRIZE)
coll = db[COLL_WINNERS]

coll.insert(nobel_winners)
res = coll.find({'category':'Chemistry'})
print(res)


