from newsapi import NewsApiClient
import datetime

def get_top_articles(api_key, topic):
    newsapi = NewsApiClient(api_key=api_key)

    # Get the current date
    today = datetime.date.today()

    # Get the top headlines for the specified topic
    top_headlines = newsapi.get_top_headlines(q=topic, language='en', country='us')

    # Extract the top three articles
    top_three_articles = top_headlines['articles'][:3]

    # Print the top three articles
    print(f"Top three articles about '{topic}' on {today}:\n")
    for index, article in enumerate(top_three_articles, start=1):
        print(f"{index}. {article['title']}")
        print(f"   Source: {article['source']['name']}")
        print(f"   URL: {article['url']}\n")

if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual News API key
    api_key = 'YOUR_API_KEY'
    
    # Replace 'YOUR_TOPIC' with the desired topic
    topic = 'YOUR_TOPIC'

    get_top_articles(api_key, topic)
