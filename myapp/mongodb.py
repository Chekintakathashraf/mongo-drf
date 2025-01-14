
import pymongo
from django.conf import settings

# Connect to MongoDB
client = pymongo.MongoClient(settings.MONGO_DB_SETTINGS['HOST'], settings.MONGO_DB_SETTINGS['PORT'])
db = client[settings.MONGO_DB_SETTINGS['DB_NAME']]

class UserActivity:
    def __init__(self):
        self.collection = db['user_activity']
        # Create index for efficient queries
        self.collection.create_index([('user_id', pymongo.ASCENDING), ('timestamp', pymongo.DESCENDING)])

    def log_activity(self, user_id, action):
        activity = {
            'user_id': user_id,
            'action': action,
            'timestamp': pymongo.datetime.datetime.utcnow()
        }
        self.collection.insert_one(activity)
