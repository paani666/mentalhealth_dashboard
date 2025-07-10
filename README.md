
# 🧠 Mental Health Survey Dashboard

This is a lightweight, interactive dashboard built using **Streamlit** to help stakeholders visualize and understand patterns in mental health survey data. The application automatically **cleans**, **merges**, and **analyzes** two separate survey datasets, generating insightful visuals.

---

## 📌 Features

✅ Cleans and standardizes gender data  
✅ Removes duplicates and handles missing values  
✅ Merges two datasets on key common fields  
✅ Interactive dashboard with various chart types:
- 🎯 Pie chart (Treatment distribution)
- 🌍 Horizontal bar (Top 10 countries)
- 📈 Violin plot (Age distribution by gender)
- ⚖️ Strip plot (Mood swings vs. Age)
- 📉 Stacked bar (Mental health consequence by family history)

---

## 📂 Files Included

- `mental_health_dashboard_enhanced.py` – Main Streamlit dashboard script  
- `requirements.txt` – Dependencies to run the app  
- `survey_sample.csv` – First input dataset  
- `survey_sample_2.csv` – Second input dataset  

---

## 🚀 How to Run Locally

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   streamlit run mental_health_dashboard_enhanced.py
   ```

3. Open your browser and go to `http://localhost:8501`.

---

## 🌍 How to Deploy (Online Access)

You can deploy this app on **Streamlit Cloud** to share with others via a link:

1. Push the files to a GitHub repository  
2. Visit [https://streamlit.io/cloud](https://streamlit.io/cloud)  
3. Log in with GitHub and create a new app  
4. Select your repo and main script: `mental_health_dashboard_enhanced.py`  
5. Click **Deploy** and share the link

> 🔗 Example: `https://yourusername.streamlit.app`

---

## 📁 Requirements

- Python 3.7+
- streamlit
- pandas
- seaborn
- matplotlib

---

## 💡 Reflection

This project demonstrates how building internal tools like dashboards can:
- Eliminate repetitive manual tasks (cleaning/merging)
- Provide **real-time insights** to stakeholders
- Encourage consistent data formatting
- Serve as scalable, maintainable internal solutions
