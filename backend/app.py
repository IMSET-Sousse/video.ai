from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def generate_video(prompt):
    # generate video
    return 'mov_bbb.mp4'



@app.route('/api/video', methods=['POST'])
def hello_world():
    if not request.json or 'prompt' not in request.json:
        return jsonify({"error": "Prompt is required"}), 400
    
    prompt = request.json['prompt']
    
    # generate video
    video_path = generate_video(prompt)

    video_data = {
        'prompt': prompt,
        'video_path': video_path
    }

    return jsonify(video_data), 200


if __name__ == '__main__':
    app.run(debug=True)