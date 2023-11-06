#Part
from mediawiki import MediaWiki 

wikipedia = MediaWiki()
Airbus350 = wikipedia.page("Airbus A350-900")
print(Airbus350.title)
print(Airbus350.content)

def website_keywords():
    """Creates a histogram that contains all the
    relevant keywords associated to the A350-900"""
    hist = {}
    keywords = Airbus350.content

    #clean the keywords:

    keywords = keywords.replace('-', '  ')

    for line in keywords.split:
        word = line.strip()

        line = line.replace('-', ' ')

        for word in line.split():
            hist[word] = hist.get(word, 0) + 1
    
    return hist

from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='ac2e443b9b1246309d13a5488324105f')

#I want to search for news related to Polygon(MATIC)
polygon_articles = newsapi.get_everything(  #used CHATGPT
    q='Polygon MATIC crypto',
    language='en',
    sort_by='relevancy',
    page=1 #adjust page number depending on new/more results
)

#Print the title of searched articles

for article in polygon_articles['articles']:
    print(article['title'])
    print(article['url'])
    print()


from newsapi import NewsApiClient
import ntlk 
from nltk.corpus import stopwords
from collections import Counter 

newsapi = NewsApiClient(api_key='')

#Search for news related to Polygon
polygon_articles = newsapi.get_everything(
    q='Polygon MATIC Crypto',
    language= 'en',
    sort_by='relevancy',
    page=1
)

#make the article text a single string - used ChatGpt
all_text = "".join([article['title'] + ' ' + article['description'] for article in polygon_articles['articles']])

#tokenize the text using nltk
tokens = nltk.word_tokenize(all_text)

#remove stop words
stop_words = set(stopwords.words('english'))
filter_tokens = [word for word in tokens if word.lower() not in stop_words] #used ChatGPT

#calculating word frequencioes
word_freq = counter(filtered_tokens)





if __name__ == "__main__":
    main()
    