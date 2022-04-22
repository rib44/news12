# in pwsh run { $env:FLASK_APP = "application.py" }

from flask import Flask, redirect, render_template
from newsapi import NewsApiClient       # importing the newsapi client

# configuring application
app = Flask(__name__)

# setting the server as development mode
if __name__ == '__main__':
    app.run(debug=True)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"]  = True

# Initializing the newsapi
newsapi = NewsApiClient(api_key='056c0e07a0ab4846ac0ba7d44ef80f89')


@app.route("/")
def index():
    
    news_source = 'bbc-news'

    # for top headlines:
    top_headlines = newsapi.get_top_headlines(sources = news_source)

    t_articles = top_headlines['articles']
    
    # making a list of contents
    news = []
    desc = []
    img = []
    p_date = []
    url = []

    for i in range (len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        contents = zip( news,desc,img,p_date,url)



    return render_template ("index.html",contents=contents)


@app.route("/verge")
def verge():
    
    news_source = 'the-verge'

    # for top headlines:
    top_headlines = newsapi.get_top_headlines(sources = news_source)

    t_articles = top_headlines['articles']
    
    # making a list of contents
    news = []
    desc = []
    img = []
    p_date = []
    url = []

    for i in range (len(t_articles)):
        main_article = t_articles[i]

        news.append(main_article['title'])
        desc.append(main_article['description'])
        img.append(main_article['urlToImage'])
        p_date.append(main_article['publishedAt'])
        url.append(main_article['url'])

        contents = zip( news,desc,img,p_date,url)

    return render_template ("index.html",contents=contents)