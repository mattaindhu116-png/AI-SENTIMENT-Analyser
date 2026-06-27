from textblob import TextBlob
import pandas as pd
from datetime import datetime

history = []

print("=" * 55)
print("        AI SENTIMENT ANALYZER")
print("=" * 55)

while True:
    text = input("\nEnter a sentence (or type 'exit' to quit): ")

    if text.lower() == "exit":
        break

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity

    if polarity > 0.3:
        sentiment = "Positive 😊"
    elif polarity < -0.3:
        sentiment = "Negative 😔"
    else:
        sentiment = "Neutral 😐"

    print("\n------ Result ------")
    print(f"Text         : {text}")
    print(f"Polarity     : {polarity:.2f}")
    print(f"Subjectivity : {subjectivity:.2f}")
    print(f"Sentiment    : {sentiment}")

    history.append({
        "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Text": text,
        "Polarity": round(polarity, 2),
        "Subjectivity": round(subjectivity, 2),
        "Sentiment": sentiment
    })

if history:
    df = pd.DataFrame(history)
    df.to_csv("sentiment_history.csv", index=False)
    print("\nHistory saved as 'sentiment_history.csv'")

print("\nThank you for using AI Sentiment Analyzer!")
