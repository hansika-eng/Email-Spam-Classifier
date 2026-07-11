# 📧 AI Email Spam Detector

A Machine Learning-powered Email Spam Detection system built with **Python**, **Scikit-learn**, and **Streamlit**. This application classifies emails as **Spam** or **Safe (Ham)** using Natural Language Processing (NLP) techniques and a trained ML model.

---

## 🚀 Live Features

- 📧 Email Spam Detection
- 🤖 Machine Learning Classification
- 📝 TF-IDF Text Vectorization
- 📊 Prediction Confidence Score
- 📈 Email Statistics
  - Word Count
  - Character Count
  - Line Count
- ⚠ Security Tips
- 🌙 Modern Dark UI
- ⚡ Interactive Streamlit Web Application

---

## 🛠 Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Plotly
- Joblib

---

## 📂 Project Structure

```text
Email-Spam-Detection/
│
├── dataset/
│   └── spam.csv
│
├── models/
│   ├── spam_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── app.py
├── styles.css
├── email_spam_detection.ipynb
├── requirements.txt
├── README.md
```

---

## 📷 Screenshots

### Home Page

![Home](images/home.png)

---

### Spam Email Detection

![Spam](images/spam_prediction.png)

---

### Safe Email Detection

![Safe](images/safe_prediction.png)

---

## ⚙ How It Works

1. User enters an email.
2. Text is cleaned and transformed using TF-IDF Vectorizer.
3. The trained Machine Learning model predicts whether the email is Spam or Safe.
4. Prediction confidence is displayed.
5. Email statistics are generated.

---

## 🧠 Machine Learning Pipeline

Dataset

↓

Text Cleaning

↓

TF-IDF Vectorization

↓

Train/Test Split

↓

Model Training

↓

Model Evaluation

↓

Model Saving (Joblib)

↓

Streamlit Deployment

---

## 📊 Model Details

- Vectorizer: TF-IDF
- Algorithm: Multinomial Naive Bayes
- Model Serialization: Joblib

---

## ▶ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Email-Spam-Detection.git
```

Move into the project

```bash
cd Email-Spam-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📦 Requirements

- Python 3.11+
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Plotly
- Joblib

---

## 👩‍💻 Author

**Hansika Indukuri**

Machine Learning Intern Project

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub.
