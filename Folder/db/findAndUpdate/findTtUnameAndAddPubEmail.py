from Folder.db.dbConnect import connect
from datetime import datetime as d


#Finding user and updating with correct trimmed schema
def findAndUpdateUser(db, user):
    #tT_userName = user[1]
    user = user
    date = d.now()
    #check if user exits
    if user["user"] == None:
        print("This no longer exists")

    else:
        #updating db if it does not exist
        try:
            db.TokFl.find_one_and_update({'TikTok.user.ins_id': user["username"]},
            {"$set":
            {"Instagram.user.uid":user["id"],
            "Instagram.user.public_email":user['public_email'],
            "Instagram.user.public_phone_number": user["public_phone_number"],
            "TikTok.lastEmailUserUpdate":date.strftime("%Y-%m-%d %H:%M:%S")}},upsert = True)
        except Exception as Exc:
            print("exceptions when updating user")
            print(Exc)
    return tT_userName
