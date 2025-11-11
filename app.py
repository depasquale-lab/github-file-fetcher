from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/github/file', methods=['POST'])
def get_github_file():
    data = request.get_json()
    repo = data.get('repo')
    path = data.get('path')
    branch = data.get('branch', 'main')

    if not repo or not path:
        return jsonify({"error": "Missing 'repo' or 'path'"}), 400

    url = f"https://raw.githubusercontent.com/{repo}/{branch}/{path}"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "File not found", "url": url}), 404

    return jsonify({
        "url": url,
        "content": response.text
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
