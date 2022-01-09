import requests
import pyautogui
import streamlit as st
st.header("The Problem of Evil")
st.subheader("This demo uses different ML models to help people think about different shapes of the future.")
st.text_input()

def finish_text():
    text = input()
    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": "Bearer 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"}
    payload = (text)
    response = requests.post(API_URL, headers=headers, json=payload)
    press_tab()
    st.write(response.json())
    
def press_tab():
    new_text()

def new_text():
    text = ""

if pyautogui.press('tab'):
    finish_text()
    press_tab()

