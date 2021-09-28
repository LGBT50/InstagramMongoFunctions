from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

#aggregate the posts for each user in the db
db = connect("TikScrape")
cursor = db.TokFl.find({})
cursor = db.TokFl.aggregate([{'$project':{"TikTok.user.signature":1,"TikTok.averages.superString":1,'_id':0, "TikTok.user.unique_id":1}}])
ins_ids = []
x = 0
for document in cursor:
    try:
        if "@gmurray11" in str(document["TikTok"]["user"]["signature"].lower()):
            ins_ids.append(document["TikTok"]["user"]["unique_id"])
        #print(len(ins_ids))
    except:
        pass
print(len(ins_ids))