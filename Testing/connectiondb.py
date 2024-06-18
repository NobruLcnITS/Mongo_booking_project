from pymongo import MongoClient

uri = "mongodb+srv://Brunolcn:2ZfdeTz851ld7e6t@atlascluster.hz5otjy.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"

client = MongoClient(uri)

db = client['sample_mflix']

collection = db['movies']
print(collection)
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)
