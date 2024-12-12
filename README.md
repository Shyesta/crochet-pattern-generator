# Crotchet Pattern Generator

### Authors: Sage Bain, Leah Konma
### Date: December 11, 2024

The goal of this project is to be able to submit a simple image and have AI generate a crotchet pattern that the user can follow to create a crotchet plush. Microsoft Azure services is utilized to make API calls to have the image analyzed. 

# Setup
<strong> Run the following commands: </strong>
- pip install pillow
- pip install flask flask_cors
- pip install groq
- pip install azure-cognitiveservices-vision-computervision
- pip install azure.ai.vision.imageanalysis
- setx VISION_KEY <your_vision_key_here>
- setx VISION_ENDPOINT <your_vision_endpoint_here>
- setx GROQ_API_KEY <your_groq_api_key_here>

<strong> Restart your IDE </strong>

# Running the Code
- In the terminal, run the command python -m app.app
- Open the URL listed from flask in the terminal (this will open an HTML page in your browser)
- Input an image URL into the textbox provided on the HTML page
- Expected Output: instructions on how to recreate the crochet pattern based off the ImageAnalysisClient tag results.

# Analysis of Capabilities and Limitations
## Capabilities
- Connects directly to two separate API's in Groq and Azure Cognitive Services
- Can take in an image URL and return basic instructions on how to recreate the object in crochet

## Limitations:
- There is no error handling in regards to improper images if the image can not be recreated in Crochet.
- Users cannot input special instructions based off of what they want, i.e. certain materials, colors, or other things used.
- We are working off of Azure's default model, which is very limited in how it analyzes the images provided. This results in sometimes generic tags/features being handed to the LLM that generates instructions.

# Potential Future Improvements
- Create and train our own model that can properly return more important image tags or visual features that are relevant to crochet pattern making
- Allow users a space to interact with Groq if they have special instructions, or need to refine the instructions that are returned to them.
- Include additional error handling for bad images provided.
- Include a way to upload files directly instead of providing an image URL, which will give users more flexibility in how they interact with the AI app.
