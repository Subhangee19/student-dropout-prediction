# Student Dropout Prediction System

AI-Powered Early Intervention & Risk Assessment Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://student-dropout-predictions.streamlit.app)

## Overview

This project implements an AI-driven decision-support system for predicting student dropout risk in higher education institutions. Using machine learning and interactive web technologies, the system enables proactive early intervention strategies to improve student retention and graduation rates.

## Features

- **High-Accuracy Predictions**: XGBoost model achieving 87-90% accuracy for multi-class classification (Graduate/Dropout/Enrolled)
- **Voice-Enabled Input**: Conversational data collection using Web Speech API
- **Interactive Dashboard**: Real-time analytics with Plotly visualizations
- **Risk Factor Analysis**: Explainable AI identifying specific dropout risk factors
- **Professional UI**: Navy & Gold themed interface with responsive design

## Demo

- **Live Application**: [https://student-dropout-predictions.streamlit.app](https://student-dropout-predictions.streamlit.app)
- **Video Demo**: [Link to demonstration video]

## Dataset

**Source**: [Kaggle - Predict Students' Dropout and Academic Success](https://www.kaggle.com/datasets/thedevastator/higher-education-predictors-of-student-retention)

- **Records**: 4,424 students
- **Features**: 35 attributes (demographic, academic, financial, socio-economic)
- **Target Classes**: Graduate, Dropout, Enrolled

## Technology Stack

- **Frontend**: Streamlit + Custom CSS/JS
- **ML Framework**: XGBoost 2.0.2, Scikit-learn 1.3.2
- **Visualization**: Plotly
- **Data Processing**: Pandas, NumPy
- **Deployment**: Streamlit Cloud

## Installation

```bash
# Clone the repository
git clone https://github.com/Subhangee19/student-dropout-prediction.git
cd student-dropout-prediction

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app_professional.py
```

## Usage

### Manual Prediction
1. Navigate to the **Prediction** page
2. Enter student demographics, academic performance, and financial status
3. Click "Generate Prediction" to view dropout risk assessment

### Voice Input
1. Navigate to the **Voice Input** page
2. Click "Start Voice Input" and allow microphone access
3. Answer AI prompts conversationally
4. Receive instant prediction with vocal confirmation

## Model Performance

| Metric | XGBoost | Logistic Regression |
|--------|---------|---------------------|
| Accuracy | 87-90% | 75-80% |
| Precision | High | Moderate |
| Recall | High | Moderate |
| F1-Score | High | Moderate |
| Inference Time | <50ms | <10ms |

## Project Structure

```
student-dropout-prediction/
├── app_professional.py       # Main Streamlit application
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── config.toml          # Streamlit configuration
├── xgbmo.pkl                # Trained XGBoost model
├── basmo.pkl                # Baseline Logistic Regression model
├── scal.pkl                 # Feature scaler
├── labenco.pkl              # Label encoder
└── cleaned_dataset.csv      # Preprocessed dataset
```

## Key Findings

1. **Tuition Payment Status**: 88% dropout rate for unpaid tuition vs. 25% for paid
2. **First Semester Performance**: Students with grades <10 have 65% dropout rate
3. **Scholarship Impact**: Scholarship holders show 70% graduation rate
4. **Financial Instability**: Non-scholarship + unpaid tuition = 82% dropout rate

## Future Enhancements

- SHAP values for enhanced explainability
- LSTM/GRU networks for temporal behavioral analysis
- Multi-institutional deployment with transfer learning
- Reinforcement learning for personalized intervention recommendations

## Author

**Subhangee Bhattacharjee**
- Student ID: GH1040365
- Programme: MSc Big Data & AI
- Module: M516 Business Project in Big Data & AI

## License

This project is developed for academic purposes as part of MSc Big Data & AI program at Gisma University of Applied Sciences.

## Acknowledgments

- Dataset: Realinho, V., Machado, J., Baptista, L., & Martins, M. V. (2022)
- Streamlit for the amazing web framework
- XGBoost developers for the powerful ML library
