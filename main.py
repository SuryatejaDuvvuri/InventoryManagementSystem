from google.cloud import storage
import firebase_admin
from firebase_admin import credentials, db
from PIL import Image
import json
import publisher
from firebase_admin import db

cred1 = credentials.Certificate("uplifted-env-424901-t2-firebase-adminsdk-1n3uy-07457c1d15.json")
firebase_admin.initialize_app(cred1, {'databaseURL': "https://uplifted-env-424901-t2-default-rtdb.firebaseio.com/"})
ref = db.reference('Inventory') 


# ref.update({
#     'Ragu': {
#         'name': 'Ragu',
#         'Count': 10,
#         'image': 'Ragu.jpeg',
#         'Aisle': '1',
#         'Missing': False,
#         'Misplaced': False
#     }
# })

#adding item
# data = {
#     'name': 'Kellogs Cereal Box',
#         'Aisle': 5,
#         'Shelf': '3',
#         'Misplaced': False,
#          'InStock': True,
# }      
# ref.child('Kellogs Cereal Box').set(data) 


storage_client = storage.Client()  # No additional arguments needed

# # Get a reference to a bucket
bucket_name = 'cs131-tests'
bucket = storage_client.bucket(bucket_name)

# List blobs (files) in the bucket
    

# # Downloading and uploading images of grocery items
# blob_name = 'Ragu.jpeg'
# # blob = bucket.blob(blob_name)
# # blob.download_to_filename('Ragu.jpeg')



# blob_name = "Ragu.jpeg"
# blob = bucket.blob(blob_name)
# blob.upload_from_filename(blob_name)

# Updating inventory data
# for item in ref.get():
#    val = ref.child(item).child('Count').get()
#    if val == 0:
#        print("Item is out of stock")
#    else:
#        ref.child(item).update({'Count': val - 1}) 
#        print('Count: ', ref.child(item).child('Count').get())

def add_stock(item_name):
    count = ref.child(item_name).child('InStock').get()
    ref.child(item_name).update({'InStock':not count})
    return ref.child(item_name).child('InStock').get()

for item in ref.get():
    val = add_stock(item)
    publisher.send_message(item, ref.child(item).child('Aisle').get(), ref.child(item).child('Shelf').get(), val)