import requests



def hello(event, context):
    r = requests.get("https://news.ycombinator.com/news")
    return {"content": r.text}
