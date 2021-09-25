from Folder.db.findAndUpdate.findTtUnameAndUpdateUid import findAndUpdateUser
from Folder.db.findAndUpdate.findTtUnameReelsPOSTS import findAndUpdateUserPostsReels

def UpdUserAndReels(db, user):
    print("adding..."+str(user['username']))
    findAndUpdateUser(db, user)
    print("UserDONE")
    findAndUpdateUserPostsReels(db, user)
    print("postsDONE")
