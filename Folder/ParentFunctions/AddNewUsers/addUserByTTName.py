from pymongo import MongoClient
import pymongo
import sys, os
import time
import concurrent.futures
from Folder.db.dbConnect import connect
from datetime import datetime as d
from Folder.routes.getUserId import addInsId
from Folder.db.helpers.updateUserandPosts import UpdUserAndReels


#adds new users by user id
def addNewUsers(user_ids):
    db = connect('TikScrape')
    test = []
    count1 = 0
    for x in user_ids:
        count1 +=1
        if count1 < 11434:
            pass
        else:
            test.append(x)


    counter = 0
    z = 0
    userCount = len(test)
    print("number of users from DB is:"+str(len(user_ids)))
    #gets documents from how many we want to scrape
    subset = []
    i = 0
    for x in test:
        counter+=1
        subset.append(x)
        print(x)
        print("subset is: "+str(subset))
        if i % 200 == 0 or userCount < 200:
            documents = addInsId(subset)
            print("Length of documents after API is:"+str(len(documents)))
            print(str(counter)+" have been updated so far!")
            with concurrent.futures.ThreadPoolExecutor(max_workers=500) as executor:
                future_to_url = (executor.submit(UpdUserAndReels, db, document)for document in documents)
                time1 = time.time()
                for future in concurrent.futures.as_completed(future_to_url):
                    try:
                        data = future.result()
                        #print(data)
                    except Exception as exc:
                        print("Exception is:"+str(exc))
                    finally:
                        NAN = 0
                        

                time2 = time.time()
            print(f'Took {time2-time1:.2f} s')
            subset = []
        
        userCount -=1
        i+=1

    print("bulk insert users complete...")
    return counter
    


 