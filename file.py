
"""Detects text in the file located in Google Cloud Storage or on the Web."""
from google.cloud import vision
import main

client = vision.ImageAnnotatorClient()
image = vision.Image()
image.source.image_uri = "gs://cs131-tests/Ragu.jpeg"

response = client.text_detection(image=image)
texts = response.text_annotations
print("Texts:")

for text in texts:
    if(text.description.lower() == "ragu"):
        print("Found Ragu")
        main.add_stock(text.description)
    print(f'\n"{text.description}"')

    vertices = [
        f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
    ]

    # print("bounds: {}".format(",".join(vertices)))

if response.error.message:
    raise Exception(
        "{}\nFor more info on error messages, check: "
        "https://cloud.google.com/apis/design/errors".format(response.error.message)
    )
