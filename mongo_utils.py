#! python3
# mongo_utils.py is a utility to access a mongo database
# from chapter 3 of Data Visualization with Python and Javascript

from pymongo import MongoClient

def get_mongo_database(db_name, host='localhost', port=27017, username=None, password=None):
    """ Get named database from MongoDB with or without authentication """
    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s/%s'%(username, password, host, db_name)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)

    return conn[db_name]

def mongo_coll_to_dicts(dbname='test', collname='test', query={}, del_id=True, **kw):
    """ turn a MongoDB collection into a dictionary """
    db = get_mongo_database(dbname, **kw)
    res = list(db[collname].find(query))
    if del_id:
        for r in res:
            r.pop('_id')

    return res


