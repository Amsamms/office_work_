required_folder_path=r'\\Personal Folders\Inbox\U-25\Precommessioning activities'
saving_path = r'D:\attachements_trial'
import pandas as pd
import os
from re import search, IGNORECASE
import win32com.client as client
outlook= client.Dispatch('Outlook.Application')
Folder =outlook.GetNameSpace('MAPI')

# converting the givven path to win32.

split= required_folder_path.split('\\')[2:]
processed_folder='final_folder=Folder.'

for i, f in enumerate(split):
    processed_folder = processed_folder + 'Folders[split[' + str(i) + "]]."

processed_folder=processed_folder[:-1]
exec(processed_folder)





# doing recursion to get all massages in allsubfolders of final_folder
massages=[]
def get_massages(folder):
    '''
    recrusievly search for all folders and subfolders of mail to find all massege items inside and adding them to a list
    '''
    for massage in folder.items:
        massages.append(massage)
        
    #check for subfolder (base case)
    subfolder_count=folder.Folders.Count
    
    #search all subfolders
    if subfolder_count>0:
        for subfolder in folder.Folders:
            massages.append(get_massages(subfolder))
    return massages

get_massages(final_folder)

# gettng attachements from the specefic folder

for massage in massages:
    try:
        print(massage.Subject)
        for attachment in massage.Attachments:
            try:
                print(f'saving "{attachment.FileName}" to {saving_path}')
                attachment.SaveAsFile(os.path.join(saving_path, str(attachment.FileName))) 
            except:
                print(f'some files could not be saved, {massage}')
                continue
        print('****************************')
    except:
        print(massage)
        continue
