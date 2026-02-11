import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Sample dataset
data = {
    "url": [
        "https://google.com",
        "https://facebook.com",
        "https://bank-login-secure.xyz",
        "http://verify-account-alert.com"
    ],
    "label": [0, 0, 1, 1]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["url"])
y = df["label"]

model = LogisticRegression()
model.fit(X, y)

def predict_url(url):
    url_vector = vectorizer.transform([url])
    prediction = model.predict(url_vector)
    return "Phishing Website ⚠️" if prediction[0] == 1 else "Safe Website ✅"
