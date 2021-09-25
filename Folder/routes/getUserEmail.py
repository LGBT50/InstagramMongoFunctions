from Folder.db.Finders.dbFindInstagramUID import findIns_uids
import requests 
from pymongo import MongoClient
import time
import concurrent.futures
from decouple import config

from Folder.db.Finders.dbFindUserNames import findUserNames

def addInsUid():
    ins_ids = findIns_uids()

    url = config("API_URL")+"account-info-full"

    #querystring = {"userid":"53111488"}

    headers = {
    'x-rapidapi-host': config("API_HOST"),
    'x-rapidapi-key': config("API_KEY")
    }
    querystrings = []
    for x in ins_ids:
        querystrings.append(x)


    def load_url(querystring):
        querystring = querystring["uid"]
        response = requests.request("GET", url, headers=headers, params={"userid":querystring})
        while response.status_code == 429:
            print("API server is getting too many requests")
            time.sleep(10)
            response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json(), querystring["tt_user"]

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_url = (executor.submit(load_url, querystring)for querystring in querystrings)
        time1 = time.time()
        time4 = time.time()
        for future in concurrent.futures.as_completed(future_to_url):
            try:
                data = future.result()
                out.append(data)
            except Exception as exc:
                data1 = str(type(exc))
                exceptions.append(data1)
                print(exc)
            finally:
                time2 = time.time()
                if len(out) %10 ==0:
                    if (time2-time4) < 3.3:
                        print("TOO FAST")
                        time.sleep(1.5)
                    time4 = time.time()
                    
                print(len(out))
                print(f' reqest Took {time2-time1:.2f} s')
    print(f' average request took {time2-time1/len(out):.2f} s')
    print(f'Took {time2-time1:.2f} s')
    print(len(out))
    return out




