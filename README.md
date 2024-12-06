# Crotchet Pattern Generator

### Authors: Sage Bain, Leah Konma
### Date: December 11, 2024

The goal of this project is to be able to submit a simple image and have AI generate a crotchet pattern that the user can follow to create an amigurumi style crotchet plush. Microsoft Azure services is utilized to make API calls to have the image analyzed. 

## Setup
<strong> Run the following commands: </strong>
- pip install pillow
- pip install flask
- pip install groq
- pip install azure-cognitiveservices-vision-computervision
- pip install azure.ai.vision.imageanalysis
- setx VISION_KEY <your_vision_key_here>
- setx VISION_ENDPOINT <your_vision_endpoint_here>
- setx GROQ_API_KEY <your_groq_api_key_here>
- OPTIONAL, HIGHLY RECOMMENDED: Install VS Code extension "Live Preview" from Microsoft to preview the website and upload image URL's

<strong> Restart your IDE </strong>

## Running the Code
- Open the HTML page in your browser
- Upload an image URL into the input box provided
- Expected output on the webpage is the instructions on how to recreate the crochet pattern based off the ImageAnalysisClient tag results.

## Analysis of Capabilities and Limitations
## Potential Future Improvements