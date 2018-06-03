import json
import re
import pymongo
from pymongo import MongoClient
import os
client = MongoClient('localhost', 27017)
db = client['mydb']

ls = ['HabrSpider']

for name in ls:
    try:
        os.remove(name+'.json')
    except OSError as err:
        print("OS error: {0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
    else:
        print(name + " deleted")
        
    
    os.system('scrapy crawl {0} -o {0}.json'.format(name))
    print(name + ".json downloaded")
    try:
        myfile = open(name+'.json',mode='r')
    except:
        print(name + "Unexpected error:", sys.exc_info()[0])
        raise
    else:
        json_data = json.load(myfile)
        db[name].drop()
        result = db[name].insert_many(json_data)
        myfile.close()
        print(name + " successfully write to database")

