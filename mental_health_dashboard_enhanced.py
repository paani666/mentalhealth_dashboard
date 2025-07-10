
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🧠 Mental Health Survey Dashboard")
st.markdown("This dashboard visualizes mental health survey data from two merged datasets.")

# File upload
st.sidebar.header("Upload Your CSV Files")
file1 = st.sidebar.file_uploader("Upload survey_sample.csv", type="csv")
file2 = st.sidebar.file_uploader("Upload survey_sample_2.csv", type="csv")

def normalize_gender(g):
    g = str(g).lower().strip()
    if "male" in g:
        return "Male"
    elif "female" in g:
        return "Female"
    else:
        return "Other"

def load_and_prepare(file1, file2):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)
    df1["Gender"] = df1["Gender"].apply(normalize_gender)
    df2["Gender"] = df2["Gender"].apply(normalize_gender)
    df1.drop_duplicates(inplace=True)
    df2.drop_duplicates(inplace=True)
    df1.fillna("Unknown", inplace=True)
    df2.fillna("Unknown", inplace=True)

    common_cols = ["Gender", "Country", "self_employed", "family_history", "treatment", "mental_health_interview", "care_options"]
    merged = pd.merge(df1, df2, on=common_cols, how="inner")
    return merged

if file1 and file2:
    df = load_and_prepare(file1, file2)

    st.success("Files successfully merged and cleaned!")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎯 Treatment Distribution (Pie Chart)")
        treatment_counts = df['treatment'].value_counts()
        fig1, ax1 = plt.subplots()
        ax1.pie(treatment_counts, labels=treatment_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
        ax1.axis('equal')
        st.pyplot(fig1)

    with col2:
        st.subheader("🌍 Country Distribution (Top 10) - Horizontal Bar")
        top_countries = df['Country'].value_counts().head(10)
        fig2, ax2 = plt.subplots()
        sns.barplot(y=top_countries.index, x=top_countries.values, ax=ax2, palette="viridis")
        ax2.set_xlabel("Count")
        ax2.set_ylabel("Country")
        st.pyplot(fig2)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("📈 Age Distribution by Gender (Violin Plot)")
        fig3, ax3 = plt.subplots()
        sns.violinplot(data=df, x="Gender", y="Age", ax=ax3, palette="Set2")
        st.pyplot(fig3)

    with col4:
        st.subheader("⚖️ Mood Swings vs. Age (Strip Plot)")
        fig4, ax4 = plt.subplots()
        sns.stripplot(data=df, x="Mood_Swings", y="Age", ax=ax4, jitter=True, palette="coolwarm")
        st.pyplot(fig4)

    st.subheader("📉 Mental Health Consequence by Family History (Stacked Bar Approximation)")
    consequence_data = df.groupby(['family_history', 'mental_health_consequence']).size().unstack().fillna(0)
    fig5, ax5 = plt.subplots()
    consequence_data.plot(kind='bar', stacked=True, ax=ax5, colormap='Accent')
    ax5.set_ylabel("Count")
    st.pyplot(fig5)

else:
    st.info("Please upload both CSV files to generate the dashboard.")
