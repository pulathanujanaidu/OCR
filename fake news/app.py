import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.model_selection import train_test_split

app = Flask(__name__)
pac = PassiveAggressiveClassifier(max_iter=50)
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)

# Load your dataset
my_data = pd.read_csv('data.csv')
labels = my_data.Label
my_data['New_Label'] = my_data['Label'].map(str)
my_data['Body'] = my_data['Body'].map(str)
my_data['Body'] = my_data['Body'].apply(str.lower)
x_train, x_test, y_train, y_test = train_test_split(my_data['Body'], labels, test_size=0.2, random_state=7)

# Fit the TF-IDF vectorizer and the model
tfidf_train = tfidf_vectorizer.fit_transform(x_train)
pac.fit(tfidf_train, y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = [request.form['text']]
        tfidf_text = tfidf_vectorizer.transform(text)

        prediction = pac.predict(tfidf_text[0])
        return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
