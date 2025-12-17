# Quick Start Guide

## Local Testing (Before Deployment)

### Run the application locally:

```bash
cd "c:\Users\s.bhattacharjee\BigData&AI"
streamlit run app_professional.py
```

The application will open automatically in your browser at `http://localhost:8502`

## Deploy to Streamlit Cloud (5 Minutes)

### Step 1: Push to GitHub

```bash
# Create a repository on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/student-dropout-prediction.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select:
   - **Repository:** `YOUR_USERNAME/student-dropout-prediction`
   - **Branch:** `main`
   - **Main file:** `app_professional.py`
5. Click "Deploy!"

Your app will be live at: `https://YOUR_USERNAME-student-dropout-prediction.streamlit.app`

## What's Included

✅ **Application Files:**
- `app_professional.py` - Main Streamlit application
- `.streamlit/config.toml` - Theme configuration

✅ **Machine Learning Models:**
- `xgboost_model.pkl` - Primary XGBoost model (1.9 MB)
- `baseline_model.pkl` - Baseline Logistic Regression (1.5 KB)
- `scaler.pkl` - Feature scaler (2.2 KB)
- `label_encoder.pkl` - Label encoder (275 bytes)

✅ **Data:**
- `cleaned_dataset.csv` - Preprocessed student dataset (470 KB)

✅ **Documentation:**
- `README.md` - Comprehensive project documentation
- `DEPLOYMENT.md` - Detailed deployment guide
- `QUICK_START.md` - This file

✅ **Configuration:**
- `requirements.txt` - Python dependencies
- `.gitignore` - Git exclusions

## Features Available

### 🏠 Home Dashboard
- Overview statistics (dropout rate, graduation rate)
- Target distribution visualization
- System features overview

### 🎯 Manual Prediction
- Comprehensive input form with 10+ parameters
- Real-time prediction results
- Probability distribution charts
- Risk factor identification
- Intervention recommendations

### 🎤 Voice Input (Experimental)
- Conversational AI data collection
- Voice-guided form filling
- Automatic prediction after data collection
- **Note:** Requires HTTPS in production (works on Streamlit Cloud)

### 📊 Analytics Dashboard
- Tuition payment impact analysis
- Academic performance distribution
- Age distribution analysis
- Interactive Plotly charts

## System Requirements

- Python 3.9+
- 2 GB RAM minimum (for model loading)
- Modern web browser (Chrome, Firefox, Edge)
- Internet connection (for deployment)

## Dependencies

All dependencies are listed in `requirements.txt`:
- streamlit==1.29.0
- pandas==2.1.3
- numpy==1.26.2
- scikit-learn==1.3.2
- xgboost==2.0.2
- plotly==5.18.0

## Troubleshooting

### Issue: "Module not found"
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: "File not found" errors
**Solution:** Ensure you're in the correct directory
```bash
cd "c:\Users\s.bhattacharjee\BigData&AI"
```

### Issue: Voice input not working
**Possible causes:**
- Not using HTTPS (required for microphone access)
- Browser doesn't support Web Speech API
- Microphone permissions denied

**Solution:**
- Deploy to Streamlit Cloud (has HTTPS)
- Use Chrome or Edge browser
- Allow microphone access when prompted

### Issue: Slow loading
**Solution:**
- Models are cached after first load
- First load may take 10-20 seconds
- Subsequent loads are faster

## Support

For detailed deployment instructions, see [DEPLOYMENT.md](DEPLOYMENT.md)

For project information, see [README.md](README.md)

---

**Quick Test:**
```bash
# Test all imports work
python -c "import streamlit; import pandas; import xgboost; print('All dependencies OK')"

# Run the app
streamlit run app_professional.py
```

**Project by:** Subhangee Bhattacharjee (GH1040365)
**Course:** Big Data & AI - Final Year Project
