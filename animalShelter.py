from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""
    # Initialize Function
    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections
        # This is hard-wired to use the aac database, the
        # animals collection and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # Connection Variables
        #
        #USER = 'aacuser'
        #PASS = 'Password123'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30876
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
    # Create Function   
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)
            if insert != 0:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to create, no data has been passed.")
    # Read Function 
    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria)
        else:
            data = self.database.animals.find({})
        return data
    # Update Function
    def update(self, initial, change):
        if initial is not None:
            if self.database.animals.count_documents(initial, limit = 1) != 0:
                update_result = self.database.animals.update_many(initial, {"$set" : change})
                result = update_result.raw_result
            else:
                result = "No document found"
            return result
        else:
            raise Exception("Nothing to update, no data has been passed.")
    # Delete Function
    def delete(self, remove):
        if remove is not None:
            if self.database.animals.count_documents(remove, limit = 1) != 0:
                delete_result = self.database.animals.delete_many(remove)
                result = delete_result.raw_result
            else:
                result = "No document found"
            return result
        else:
            raise Exception("Nothing to delte, no data has been passed.")
    