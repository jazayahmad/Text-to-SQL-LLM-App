from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from annotated_text import annotated_text
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Gemini Pro and get SQL query as responses
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    return response.text

## Funtion to retrive query from the SQL DB
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]
## Initiliaze Streamlit App
st.set_page_config(page_title="Retrieve any SQL query")
st.header("LLM App to Retrieve SQL Data")
input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input, prompt=prompt)
    annotated_text(" ",(response, "Query Generated", "#afa"),)
    response=read_sql_query(response,"student.db")
    st.subheader("Response: ")
    for row in response:
        print(row)
        st.header(row)