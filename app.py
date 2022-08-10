import re
import time
import datetime
import pandas as pd
from PIL import Image
import streamlit as st
from app_funcs import *

st.set_page_config(
    page_title="Scanned PDFs Checker",
    page_icon="📄",
    layout="centered",
    initial_sidebar_state="auto",
)

main_image = Image.open('static/main_banner.png')

input_path = "input/"
output_path = "output/"
zip_path = "compressed/"

total_docs = 0

scanned_docs_df = pd.DataFrame(columns = ['File Name'])
digital_docs_df = pd.DataFrame(columns = ['File Name'])

clean_directory(input_path)
clean_directory(output_path)
clean_directory(zip_path)

st.image(main_image,use_column_width='auto')
st.title("📑📝 Scanned PDFs checker 📄👨‍💻")
st.info('✨ Checks for the number of scanned/digitally created PDFs from a corpus of PDF documents.😉')
st.info('☢ The app\'s execution time may vary depending on the size/number of the uploaded PDFs.')

uploaded_files = st.file_uploader("Upload PDFs 🚀", type=["pdf"], accept_multiple_files=True)
with st.spinner(f"Working... 💫"):
   if uploaded_files:
      for uploaded_file in uploaded_files:
         with open(os.path.join(input_path,uploaded_file.name),"wb") as f:
            f.write((uploaded_file).getbuffer())

      for file_name in os.listdir(input_path):
         print("-"*40)
         print("Checking: ", file_name)
         start_time = time.time()
         output_file_name = "OCRed_"+file_name
         output = sp.getoutput(f"ocrmypdf {input_path}{file_name} {output_path}{output_file_name}")
         if not re.search("PriorOcrFoundError: page already has text!",output):
            print("--- Uploaded scanned PDF ---")
            scanned_docs_df = scanned_docs_df.append({'File Name' : file_name},ignore_index = True)
         else:
            print("---Uploaded digital PDF ---")
            digital_docs_df = digital_docs_df.append({'File Name' : file_name},ignore_index = True)
         print("Processing complete..")
         print("Time Taken: ", round(time.time() - start_time, 2), " seconds")
         total_docs+=1

      col1, col2 = st.columns(2)
      col1.metric("# Scanned PDFs", len(scanned_docs_df))
      col2.metric("# Digital PDFs", len(digital_docs_df))
      with col1:
         st.markdown("<br>", unsafe_allow_html=True)
         st.write("List of Scanned PDFs 📝")
         st.dataframe(scanned_docs_df)
      with col2:
         st.markdown("<br>", unsafe_allow_html=True)
         st.write("List of Digital PDFs 📝")
         st.dataframe(digital_docs_df)

      if len(scanned_docs_df) > 0:
         check = st.checkbox("Do you want me to perform OCR for the scanned PDFs? 🤔")
         if check:
            print("Generating Zip...")
            compress()
            with open(zip_path + 'OCR_PDFs.zip', "rb") as file:
               if st.download_button(
                                      label="Download Zip file of OCRed PDFs 📑",
                                      data=file,
                                      file_name='OCR_PDFs.zip',
                                      mime='application/zip'
                                   ):
                  download_success()

   else:
      st.warning('⚠ Please upload your corpus of PDFs! 😯')


st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=Scanned PDFs Checker WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a>✨</center><hr>", unsafe_allow_html=True)

st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
