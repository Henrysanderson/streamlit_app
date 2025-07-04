
# Streamlit App for Salary Data Analysis
# This app allows you to upload a salary dataset and visualize various insights using interactive charts.
# It uses pandas for data manipulation, seaborn/matplotlib for plotting, and Streamlit for the web interface.

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# App Title
st.title("Streamit App Project")
st.write("""
Welcome! This Streamlit app lets you explore and visualize salary data. You can upload your own CSV file or use the default dataset provided. The app will guide you through data cleaning, exploration, and visualization steps to help you gain insights into salary trends by gender, education, experience, and more.
""")


# File uploader for flexibility
# st.markdown("**Step 1: Upload your Salary Data CSV file (or use the default dataset)**")
# uploaded_file = st.file_uploader("Upload Salary Data CSV", type=["csv"])
# if uploaded_file is not None:
#     df = pd.read_csv(uploaded_file)
#     st.success("File uploaded successfully!")
# else:
#     df = pd.read_csv("./Salary_Data.csv")
#     st.info("Using default Salary_Data.csv from the project folder.")

df = pd.read_csv(uploaded_file)
# Exploratory Data Analysis Section
st.header("Exploratory Data Analysis")
st.write("Let's take a look at the data and perform some basic cleaning and exploration.")


# Show the first 10 rows
st.subheader("First 10 Rows of Data")
st.write("Previewing the first 10 rows of the dataset:")
st.dataframe(df.head(10))


# Clean up the 'Education Level' column for consistency
df['Education Level'] = df['Education Level'].replace("Bachelor's degree", "Bachelors")
df['Education Level'] = df['Education Level'].replace("Master's degree", "Masters")


# Show unique values in the Gender column
st.subheader("Unique Genders")
st.write("These are the unique gender values present in the dataset:")
st.write(df['Gender'].unique())


# Check for missing values and drop them
st.subheader("Missing Values Before Cleaning")
st.write("Number of missing values in each column before cleaning:")
st.write(df.isnull().sum())
df = df.dropna()
st.subheader("Missing Values After Cleaning")
st.write("Number of missing values in each column after dropping rows with missing data:")
st.write(df.isnull().sum())


# Show dataset shape and data types
st.subheader("Dataset Shape")
st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")
st.subheader("Data Types")
st.write("Data types of each column:")
st.write(df.dtypes)


# Visualize Salary Distribution
st.subheader("Salary Distribution")
st.write("This histogram shows the distribution of salaries in the dataset.")
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df['Salary'], kde=True, bins=20, ax=ax)
ax.set_title('Salary Distribution')
ax.set_xlabel('Salary')
ax.set_ylabel('Frequency')
st.pyplot(fig)


# Visualize Average Salary by Gender
st.subheader("Average Salary by Gender")
st.write("This bar chart displays the average salary for each gender.")
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x='Gender', y='Salary', data=df, estimator=np.mean, ax=ax)
ax.set_title('Average Salary by Gender')
ax.set_xlabel('Gender')
ax.set_ylabel('Average Salary')
st.pyplot(fig)


# Further clean the Education Level column for consistency
education_mapping = {
    "Bachelor's": "Bachelor's Degree",
    "Master's": "Master's Degree",
    "PhD": "PhD",
    "High School": "High School",
    "phD": "PhD"
}
df['Education Level'] = df['Education Level'].replace(education_mapping)


# Visualize Average Salary by Education Level
st.subheader("Average Salary by Education Level")
st.write("This chart shows the average salary for each education level.")
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Education Level', y='Salary', data=df, estimator=np.mean, ax=ax)
ax.set_title('Average Salary by Education Level')
ax.set_xlabel('Education Level')
ax.set_ylabel('Average Salary')
plt.xticks(rotation=45)
st.pyplot(fig)


# Visualize Salary vs Years of Experience
st.subheader("Salary vs Years of Experience")
st.write("This scatter plot with a trend line shows how salary relates to years of experience.")
fig, ax = plt.subplots(figsize=(10, 6))
sns.regplot(x='Years of Experience', y='Salary', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'}, ax=ax)
ax.set_title('Salary vs Years of Experience')
ax.set_xlabel('Years of Experience')
ax.set_ylabel('Salary')
st.pyplot(fig)


# Visualize Gender Distribution by Education Level
st.subheader("Gender Distribution by Education Level")
st.write("This count plot shows the distribution of genders across different education levels.")
fig, ax = plt.subplots(figsize=(10, 6))
sns.countplot(x='Education Level', hue='Gender', data=df, ax=ax)
ax.set_title('Gender Distribution by Education Level')
ax.set_xlabel('Education Level')
ax.set_ylabel('Count')
ax.legend(title='Gender')
st.pyplot(fig)


# Visualize Age vs Salary
st.subheader("Age vs Salary")
st.write("This scatter plot shows the relationship between age and salary.")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Age', y='Salary', data=df, ax=ax)
ax.set_title('Age vs Salary')
ax.set_xlabel('Age')
ax.set_ylabel('Salary')
st.pyplot(fig)


# Visualize Top 10 Paying Jobs
st.subheader("Top 10 Paying Jobs")
st.write("This horizontal bar chart displays the 10 job titles with the highest average salaries in the dataset.")
top_paying_jobs = df.groupby('Job Title')['Salary'].mean().sort_values(ascending=True).head(10)
fig, ax = plt.subplots(figsize=(10, 6))
top_paying_jobs.plot(kind='barh', color='skyblue', ax=ax)
ax.set_title('Top 10 Paying Jobs')
ax.set_xlabel('Average Salary')
ax.set_ylabel('Job Title')
st.pyplot(fig)
