from datetime import date

from notion.client import NotionClient
from notion.block.basic import TextBlock, PageBlock 

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Notion API</h1><p>Use /add_block, /add_page or /add_record</p>"

@app.route('/add_block', methods=['POST'])
def add_block():
    try:
        token_v2 = request.json['token']
        notebook_link = request.json['link']
        note_title = request.json['title']
        note_text = request.json['note']        

        client = NotionClient(token_v2)
        page = client.get_block(notebook_link)

        today = date.today()
        new_block = page.children.add_new(TextBlock, title=today.strftime("%d/%m/%y") + ": " + note_title)
        new_block.set('format.block_color', 'red')        
        page.children.add_new(TextBlock, title=note_text)

        return 'The note added', 200
    except Exception:
        return 'Adding the note failed', 500

@app.route('/add_page', methods=['POST'])
def add_page():
    try:
        token_v2 = request.json['token']
        notebook_link = request.json['link']
        note_title = request.json['title']
        note_text = request.json['note']

        client = NotionClient(token_v2)
        page = client.get_block(notebook_link)

        today = date.today()
        new_page = page.children.add_new(PageBlock, title=today.strftime("%d/%m/%y") + ": " + note_title)
        new_page.children.add_new(TextBlock, title=note_text)

        return 'The page added', 200
    except Exception:
        return 'Adding the page failed', 500        

@app.route('/add_record', methods=['POST'])
def add_record():
    try:
        token_v2 = request.json['token']
        notebook_link = request.json['link']
        note_title = request.json['title']
        note_text = request.json['note']

        client = NotionClient(token_v2)
        cv = client.get_collection_view(notebook_link)

        print(cv.parent.views)
        cv.collection.add_row(Header=note_title, Message=note_text, Date=date.today())

        return 'The record added', 200
    except Exception:
        return 'Adding the record failed', 500            

if __name__ == '__main__':
    app.run(threaded=True, port=5000)        

