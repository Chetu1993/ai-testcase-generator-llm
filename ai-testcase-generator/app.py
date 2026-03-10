from langchain_ollama import ChatOllama
import streamlit as st
import pandas as pd

llm=ChatOllama(model="mistral:latest",base_url="http://localhost:11434")
st.title("AI testcase generator")
requirement=st.text_area("enter software requirements")

if st.button("Generate test cases"):
    prompt=f"""generate software testcases for the following requirements:

Return ONLY a table using this exact format:
Test Case ID | Test Scenario | Test Steps | Expected Result
Rules:
- Exactly 4 steps
- use "|" as seperator
- do not add extra "|" inside cells
- do not add markdown seperators like |----|
Do not include explanations.
Requirement:
{requirement}

"""
    response=llm.invoke(prompt)
    st.write(response.content)
    lines=response.content.split("\n")
    rows=[]
    for line in lines:
        if "|" in line:
            rows.append([col.strip() for col in line.split("|")])

    if len(rows)>1:
        df=pd.DataFrame(rows[1:],columns=rows[0])
    else:
        df=pd.DataFrame({"Output":[response.content]})
    csv=df.to_csv(index=False)
    st.download_button("Download Test cases",data=csv,file_name="testcases.csv",mime="text/csv")



if st.button("Generate selenium scripts automation"):
    prompt=f"""write the python selenium script for the below requirement
{requirement}:
- Use selenium 4
- webdriver-manager
- Proper imports
- Explicit Waits
- Comments"""

    response=llm.invoke(prompt)
    st.write(response.content)
    st.session_state.selenium_script = response.content
if "selenium_script" in st.session_state:
    st.code(st.session_state.selenium_script, language="python")
    st.download_button("Download selenium script",data=st.session_state.selenium_script,file_name="selenium_script.py",mime="text/plain")
