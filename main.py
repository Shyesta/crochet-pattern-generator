from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


from array import array
import os
from PIL import Image
import sys
import time

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

'''
Quickstart variables
These variables are shared by several examples
'''
# Images used for the examples: Describe an image, Categorize an image, Tag an image, 
# Detect faces, Detect adult or racy content, Detect the color scheme, 
# Detect domain-specific content, Detect image types, Detect objects
images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
remote_image_url = "https://images-ext-1.discordapp.net/external/Af8sIRhgdw28iYnuODvtb1gY8_xWJNV8ryKikDvZVMg/https/assets.voxcity.com/uploads/blog_images/Iconic%2520Landmarks%2520in%2520Rome_original.jpg?width=832&height=468"
'''
END - Quickstart variables
'''


'''
Tag an Image - remote
This example returns a tag (key word) for each thing in the image.
'''
# Call API with remote image and request specific visual features
visual_features = [VisualFeatureTypes.categories, VisualFeatureTypes.tags, VisualFeatureTypes.description, VisualFeatureTypes.objects]

tags_result_remote = computervision_client.analyze_image(remote_image_url, visual_features=visual_features)

# Print results of categories with confidence score
print("Categories and tags in the remote image:")
if not tags_result_remote.categories:
    print("No categories detected.")
else:
    for category in tags_result_remote.categories:
        print(f"Category '{category.name}' with confidence {category.score * 100:.2f}%")

# Print results of tags with confidence score
if not tags_result_remote.tags:
    print("No tags detected.")
else:
    for tag in tags_result_remote.tags:
        print(f"Tag '{tag.name}' with confidence {tag.confidence * 100:.2f}%")

# Print results of description with confidence score
if not tags_result_remote.description.captions:
    print("No description detected.")
else:
    for caption in tags_result_remote.description.captions:
        print(f"Description: '{caption.text}' with confidence {caption.confidence * 100:.2f}%")

# Print results of objects with confidence score
if not tags_result_remote.objects:
    print("No objects detected.")
else:
    print("Objects in the remote image:")
    for object in tags_result_remote.objects:
        print(f"Object '{object.object_property}' with confidence {object.confidence * 100:.2f}%")

print()
'''
END - Tag an Image - remote
'''
print("End of Computer Vision quickstart.")