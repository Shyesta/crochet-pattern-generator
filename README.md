# Crotchet Pattern Generator

### Authors: Sage Bain, Leah Konma
### Date: December 11, 2024

The goal of this project is to be able to submit a simple image and have AI generate a crotchet pattern that the user can follow to create an amigurumi style crotchet plush. Microsoft Azure services is utilized to make API calls to have the image analyzed. 

## Setup
<strong> Run the following commands: </strong>
- pip install pillow
- pip install azure-cognitiveservices-vision-computervision
- setx VISION_KEY 97g3WiPAnTBK2ubCnYbZwOPkNE22AsR5xXmsglXFU7HfTkzbwFepJQQJ99AKAC4f1cMXJ3w3AAAFACOGgqh3
- setx VISION_ENDPOINT https://crochet-vision.cognitiveservices.azure.com/    


## Running the Code
- Input a link to an image in the remote_image_url variable 
- Run the code
- Expected output in the terminal is a list of tags with a confidence level attached to each one

## Analysis of Capabilities and Limitations
## Potential Future Improvements