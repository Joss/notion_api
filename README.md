# Simple Notion API
Simple Notion.so API to add a note into selected page by email

### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

- Press the button above
- Create a new Herocu account, confirm the email
- Choose an app name and select prefered region for server

<img width="500px" src="https://user-images.githubusercontent.com/9437720/92416668-416fe880-f167-11ea-9ede-ed1b96b5b158.png?raw=true">

- Press `Deploy app` button
- Press the `View` button and keep a web link to app url

### Configure IFTTT
- Goto https://ifttt.com/
- Login and press `Create`
- Add `Email` as service

<img width="500px" src="https://user-images.githubusercontent.com/9437720/92417016-c7d8fa00-f168-11ea-8540-710a9c979cb2.png?raw=true">

- Select `Send IFTTT any email` 
- Add `Webhooks` as action service

<img width="500px" src="https://user-images.githubusercontent.com/9437720/92417019-cc051780-f168-11ea-960d-7878b75244ed.png?raw=true">

- Select `Make a web request`
- Add `<web_link_to_app>/add_block` (if you prefer collect all emails on one page as blocks) or `<web_link_to_app>/add_page` (if you want to keep emails as separate pages) to URL
- Select `Post` method
- Select `application/json` content type
- Add `{"token":"<token_v2>", "link":"<page_link>", "note":"<<<{{Body}}>>>", "title":"<<<{{Subject}}>>>"}` as body

<img width="500px" src="https://user-images.githubusercontent.com/9437720/92419570-0aa1ce80-f177-11ea-9156-9c4f92d58efa.png?raw=true">

### Testing
1. Forward an email from your mailbox to `trigger@applet.ifttt.com`
