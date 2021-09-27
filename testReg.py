from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

#aggregate the posts for each user in the db

db = connect("TikScrape")
cursor = db.TokFl.find({})
#cursor = db.TokFl.find({ "TikTok.user.signature": { '$regex': "lgbt", '$options': "i" } })
cursor = db.TokFl.find({ "TikTok.averages.superString": { '$regex': "^lgbt", '$options': "im" } })

ins_ids = []
x = 0
#print(len(cursor))
print(len(list(cursor)))
for document in cursor:
    #print(document['TikTok']["user"]["unique_id"])
    ins_ids.append(document)
    x+=1
    #print(x)
print(len(ins_ids))
