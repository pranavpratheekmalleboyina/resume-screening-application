import streamlit as st
import pickle 
import re
import nltk

#dependencies
nltk.download("punkt")
nltk.download("stopwords")

def cleanup(text):
    cleaned_text = re.sub('http\S+s*', ' ', text)
    cleaned_text = re.sub('RT|cc', ' ', cleaned_text)
    cleaned_text = re.sub('#\S*', ' ', cleaned_text)
    cleaned_text = re.sub('@\S*', ' ', cleaned_text)
    cleaned_text = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleaned_text)
    cleaned_text = re.sub('\s+', ' ', cleaned_text)
    cleaned_text = re.sub(r'[\x00-\x7f]', r' ', cleaned_text)
    return cleaned_text

#web app
def main(): 
   st.title("Resume Screening application")
   file_uploaded = st.file_uploader("Please upload your resume here",type=['txt', 'pdf'])
   
   if file_uploaded is not None:
       try:
           resume_bytes = file_uploaded.read()
           resume_text = resume_bytes.decode('utf-8')
       except UnicodeDecodeError:    
           resume_text = resume_bytes.decode('latin1')
       cleaned_resume = cleanup([resume_text])      
   
if __name__ == "__main__":
    main()   


