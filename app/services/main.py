from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

from groq import Groq
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

image_client = ImageAnalysisClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(subscription_key)
)

def analyze_image_and_generate_pattern(image_url):
    # Get a caption for the image. This will be a synchronously (blocking) call.
    result = image_client.analyze_from_url(
        image_url=image_url,
        visual_features=[VisualFeatures.TAGS, VisualFeatures.OBJECTS],
        gender_neutral_caption=True,  # Optional (default is False)
    )

    # Prepare the tags array
    tags_array = []
    if result.tags is not None:
        for tag in result.tags.list:
            tags_array.append({"name": tag.name, "confidence": tag.confidence})

    # Prepare the objects array if needed (optional, for more details)
    objects_array = []
    if result.objects is not None:
        for obj in result.objects.list:
            objects_array.append({
                "tag": obj.tags[0].name,
                "bounding_box": obj.bounding_box,
                "confidence": obj.tags[0].confidence
            })

    # Initialize the Groq client
    groq_client = Groq(api_key=os.environ['GROQ_API_KEY'])

    # Send the tags to the Groq API
    chat_completion = groq_client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"""You are a helpful assistant whose goal is to assist the user in recreating a crochet pattern based on image tags. 
                You can not ask any questions for clarification. There will not be any further messages provided about the image provided. 
                If certain information is missing that is required, you must decide that information on your own. 
                Come up with a set of materials and instructions based on the image tags. Include a legend for any abbreviations
                that beginner crocheters might not know. The tags are: {tags_array}"""
            }
        ],
        model="llama3-8b-8192"
    )

    response = chat_completion.choices[0].message.content

    # Output the API response
    return response
    #print(response)

# print(analyze_image_and_generate_pattern("https://images-ext-1.discordapp.net/external/N1PJfiAdil7yMxEwqEVE6RtDlDmIcZBStdXPDjHzkn8/https/m.media-amazon.com/images/I/51G9HvPQ-bL.jpg?width=468&height=468"))
'''
Computer Vision Section - Commented out since we are now using 
Azure.AI.Vision.ImageAnalysis instead of Azure.CognitiveServices.Vision.ComputerVision
Keeping for reference
'''

# computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
# '''
# END - Authenticate
# '''

# '''
# Quickstart variables
# These variables are shared by several examples
# '''
# # Images used for the examples: Describe an image, Categorize an image, Tag an image, 
# # Detect faces, Detect adult or racy content, Detect the color scheme, 
# # Detect domain-specific content, Detect image types, Detect objects
# images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")
# remote_image_url = "https://images-ext-1.discordapp.net/external/Af8sIRhgdw28iYnuODvtb1gY8_xWJNV8ryKikDvZVMg/https/assets.voxcity.com/uploads/blog_images/Iconic%2520Landmarks%2520in%2520Rome_original.jpg?width=832&height=468"
# '''
# END - Quickstart variables
# '''


# '''
# Tag an Image - remote
# This example returns a tag (key word) for each thing in the image.
# '''
# # Call API with remote image and request specific visual features
# visual_features = [VisualFeatureTypes.categories, VisualFeatureTypes.tags, VisualFeatureTypes.description, VisualFeatureTypes.objects]

# tags_result_remote = computervision_client.analyze_image(remote_image_url, visual_features=visual_features)

# # Print results of categories with confidence score
# print("Categories and tags in the remote image:")
# if not tags_result_remote.categories:
#     print("No categories detected.")
# else:
#     for category in tags_result_remote.categories:
#         print(f"Category '{category.name}' with confidence {category.score * 100:.2f}%")

# # Print results of tags with confidence score
# if not tags_result_remote.tags:
#     print("No tags detected.")
# else:
#     for tag in tags_result_remote.tags:
#         print(f"Tag '{tag.name}' with confidence {tag.confidence * 100:.2f}%")

# # Print results of description with confidence score
# if not tags_result_remote.description.captions:
#     print("No description detected.")
# else:
#     for caption in tags_result_remote.description.captions:
#         print(f"Description: '{caption.text}' with confidence {caption.confidence * 100:.2f}%")

# # Print results of objects with confidence score
# if not tags_result_remote.objects:
#     print("No objects detected.")
# else:
#     print("Objects in the remote image:")
#     for object in tags_result_remote.objects:
#         print(f"Object '{object.object_property}' with confidence {object.confidence * 100:.2f}%")

# print()
# '''
# END - Tag an Image - remote
# '''
# print("End of Computer Vision quickstart.")