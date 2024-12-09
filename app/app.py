from flask import Flask, render_template, request, jsonify
from app.services.main import analyze_image_and_generate_pattern

# initalize the Flask app
app = Flask(__name__)

# define the index route 
@app.route('/')
def home():
    return render_template('index.html')

#
@app.route('/', methods=['POST'])
def process_image():
    data = request.get_json()
    image_url = data.get("image_url")
    if not image_url:
        return jsonify({"error": "Image URL is required"}), 400

    # Call the service function
    result = analyze_image_and_generate_pattern(image_url)

    if "error" in result:
        return jsonify({"error": result["error"]}), 500

    return jsonify({"tags": result["tags"], "pattern": result["pattern"]})

# run the app
if __name__ == '__main__':
    app.run(debug=True)