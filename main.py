from google.cloud import storage
import firebase_admin
from firebase_admin import credentials, db
from PIL import Image
import json

cred1 = credentials.Certificate("uplifted-env-424901-t2-firebase-adminsdk-1n3uy-07457c1d15.json")
firebase_admin.initialize_app(cred1, {'databaseURL': "https://uplifted-env-424901-t2-default-rtdb.firebaseio.com/"})
ref = db.reference('Inventory') 


ref.update({
    'Ragu': {
        'name': 'Ragu',
        'quantity': 10,
        'image': 'Ragu.jpeg',
        'Aisle': '1',
        'Missing': False,
        'Misplaced': False
    }
})
storage_client = storage.Client()  # No additional arguments needed

# # Get a reference to a bucket
bucket_name = 'cs131-tests'
bucket = storage_client.bucket(bucket_name)

# List blobs (files) in the bucket
for blob in bucket.list_blobs():
    ref.child(blob).child('image').get()
    

# # Download a blob
# blob_name = 'Ragu.jpeg'
# # blob = bucket.blob(blob_name)
# # blob.download_to_filename('Ragu.jpeg')



blob_name = "Ragu.jpeg"
blob = bucket.blob(blob_name)
blob.upload_from_filename(blob_name)




