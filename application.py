from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS
import time

from Folder.routes.getUserId import addInsId
from Folder.db.Finders.dbFindInstagram import findIns_id
from Folder.ParentFunctions.AddNewUsers.addUserByTTName import addNewUsers
from addNCAA import getNCAABBall


#initializing app, api, and cors
application = Flask(__name__)
api = Api(application)
CORS(application)

#setting reqparser
scrape_post_args = reqparse.RequestParser()
scrape_post_args.add_argument("tiktok_userNames", action='append', help="Please send an array sec_uids to update...")
scrape_post_args.add_argument("insta_userNames", action='append', help="Please send an array of usernames to add to the DB...")


#definiing endpoints and actions
class Home(Resource):
    def get(self):
        return "Hello World"


#defining update function endpoints

class addUserId(Resource):
    def post(self):
        addInsUid()
        return "Success"
    def get(self):
        return "Nothing to GET"
class updateTikTokUsers(Resource):
    def post(self):
        userNames = findIns_id()
        count = addNewUsers(userNames)
        
        print("application function--- updated Docs shows:"+str(count))
        print("Instagrams Scraped and Added to the db")
        return "Success"
    def get(self):
        return "Nothing to GET"
class AddNCAABaskeBall(Resource):
    def post(self):
        userNames = getNCAABBall()
        count = addNewUsers(userNames)
        
        print("application function--- updated Docs shows:"+str(count))
        print("Instagrams Scraped and Added to the db")
        return "Success"
    def get(self):
        return "Nothing to GET"


api.add_resource(updateTikTokUsers, "/updateTikTokUsers")




#Home
api.add_resource(Home, "/")

if __name__ == "__main__":
   application.run()

