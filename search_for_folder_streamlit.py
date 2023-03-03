import pandas as pd
from re import search, IGNORECASE
import win32com.client as client
import streamlit as st
if st.checkbox('check here'):
    search_substring=st.text_input('input substring of the name of the folder, you will get folder paths')
    if st.button('check'):
        outlook= client.Dispatch('Outlook.Application')
        Folder =outlook.GetNameSpace('MAPI')
        #print(search_substring)
        #search_substring=str(input('input substring of the name of the folder, you will get folder paths\n'))


        # recursion function to check every subfolder
        def get_folder_path(Folder):
            for folder in Folder.Folders:
                if search(search_substring,(folder.name),IGNORECASE)==None:
                    pass
                else:
                    st.write(folder.folderpath)
            subfolder_count=Folder.Folders.Count
            if subfolder_count>0:
                for subfolder in Folder.Folders:
                    get_folder_path(subfolder)

        get_folder_path(Folder)
        st.write('search is finished')
        st.write('+++++++++++++++++++++')
        st.write('+++++++++++++++++++++')
        st.write('+++++++++++++++++++++')