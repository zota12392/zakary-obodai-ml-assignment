# AI Assignment 1

This project is a complete end-to-end machine learning pipeline built using the Titanic dataset. It includes all phases: data cleaning, EDA, model training, and an interactive Streamlit UI.

---

#### AUTHOR

- **Zakary Obodai**
- **BIT**
- **2305000083**

---

> **Instructor**: Victor Muvunyi  
> **Deadline**: June 14, 2025  
> **GitHub Repo**: https://github.com/zota12392/zakary-obodai-ml-assignment

---

## 🔍 Objective

Build a machine learning pipeline in Python to predict survival on the Titanic. The pipeline includes:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Model Training
- Interactive UI via Streamlit

---

## 📁 Project Structure

- ├── notebook.ipynb # Jupyter notebook with all tasks
- ├── app.py # Streamlit app for prediction (Task 4)
- | ├── cleaned_data # Cleaned Titanic dataset
- | ├── rawtitanic.csv # Titanic dataset
- ├── titanic_model.pkl # Trained RandomForest model
- ├── model_columns.pkl # Feature list used in model
- ├── requirements.txt # Python dependencies
- ├── README.md # Project documentation
- └── .gitignore # Files to ignore in version control

---

---

## Task Description

### 🔹 Task 1: Data Cleaning

- Dataset: Titanic
- Tools: `pandas`
- Actions:
  - Filled missing values (`Age`, `Embarked`)
  - Dropped unnecessary columns (`Cabin`, `Name`, `Ticket`)
  - Saved result as `data/cleaned_data.csv`

---

### 🔹 Task 2: Exploratory Data Analysis (EDA)

- Tools: `matplotlib`, `seaborn`, `ydata-profiling`
- Performed:
  - Summary statistics with `df.describe(include='all')`
  - Visualizations:
    - Survival countplot
    - Age distribution histogram
    - Feature correlation heatmap

---

### 🔹 Task 3: Machine Learning Model

- Model: `RandomForestClassifier`
- Tools: `scikit-learn`
- Process:
  - Label encoding of categorical features
  - Train-test split (80/20)
  - Evaluated using accuracy, confusion matrix, and classification report
  - Model saved as `titanic_model.pkl`

---

### 🔹 Task 4: UI with Streamlit

- File: `app.py`
- Features:
  - Takes user input: class, age, sex, fare, etc.
  - Predicts survival using trained model
  - Shows result in the browser

---

## ⚙️ How to Run This Project

### 1. Clone the Repository

````bash
git clone https://github.com/zota12392/zakary-obodai-ml-assignment
cd zakary-obodai-ml-assignment


### 🔹 2. Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
````

### 🔹 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 🔹 4. Run Streamlit App

```bash
streamlit run app.py
```

### ✅ Requirements

### All dependencies are listed in requirements.txt, including:

- `pandas`

- `seaborn`

- `matplotlib`

- `scikit-learn`

- `ydata-profiling`

- `streamlit`

- `joblib`

### 📊 Sample Prediction

Enter details in the web form and get a prediction like:

```bash
🎉 Survived!
```

OR

```bash
❌ Did not survive.
```

### 📌 Notes

- Cleaned dataset: cleaned_data.csv

- Model saved as: titanic_model.pkl

- Make sure these files are in the root directory when running the app.
