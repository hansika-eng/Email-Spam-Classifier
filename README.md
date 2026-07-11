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

<img width="1912" height="917" alt="image" src="https://github.com/user-attachments/assets/112ee940-c6bd-442d-b892-11ab6fea788a" />


---

### Spam Email Detection

<img width="1570" height="865" alt="image" src="https://github.com/user-attachments/assets/20a56f55-3129-45d6-aa74-37d285b7885c" />
<img width="1911" height="881" alt="image" src="https://github.com/user-attachments/assets/40531148-483c-4349-a4d3-8de1b0cd016f" />


---

### Safe Email Detection

<img width="1547" height="861" alt="image" src="https://github.com/user-attachments/assets/8f5172d4-5052-4aeb-a804-37445bfb9602" />



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
git clone https://github.com/hansika-eng/Email-Spam-Classifier.git
```

Move into the project

```bash
cd Email-Spam-Classifier
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
