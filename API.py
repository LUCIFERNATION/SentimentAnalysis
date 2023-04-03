import requests
import json
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from textblob import TextBlob

url = "https://amazon23.p.rapidapi.com/reviews"

querystring = {"asin":"B07XQXZXJC","sort_by":"helpful","country":"US"}

headers = {
	"X-RapidAPI-Key": "79d614ce0fmsh4e9fb94bc52d79ap17873fjsn376baf3d1afc",
	"X-RapidAPI-Host": "amazon23.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)

# Extract review text and rating from the response
reviews = data['result']



review_text_list = []  # Initialize list to store review text
review_rating_list = []  # Initialize list to store review rating

for item in reviews:
    review_text = item['review']
    review_rating = item['rating']
    review_text_list.append(review_text)
    review_rating_list.append(review_rating)

print("Review Texts:", review_text_list)
print("Review Ratings:", review_rating_list)


# Process the review text and ratings for use in a machine learning model
dataset = list(zip(review_text_list, review_rating_list))
df = pd.DataFrame(dataset, columns=[0, 1])

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[0], df[1], test_size=0.2)

# Vectorize text data using count vectorizer
vectorizer = CountVectorizer(stop_words='english')
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train and evaluate Naive Bayes model
nb_model = MultinomialNB()
nb_model.fit(X_train_vec, y_train)
accuracy = nb_model.score(X_test_vec, y_test)

print('Model accuracy:', accuracy)



reviews = df[0].tolist()


for review in reviews:
    blob = TextBlob(review)
    sentiment = blob.sentiment.polarity
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment}")
    print("")
