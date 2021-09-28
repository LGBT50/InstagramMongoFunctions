from Folder.db.dbConnect import connect
from datetime import datetime as d


#Finding user and updating with correct trimmed schema
def findAndUpdateUser(db, user):
    #tT_userName = user[1]
    #user = user[0]
    date = d.now()
    #check if user exits
    #if user["user"] == None:
      #  print("This no longer exists")

        #updating db if it does not exist
    try:
        db.TokFl.find_one_and_update({'TikTok.user.ins_id': user["username"]},
        {"$set":
        {"NCAA.sport":"basketball",
        "NCAA.division":1,
            "Instagram.user.uid":user["id"],
        "Instagram.user.follower_count":user["edge_followed_by"]['count'],
        "Instagram.user.following_count":user["edge_follow"]['count'],
        "Instagram.user.posts":user["edge_owner_to_timeline_media"]['count'],
        "Instagram.user.bio":user["biography"],
        "Instagram.user.countryBlock":user["country_block"],
        "Instagram.user.url":user["external_url"],
        "Instagram.user.business_email":user["business_email"],
        "Instagram.user.category_name":user["category_name"],
        "Instagram.user.is_verified":user["is_verified"],
        "Instagram.user.professionalAcct":user["is_professional_account"],
        "Instagram.user.pronouns":user["pronouns"],
        "TikTok.lastUserUpdate":date.strftime("%Y-%m-%d %H:%M:%S")}},upsert = True)
    except Exception as Exc:
        print("exceptions when updating user")
        print(Exc)
    return user['username']
