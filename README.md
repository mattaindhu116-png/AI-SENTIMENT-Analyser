# 😊 AI Sentiment Analyzer

An intermediate-level Python project that analyzes the sentiment of user-entered text using Natural Language Processing (NLP).

The application classifies text as **Positive**, **Negative**, or **Neutral**, displays sentiment scores, and saves all analysis results to a CSV file.

---

## 🚀 Features

- Analyze text sentiment using TextBlob
- Detect Positive, Negative, and Neutral emotions
- Calculate Polarity Score
- Calculate Subjectivity Score
- Save analysis history to a CSV file
- Simple command-line interface
- Beginner-friendly and easy to understand

---

## 📂 Project Structure

```
AI-Sentiment-Analyzer/
│
├── sentiment_analyzer.py
├── sentiment_history.csv
├── README.md
└── requirements.txt
```

---

## 🛠 Requirements

- Python 3.14.6
- TextBlob
- Pandas

Install the required packages:

```bash
pip install textblob pandas
```

Download TextBlob data:

```bash
python -m textblob.download_corpora
```

---

## ▶️ How to Run

Run the program using:

```bash
python sentiment_analyzer.py
```

---

## 💻 Example

```
=======================================================
             AI SENTIMENT ANALYZER
=======================================================

Enter a sentence:
I love learning Python.

------ Result ------
Text         : I love learning Python.
Polarity     : 0.50
Subjectivity : 0.60
Sentiment    : Positive 😊
```

---

## 📊 Sentiment Categories

| Polarity Score | Sentiment |
|---------------|-----------|
| > 0.30 | Positive 😊 |
| < -0.30 | Negative 😔 |
| -0.30 to 0.30 | Neutral 😐 |

---

## 📁 Output

The program automatically creates:

```
sentiment_history.csv
```

Example:

| Date | Text | Polarity | Subjectivity | Sentiment |
|------|------|----------|--------------|-----------|
| 2026-06-27 | I love Python | 0.50 | 0.60 | Positive 😊 |

---

## 📚 Technologies Used

- Python
- TextBlob
- Pandas
- CSV File Handling
- Natural Language Processing (NLP)

---

## 🎯 Future Improvements

- GUI using Tkinter
- Streamlit Web App
- Charts and Graphs
- Voice Input
- AI Emotion Detection
- Multiple Language Support
- PDF Report Generation
- Machine Learning Model Integration

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the MIT License.

---

## 👨‍💻 Author

Developed by **Matta Indhu**

If you found this project useful, don't forget to ⭐ star the repository!
