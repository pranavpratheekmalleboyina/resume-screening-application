import streamlit as st
import pickle 
import re
import nltk

#dependencies
nltk.download("punkt")
nltk.download("stopwords")

#web app
def main(): 
   st.title("Resume Screening application")
   st.file_uploader("Please upload your resume here",type=['txt', 'pdf'])
   
if __name__ == "__main__":
    main()   


