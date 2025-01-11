from robyn import Robyn, jsonify, Response
from typing import Dict, List

app = Robyn(__file__)

# Sample content data
content = [
    {
        "id": 1,
        "title": "Getting Started",
        "category": "Basics",
        "content": "This is the getting started guide..."
    },
    {
        "id": 2,
        "title": "Advanced Topics",
        "category": "Advanced",
        "content": "Advanced topics include..."
    }
]

@app.get("/api/content")
async def get_content() -> Response:
    # Add CORS headers
    headers = {
        "Access-Control-Allow-Origin": "http://localhost:3000",
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "*",
    }
    return jsonify(content)

@app.get("/api/content/:content_id")
async def get_content_by_id(request) -> Response:
    content_id = int(request.path_params.get("content_id"))
    headers = {
        "Access-Control-Allow-Origin": "http://localhost:3000",
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "*",
    }
    
    for item in content:
        if item["id"] == content_id:
            return jsonify(item, headers=headers)
    return jsonify({"error": "Content not found"}, headers=headers, status_code=404)

# Handle CORS preflight requests
@app.options("/*")
async def handle_options() -> Response:
    headers = {
        "Access-Control-Allow-Origin": "http://localhost:3000",
        "Access-Control-Allow-Methods": "GET, OPTIONS",
        "Access-Control-Allow-Headers": "*",
    }
    return Response(status_code=204, headers=headers)

if __name__ == "__main__":
    app.start(port=8000) 