from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

#aggregate the posts for each user in the db
def findIns_id():
    db = connect("TikScrape")
    cursor = db.TokFl.find({})
    cursor = db.TokFl.aggregate([{'$project':{ 'Instagram':1, '_id':0 }}])
    ins_ids = []
    x = 0
    for document in cursor:
        try:
            ins = document['Instagram']
            tempDict = {"ins_id":ins}
            if ins == "":
                NAN = 0
            else:
                ins_ids.append(tempDict)
                NAN = 0
        except KeyError: 
            print(KeyError)
            print("not working")
	        # handle the error 
        x+=1
    print(len(ins_ids))
findIns_id()
    #return ins_ids