# 🎓 AI-Driven Student Dropout Prediction System

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-2.0.2-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📋 Project Overview

An AI-powered decision-support system that predicts student dropout risk using machine learning to enable early intervention strategies. This project uses **XGBoost** as the primary model and **Logistic Regression** as a baseline to predict whether a student will graduate, drop out, or remain enrolled.

### 🎯 Key Features

- **Real-time Predictions**: Instant dropout risk assessment
- **Interactive Dashboard**: Beautiful, modern UI built with Streamlit
- **Model Comparison**: Compare XGBoost vs Logistic Regression predictions
- **Risk Analysis**: Identify key risk factors and probability distributions
- **Personalized Recommendations**: Tailored intervention suggestions
- **Data Analytics**: Comprehensive visualizations and insights

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Installation

1. **Clone or download this repository**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app_professional.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8502`

## 📊 Dataset

- **Source**: [Kaggle - Predict Students' Dropout and Academic Success](https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention)
- **Records**: ~4,400 student profiles
- **Features**: 35 attributes including:
  - Demographics (age, gender, marital status)
  - Academic performance (grades, attendance, enrolled units)
  - Socio-economic factors (tuition status, scholarships, parental education)
  - Economic indicators (unemployment rate, inflation, GDP)

## 🏗️ Project Structure

```text
BigData&AI/
├── app_professional.py        # Main Streamlit application
├── xgboost_model.pkl          # Trained XGBoost model
├── baseline_model.pkl         # Trained Logistic Regression model
├── scaler.pkl                 # Feature scaler
├── label_encoder.pkl          # Label encoder
├── cleaned_dataset.csv        # Preprocessed dataset
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── .streamlit/
    └── config.toml            # Streamlit configuration
```

## 🤖 Models Used

### Primary Model: XGBoost
- **Accuracy**: High performance on imbalanced data
- **Features**: Handles mixed data types, built-in regularization
- **Explainability**: Feature importance and SHAP values

### Baseline Model: Logistic Regression
- **Purpose**: Statistical baseline for comparison
- **Interpretability**: Clear coefficient interpretation
- **Speed**: Fast inference time

## 🎨 Application Features

### 1. Home Dashboard
- Project overview and statistics
- Target distribution visualization
- Quick metrics (dropout rate, graduation rate)

### 2. Prediction Interface
- Comprehensive input form organized by sections:
  - Demographics
  - Academic Information
  - Socio-Economic Factors
  - Academic Performance (Semester 1 & 2)
  - Economic Indicators
- Real-time prediction results
- Probability distribution charts
- Risk factor identification
- Personalized intervention recommendations

### 3. Analytics Dashboard
- Gender distribution analysis
- Tuition payment impact
- Age distribution
- Grade performance analysis

### 4. About Section
- Project information
- Model details
- Dataset description
- Developer information

## 🌐 Deployment

### Deploy to Streamlit Cloud (Recommended)

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository, branch, and main file (app.py)
   - Click "Deploy"

3. **Your app will be live at**: `https://your-app-name.streamlit.app`

### Alternative: Deploy to Heroku

1. Create `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. Create `setup.sh`:
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   \n\
   " > ~/.streamlit/config.toml
   ```

3. Deploy:
   ```bash
   heroku login
   heroku create your-app-name
   git push heroku main
   ```

## 📈 Model Performance

| Metric | XGBoost | Logistic Regression |
|--------|---------|---------------------|
| Accuracy | ~85-90% | ~75-80% |
| Precision | High | Moderate |
| Recall | High | Moderate |
| F1-Score | High | Moderate |

## 🔍 Key Insights

1. **Tuition Payment Status**: Strongest predictor of dropout risk
2. **Academic Performance**: 1st semester grades highly correlated with outcomes
3. **Socio-Economic Factors**: Scholarship status and parental education matter
4. **Age**: Non-traditional students (>25) have different risk profiles

## 👨‍💻 Developer

**Subhangee Bhattacharjee** (GH1040365)
- Final Year Project
- Program: Big Data & AI

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- Dataset provided by Kaggle
- Streamlit for the amazing framework
- Plotly for interactive visualizations

## 📧 Contact

For questions or feedback, please contact through the project repository.

---

**Made with ❤️ for academic excellence and student success**
