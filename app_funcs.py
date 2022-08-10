import os
import zlib
import shutil
import zipfile
import streamlit as st
import subprocess as sp

zip_path = "compressed/"

@st.cache(persist=True,allow_output_mutation=False,show_spinner=True,suppress_st_warning=True)
def clean_directory(dir):
    shutil.rmtree(dir)
    os.makedirs(dir)

@st.cache(persist=True,allow_output_mutation=False,show_spinner=True,suppress_st_warning=True)
def get_all_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def compress():
   directory = './output'
   file_paths = get_all_file_paths(directory)

   print('Following files will be zipped:')
   for file_name in file_paths:
      print(file_name)

   with zipfile.ZipFile(zip_path + 'OCR_PDFs.zip','w') as zip:
      for file in file_paths:
         zip.write(file)
   print('All files zipped successfully!')


@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def download_success():
    st.balloons()
    st.success('✅ Download Successful !!')
