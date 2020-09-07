# notion_api
Simple Notion.so API to add a note into selected page

### Deploy to Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Configure IFTTT

1. Goto https://ifttt.com/
2. Press `Create`
3. Add `Email` as service
4. Select `Send IFTTT any email`
5. Add `Webhooks` as action service
6. Select `Make a web request`
7. Add `<your_heroku_link>/add_url` to URL
8. Select `Post` method
9. Select `application/json` content type
10. Add `{"token":"<token_v2>", "link":"<page_link>", "note":"<<<{{Body}}>>>"}` as body

