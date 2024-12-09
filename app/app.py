from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from app.services.main import analyze_image_and_generate_pattern

# initalize the Flask app
app = Flask(__name__)
CORS(app)

# define the index route 
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/", methods=["POST"])
def process_image():
    data = request.get_json()
    image_url = data.get("image_url")

    if not image_url:
        return jsonify({"error": "Image URL is required"}), 400

    # Call the image analysis function
    result = analyze_image_and_generate_pattern(image_url)

    if result is None:
        return jsonify({"error": "Failed to analyze the image"}), 500

    # Return the pattern data
    return result

if __name__ == "__main__":
    app.run(debug=True)