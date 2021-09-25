from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

#aggregate the posts for each user in the db
def findIns_uids():
    db = connect("TikScrape")
    cursor = db.TokFl.find({})
    cursor = db.TokFl.aggregate([{'$project':{ 'Instagram.user.uid':1, '_id':0, "TikTok.user.unique_id":1}}])
    ins_uids = []
    x = 0
    for document in cursor:
        try:
            ins = document['Instagram']['user']['uid']
            tt_user = document['TikTok']['user']['unique_id']
            tempDict = {"tt_user":tt_user,"uid":ins}
        except KeyError: 
            print(KeyError)
            print("not working")
	        # handle the error 
        x+=1
    return ins_uids