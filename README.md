# Streamlit Salary Data App

This is a Streamlit web app for exploring and visualizing salary data. You can upload your own CSV or use the provided sample. The app provides interactive charts and insights about salary trends by gender, education, experience, and more.

## Features
- Upload your own salary data CSV or use the default sample
- Data cleaning and exploration
- Visualizations:
  - Salary distribution
  - Average salary by gender
  - Average salary by education level
  - Salary vs. years of experience
  - Gender distribution by education level
  - Age vs. salary
  - Top 10 paying jobs

## How to Run Locally
1. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   streamlit run streamlit_app.py
   ```

## Deploy Online
- Push this repo to GitHub.
- Go to [Streamlit Cloud](https://streamlit.io/cloud), connect your repo, and deploy `streamlit_app.py`.

## File Structure
- `streamlit_app.py` — Main Streamlit app
- `Salary_Data.csv` — Sample dataset

## Example
![screenshot](screenshot.png)

---

## License
MIT
