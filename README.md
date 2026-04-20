# 💰 WealthWise AI

### Personal Finance OS for Smarter Financial Decisions

---

## 🚀 Overview

**WealthWise AI** is an AI-powered personal finance assistant that helps users **understand, manage, and improve their financial health**.

Unlike traditional tools that only track expenses or predict outcomes, WealthWise AI goes further:

> ✅ It analyzes your financial behavior

> ✅ Predicts credit approval chances

> ✅ Simulates improvements

> ✅ Provides actionable financial guidance

---

## 🎯 Problem Statement

Many individuals struggle with:

* Poor financial awareness
* Lack of budgeting discipline
* No clear guidance on improving creditworthiness

Most tools either:

* Track expenses ❌
* OR give predictions ❌

👉 But **don’t tell users what to do next**

---

## 💡 Solution

WealthWise AI is designed as a **decision-making system**, not just a tracking tool.

It combines:

* 📊 Budget analysis
* 🧠 Machine learning prediction
* 🔁 Simulation engine
* 🤖 AI-driven guidance

To answer the key question:

> “What should I do to improve my financial future?”

---

## 🔥 Key Features

### 📊 1. Smart Budget Analysis

* Automatically categorizes expenses
* Provides category-wise breakdown
* Detects overspending patterns

---

### 🧠 2. Financial Health Score

* Calculates a score based on:

  * Savings rate
  * Spending behavior
  * Financial stability

---

### 🤖 3. Credit Approval Prediction

* Uses ML model (Decision Tree)
* Outputs:

  * Approval probability
  * Risk level

---

### 🔁 4. Credit Improvement Simulator

* Simulate financial changes:

  * Reduce expenses
  * Increase income
* See real-time impact on:

  * Credit approval probability
  * Financial score

---

### 💡 5. AI Financial Assistant

* Ask questions like:

  * “Can I afford a ₹50,000 phone?”
  * “How do I improve my credit chances?”
* Get personalized responses based on real data

---

## 🧱 Tech Stack

* **Backend:** Flask (Python)
* **Machine Learning:** Scikit-learn (Decision Tree)
* **Data Processing:** Pandas, NumPy
* **Architecture:** Modular service-based design

---

## 📁 Project Structure

```
backend/
│── app.py
│── routes/
│── services/
│── utils/
│── model/
│── data/
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/kanak-404/WealthWise-AI
cd backend
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

### 3. Run the application

```
python app.py
```

Server will start at:

```
http://127.0.0.1:5000/
```

---

## 🧪 API Usage

### 🔹 Analyze Financial Data

**POST** `/analyze-finance`

```json
{
  "income": 20000,
  "transactions": [
    {"description": "Zomato", "amount": 500}
  ]
}
```

---

### 🔹 Simulate Improvements

**POST** `/simulate-improvement`

```json
{
  "income": 20000,
  "transactions": [...],
  "reduce_expense_by": 2000
}
```

---

### 🔹 Ask AI

**POST** `/ask-ai`

```json
{
  "question": "Can I afford a ₹50000 phone?",
  "income": 20000,
  "transactions": [...]
}
```

---

## 🧠 Innovation

What makes WealthWise AI different:

* ❌ Not just prediction
* ❌ Not just tracking

👉 It provides **actionable financial intelligence**

> “We don’t just tell users where they are — we show them how to improve.”

---

## 📈 Future Scope

* Bank API integration (real transaction data)
* Investment recommendations
* Mobile app deployment
* Personalized financial planning

---

## 🏆 Hackathon Alignment

This project aligns with the **Money Management Track**:

* ✔ Investment & financial guidance
* ✔ Budget tracking
* ✔ Financial literacy
* ✔ Real-world applicability

---

## 👨‍💻 Author

**Kanak Soni**
B.Tech CSE (Cybersecurity)
VIT Bhopal University

---

## 📌 Final Note

WealthWise AI is built with a focus on **real-world usability**, not just demonstration.

> “From prediction to action — making finance smarter for everyone.”
