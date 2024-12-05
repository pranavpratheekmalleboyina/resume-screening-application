import streamlit as st
import pickle 
import re
import nltk

#dependencies
nltk.download("punkt")
nltk.download("stopwords")

#loading the models
tfidf = pickle.load(open('tfidf.pkl','rb'))
clf = pickle.load(open('clf.pkl','rb'))

def cleanup(text):
    cleaned_text = re.sub(r'http\S+\s', ' ', text)
    cleaned_text = re.sub(r'RT|cc', ' ', cleaned_text)
    cleaned_text = re.sub(r'#\S+\s', ' ', cleaned_text)
    cleaned_text = re.sub(r'@\S+', ' ', cleaned_text)
    special_characters = re.escape(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""")
    pattern = rf"[{special_characters}]"
    cleaned_text = re.sub(pattern, ' ', cleaned_text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)
    cleaned_text = re.sub('[^\x00-\x7f]', ' ', cleaned_text)
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
       #st.write(resume_text)    
       cleaned_resume = cleanup(resume_text)     
       input_features = tfidf.transform([cleaned_resume]) 
       prediction_id = clf.predict(input_features)[0]
       
       category_mapping = {
        15: "Java Developer",
        23: "Testing",
        8 : "Devops Engineer",
        20 : "Python Developer",
        24: "Web Designer",
        12 : "HR",
        13: "Hadoop",
        3 : "Blockchain",
        10:"ETL Developer",
        18: "Operations Manager",
        6 : "Data Science",
        22: "Sales",
        16: "Mechanical Engineer",
        1:"Art",
        7:"Database",
        8:"Electric Engineer",
        14:"Health and Fitness",
        19:"PMO",
        4:"Business Analyst",
        9:"dotnet developer",
        2:"Automation tester",
        17:"Network Security Engineer",
        21:"SAP Developer",
        5:"Civil Engineer",
        0:"Advocate"
 }

       category_name = category_mapping.get(prediction_id,"unknown")
       st.write(f"The category is {category_name}")
       #st.write(f"The prediction id is {prediction_id}") 
       
if __name__ == "__main__":
    main()   


