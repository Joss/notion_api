# Simple Notion API
Simple Notion.so API to add a note into selected page by email

### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

1. Press the button above
2. Create a new Herocu account, confirm the email
3. Choose an app name and select prefered region for server
<p align="left">
  <img src="https://user-images.githubusercontent.com/9437720/92416668-416fe880-f167-11ea-9ede-ed1b96b5b158.png" />
</p>
4. Press `Deploy` button
5. Press the `View` button and keep a web link to app url
<p align="left">
  <img src="https://user-images.githubusercontent.com/9437720/92416811-f2768300-f167-11ea-9afb-cc3e445988e9.png" />
</p>

### Configure IFTTT
1. Goto https://ifttt.com/
2. Login and press `Create`
3. Add `Email` as service
<p align="left"><img src="https://user-images.githubusercontent.com/9437720/92417016-c7d8fa00-f168-11ea-8540-710a9c979cb2.png" /></p>
4. Select `Send IFTTT any email` 
5. Add `Webhooks` as action service
<p align="left"><img src="https://user-images.githubusercontent.com/9437720/92417019-cc051780-f168-11ea-960d-7878b75244ed.png" /></p>
6. Select `Make a web request`
7. Add `<your_heroku_link>/add_block` or `<your_heroku_link>/add_page` to URL
8. Select `Post` method
9. Select `application/json` content type
10. Add `{"token":"<token_v2>", "link":"<page_link>", "note":"<<<{{Body}}>>>", "title":"<<<{{Subject}}>>>"}` as body

### Testing
1. Forward an email from your mailbox to `trigger@applet.ifttt.com`
