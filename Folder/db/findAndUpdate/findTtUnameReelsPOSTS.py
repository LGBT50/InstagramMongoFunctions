from Folder.db.dbConnect import connect
from datetime import datetime as d
from datetime import datetime

#Finding user and updating posts with correct trimmed schema
def findAndUpdateUserPostsReels(db, user):
    #ttName = user[1]
    #user = user[0]

    #setting initial variables
    date = d.now()
    counter = 0
    reels_data = []
    userPosts = {}
    descSuperString = ''
    totalComments = 0
    totalLikes = 0
    totalViews = 0
    post_data = []
    reelsCount = 0
    postCount = 0
    totalReelsComments =0
    totalReelsLikes = 0
    totalReelsViews = 0
    

    #getting min number of posts to get average
    if len(user['edge_owner_to_timeline_media']['edges']) < 6:
        length = len(user['edge_owner_to_timeline_media']['edges'])
    else:
        length = 6
    
    #trim schema to take up less data
    for post in user['edge_owner_to_timeline_media']['edges']:
        post = post["node"]
        #print(post)
        timestamp = post['taken_at_timestamp']
        #print(timestamp)
        dt_object = datetime.fromtimestamp(timestamp)
        if post["__typename"] == "GraphVideo":
            if reelsCount < 7:
                totalReelsComments += post['edge_media_to_comment']['count']
                totalReelsLikes += post['edge_liked_by']['count']
                totalReelsViews += post['video_view_count']
                reelsCount +=1
            reels_data.append({
            'author':
            {'insta_uName':user['username']},

            'music':post['clips_music_attribution_info'],

            'statistics':
            {'views':post['video_view_count'],
            'comments':post['edge_media_to_comment']['count'],
            'likes':post['edge_liked_by']['count']},

            'general':
            {'id':post['id'],
            'desc':post['edge_media_to_caption']['edges'][0]['node']['text'],
            'date':dt_object
            }
            })
        else:
            if postCount < 7:
                totalComments += post['edge_media_to_comment']['count']
                totalLikes += post['edge_liked_by']['count']
                postCount +=1
            post_data.append({
            'author':
            {'insta_uName':user['username']},

            'statistics':
            {
            'comments':post['edge_media_to_comment']['count'],
            'likes':post['edge_liked_by']['count']},

            'general':
            {'id':post['id'],
            'desc':post['edge_media_to_caption']['edges'][0]['node']['text'],
            'date':dt_object}
            })


        descSuperString+=post['edge_media_to_caption']['edges'][0]['node']['text']

    #calculating averages for reels
    print("total reels posts:"+str(reelsCount))
    print("total posts:"+str(postCount))
    if (reelsCount>0):
        averageReelsComments = round(totalReelsComments/reelsCount)
        averageReelsLikes = round(totalReelsLikes/reelsCount)
        averageReelsViews = round(totalReelsViews/reelsCount)
    else:
        averageReelsComments = None
        averageReelsLikes = None
        averageReelsViews = None

        
    #calculating average for posts
    if (postCount>0):
        averageComments = round(totalComments/postCount)
        averageLikes = round(totalLikes/postCount)
    else:
        averageComments = None
        averageLikes = None

    #creating dictionaries to later add to the db
    userReelsPosts = {'reels_data':
    reels_data}

    #creating dictionary of averages and superString
    averagesReels = {
    'views':averageReelsViews,
    'likes':averageReelsLikes,
    'comments':averageReelsComments,
    }
    averagesPosts = {'likes':averageLikes,
    'comments':averageComments,
    'superString':descSuperString}
    #adding to dbs
    db.TokFl.find_one_and_update({'TikTok.user.ins_id': user["username"]}, {"$set":{"Instagram.reelsPosts":reels_data, "Instagram.feedPosts":post_data, 'Instagram.reelsAverages':averagesReels, 'Instagram.postsAverages':averagesPosts, "Instagram.lastPostUpdate":date.strftime("%Y-%m-%d %H:%M:%S")}})

    return user["username"]