from pymongo import MongoClient
import time

from Folder.db.dbConnect import connect

#aggregate the posts for each user in the db
def findIns_id():
    db = connect("TikScrape")
    cursor = db.TokFl.find({})
    cursor = db.TokFl.aggregate([{'$project':{ 'TikTok.userPosts.aweme_list':1, '_id':0 }}])
    ins_ids = []
    y = 0
    total = 0
    countries = []
    for document in cursor:
        try:
            for x in document["TikTok"]["userPosts"]["aweme_list"]:
                try:
                    if str(document['TikTok']['userPosts']['aweme_list'][0]['author']['region']) in countries:
                        pass
                    else:
                        countries.append(str(document['TikTok']['userPosts']['aweme_list'][0]['author']['region']))
                        print(countries)
                    if str(document['TikTok']['userPosts']['aweme_list'][0]['author']['region']) == 'US':
                        total +=1
                except: 
                    pass
                    #print(KeyError)
                    #print("not working")
                    # h
                break
        except:
            pass
            
        #print(document['TikTok']['userPosts']['aweme_list'][0]['author']['region'])

        #print(str(document['TikTok']['userPosts']['aweme_list']['0']['author']['region']))
        y+=1
    print(total)
    print(countries)
    print(x)
findIns_id()
    #return ins_ids