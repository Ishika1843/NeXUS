import base64
from readline import insert_text
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import io
import base64
import google.generativeai as genai
from PIL import Image
import pdf2image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])
def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response
#streamlit app
st.set_page_config(page_title="Lets have some question and answers with each other")
st.header("Gemini LLM Application based")
if "🔎 chat_history 🔍" not in st.session_state:
        st.session_state["🔎 chat_history 🔍"]=[]
        input=st.text_input("Input:",key="input")
        submit=st.button("🤗 answer question please🤗 ")
        if submit and input:
            response=get_gemini_response(input)
            st.session_state['🔎 chat_history 🔍'].append(("You",input))
            st.subheader("The Response is")
            for chunk in response:
                st.write(chunk.text)
                st.session_state["🔎 chat_history 🔍"].append(("Bot",chunk.text))
                st.subheader("'🔎  ✍🏻Your chat history✍🏻  is 🔍'")
                for role,text in st.session_state['🔎 chat_history 🔍']:
                    st.write(f"{role}:{text}")
                    def get_gemini_response(input,pdf_content,prompt):
                        model=genai.GenerativeModel('gemini-pro-vision')
                        response=model.generate_content([input,pdf_content[0],prompt])
                        return response.text
                    def input_pdf_setup(uploaded_file):
                        if uploaded_file is not None:
                            ## pdf to image
                            images =pdf2image.convert_from_bytes(uploaded_file.read())
                            first_page=images[0]
                            img_byte_arr = io.BytesIO()
                            first_page.save(img_byte_arr, format='JPEG')
                            img_byte_arr = img_byte_arr.getvalue()
                            pdf_parts = [
                                {
                                     "mime_type": "image/jpeg",
                                     "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
                                     }
                                     ]
                            return pdf_parts
                        else:
                            raise FileNotFoundError("No file uploaded")
 #streamlit for pdf stuff
st.header("😎 ATS COLLEGE APPLICATION EXPERT 😎")
st.subheader("ATS Tracking system")
uploaded_file=st.file_uploader("Upload your college application in PDF format",type=["pdf"])
if uploaded_file is  not None:
    st.write("PDF Uploaded Successfully")
    submit1=st.button("Tell me about the College Application")
    submit2 = st.button("Percentage match")
    input_prompt1 = """ You are an experienced Technical Human Resource Manager,your task is to review the provided college application against the college description. Please share your professional evaluation on whether the candidate's profile aligns with the college requirements. 
            Highlight the strengths and weaknesses of the applicant in relation to the specified college requirements."""
    input_prompt2 = """You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, your task is to evaluate the resume against the provided college application description. give me the percentage of match if the application matches the college description. First the output should come as percentage and then keywords missing and last final thoughts."""
    if submit1:
        if uploaded_file is not None:
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response(input_prompt1,pdf_content,insert_text)
            st.subheader("The Repsonse is")
            st.write(response)
        else:
            st.write("Please uplaod the resume")
    elif submit2:
        if uploaded_file is not None:
            pdf_content=input_pdf_setup(uploaded_file)
            response=get_gemini_response(input_prompt2,pdf_content,insert_text)
            st.subheader("The Repsonse is")
            st.write(response)
    else:
        st.write("Please uplaod the resume")
