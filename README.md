# AI Test Case Generator using LLM

An AI-powered application that automatically generates software test cases and Selenium automation scripts from software requirements using a Large Language Model (LLM).

This tool helps QA engineers quickly create test cases and automation scripts, reducing manual effort in the testing process.

---

## Features

- Generate test cases automatically from requirements
- Output in structured table format
- Export test cases to CSV
- Generate Selenium Python automation scripts
- Simple UI built with Streamlit
- Uses local LLM via Ollama (Mistral model)

---

## Tech Stack

- Python
- Streamlit
- LangChain
- Ollama
- Mistral LLM
- Selenium
- Pandas

---

## Project Architecture

User Requirement Input  
↓  
Streamlit UI  
↓  
LangChain Prompt Processing  
↓  
LLM (Mistral via Ollama)  
↓  
Generated Test Cases / Selenium Script  
↓  
Download as CSV or Python File

---

## Installation

Clone the repository:

git clone https://github.com/Chetu1993/ai-testcase-generator-llm.git
cd ai-testcase-generator-llm

## Install dependencies:
```
pip install -r requirements.txt
```
## Install and start Ollama:
```
Install and start Ollama:
```
## Run the Application
Start the Streamlit app:
```
streamlit run app.py
```
Open in browser:
```
http://localhost:8501
```
## Example Input
Requirement:
Search functionality in Amazon website where user can search products.

Example Output
```
| Test Case ID | Test Scenario                  | Test Steps                          | Expected Result                 |
| ------------ | ------------------------------ | ----------------------------------- | ------------------------------- |
| TC_01        | Verify search box availability | Open Amazon homepage                | Search box should be visible    |
| TC_02        | Verify product search          | Enter product name and click search | Relevant products should appear |

```

## Selenium Script Generation
The system also generates Python Selenium scripts automatically for the given requirements.

Example:
```
driver.find_element(By.ID,"twotabsearchtextbox").send_keys("laptop")
```

## Author
## Chetan Kumar

## GitHub:
## https://github.com/Chetu1993
