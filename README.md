# 🎓 Placement_Predictor

A Machine Learning web application that predicts whether a student is likely to get placed based on their **CGPA** and **IQ**.

The project uses **Logistic Regression** as the classification algorithm and **Flask** to provide a simple web interface for making predictions.

---

## 🚀 Project Overview

The goal of this project is to build a simple **Binary Classification** model that predicts:

* `1` → Student will get placed
* `0` → Student will not get placed

### Input Features

The model uses:

* **CGPA**
* **IQ**

### Machine Learning Algorithm

**Logistic Regression**

Logistic Regression is used because the target variable has two possible outcomes: **Placed / Not Placed**.

---

## 🛠️ Tech Stack

* **Python**
* **Flask** — Web application
* **Scikit-learn** — Machine Learning
* **NumPy** — Numerical operations
* **Joblib** — Model serialization
* **Gunicorn** — Production WSGI server

---

## 📁 Project Structure

```text
student-placement-prediction/
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
│
└── data/
    └── placement.csv
```

> The exact structure may vary depending on your implementation.

---

# ⚙️ Setup & Installation

Follow the steps below to run the project locally.

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project directory:

```bash
cd student-placement-prediction
```

---

## 2. Create a Virtual Environment

Create a Python virtual environment:

```bash
python -m venv .venv
```

### Windows

Activate the environment:

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

After activation, you should see:

```text
(.venv)
```

in your terminal.

---

## 3. Install Required Libraries

The project includes a `requirements.txt` file containing the required dependencies and their versions.

Install them using:

```bash
pip install -r requirements.txt
```

### Requirements

```text
Flask==3.0.3
scikit-learn==1.5.1
joblib==1.4.2
numpy==1.26.4
gunicorn==22.0.0
```

---

# ▶️ Run the Application

After installing the dependencies, run:

```bash
python app.py
```

The Flask development server will start.

You should see something similar to:

```text
Running on http://127.0.0.1:5000/
```

Open the following URL in your browser:

```text
http://127.0.0.1:5000/
```

You can then enter the student's:

* CGPA
* IQ

and get the predicted placement result.

---

# 🧠 Machine Learning Workflow

The project follows a basic Machine Learning pipeline:

```text
Custom CSV Dataset
        ↓
Data Preparation
        ↓
Feature Selection
        ↓
Train/Test Split
        ↓
Logistic Regression
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Save Trained Model
        ↓
Flask Application
        ↓
User Input
        ↓
Prediction
```

---

# 📊 Dataset

The model is trained using a custom CSV dataset containing student information.

The primary features used by the model are:

| Feature   | Description                                 |
| --------- | ------------------------------------------- |
| CGPA      | Student's academic performance              |
| IQ        | Student's IQ score                          |
| Placement | Target variable indicating placement status |

### Target Variable

```text
1 → Placed
0 → Not Placed
```

---

# 🤖 Model

The project uses **Logistic Regression** for prediction.

The model learns the relationship between:

```text
CGPA + IQ → Placement Probability
```

For example:

```text
CGPA = 8.5
IQ   = 120

        ↓

Logistic Regression

        ↓

Placed
```

The trained model is saved using **Joblib** so that it can be loaded by the Flask application without retraining every time the application starts.

---

# 🌐 Flask Application

The Flask application acts as the interface between the user and the Machine Learning model.

The basic flow is:

```text
User
 ↓
Enter CGPA & IQ
 ↓
Flask Application
 ↓
Load Trained Model
 ↓
Logistic Regression
 ↓
Prediction
 ↓
Placed / Not Placed
```

---

# 📦 Virtual Environment

A virtual environment keeps the project's dependencies isolated from other Python projects on your computer.

This project uses:

```text
.venv/
```

The virtual environment is created locally and is **not required to be uploaded to GitHub**.

Instead, the required packages and their versions are specified in:

```text
requirements.txt
```

Another developer can recreate the environment using:

```bash
pip install -r requirements.txt
```

---

# 🔮 Future Improvements

Possible improvements for this project:

* Add more student features such as attendance, internships, projects, and skills
* Compare Logistic Regression with other classification algorithms
* Add model accuracy and evaluation metrics
* Display prediction probability
* Add data visualization
* Improve the web UI
* Deploy the application online
* Add input validation
* Add automated model retraining

---

# 👨‍💻 Author

**Khushwant Kumawat**

This project was created as a Machine Learning project to understand the complete workflow from **custom dataset → model training → model serialization → Flask deployment**.

<img width="1900" height="864" alt="image" src="https://github.com/user-attachments/assets/27b3babe-fe33-4c49-a7c3-4db34091f5c6" />

