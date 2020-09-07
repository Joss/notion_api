from notion.client import NotionClient
from notion.block import TextBlock

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Notion API</h1>"

@app.route('/add_note', methods=['POST'])
def add_note():
    try:
        token_v2 = request.json['token']
        notebook_link = request.json['link']
        note_text = request.json['note']

        client = NotionClient(token_v2)
        page = client.get_block(notebook_link)
        page.children.add_new(TextBlock, title=note_text)

        return 'The note added', 200
    except Exception:
        return 'Adding the note failed', 500

if __name__ == '__main__':
    app.run(threaded=True, port=5000)        

