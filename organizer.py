'''
    Author: Keerthivasan S J

    Date: 20 October 2023
    
    These functionalities are created to be used in the 
    file_organiser_app.py
'''

import shutil
import os
def file_organizer(main_path:str):

    if main_path.endswith('/') or main_path.endswith('\\'):
        main_path=main_path.replace('\\','/')
    else:
        main_path=main_path.replace('\\','/')+'/'

    l=[f for f in os.listdir(main_path) if os.path.isfile(os.path.join(main_path, f))]
    
    for f in l:
        
        if f.endswith(".py"):
            if not os.path.exists(main_path+"Python files"):
                os.mkdir(main_path+"Python files")
                shutil.move(os.path.join(main_path, f),main_path+"Python files")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"Python files")
                

        elif f.endswith(".mp3"):
            if not os.path.exists(main_path+"Audios"):
                os.mkdir(main_path+"Audios")
                shutil.move(os.path.join(main_path, f),main_path+"Audios")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"Audios")
                 

        elif f.endswith(".docx"):
            if not os.path.exists(main_path+"Word documents"):
                os.mkdir(main_path+"Word documents")
                shutil.move(os.path.join(main_path, f),main_path+"Word documents")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"Word documents")
                
                       
        elif f.endswith(".pptx"):
            if not os.path.exists(main_path+"PPT files"):
                os.mkdir(main_path+"PPT files")
                shutil.move(os.path.join(main_path, f),main_path+"PPT files")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"PPT files")
                
                
        elif f.endswith(".xlsx"):
            if not os.path.exists(main_path+"EXCEL files"):
                os.mkdir(main_path+"EXCEL files")
                shutil.move(os.path.join(main_path, f),main_path+"EXCEL files")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"EXCEL files")
                
                
        elif f.endswith(".txt"):
            if not os.path.exists(main_path+"Text files"):
                os.mkdir(main_path+"Text files")
                shutil.move(os.path.join(main_path, f),main_path+"Text files")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"Text files")
                
                      
        elif f.endswith(".pdf"):
            if not os.path.exists(main_path+"Pdf files"):
                os.mkdir(main_path+"Pdf files")
                shutil.move(os.path.join(main_path, f),main_path+"Pdf files")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"Pdf files")
                
        
        elif f.endswith(".mkv") or f.endswith(".mp4"):
            if not os.path.exists(main_path+"Videos"):
                os.mkdir(main_path+"Videos")
                shutil.move(os.path.join(main_path, f),main_path+"Videos")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"Videos")
                
                
        elif f.endswith(".java"):
            if not os.path.exists(main_path+"Java files"):
                os.mkdir(main_path+"Java files")
                shutil.move(os.path.join(main_path, f),main_path+"Java files")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"Java files")
                

        elif f.endswith(".csv"):
            if not os.path.exists(main_path+"Csv files"):
                os.mkdir(main_path+"Csv files")
                shutil.move(os.path.join(main_path, f),main_path+"Csv files")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"Csv files")
                

        elif f.endswith(".exe"):
            if not os.path.exists(main_path+"Applivation files"):
                os.mkdir(main_path+"Applivation files")
                shutil.move(os.path.join(main_path, f),main_path+"Applivation files")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"Applivation files")
                
            
        elif f.endswith(".css"):
            if not os.path.exists(main_path+"Css files"):
                os.mkdir(main_path+"Css files")
                shutil.move(os.path.join(main_path, f),main_path+"Css files")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"Css files")
                
                
        elif f.endswith(".htm") or f.endswith(".html"):
            if not os.path.exists(main_path+"Html files"):
                os.mkdir(main_path+"Html files")
                shutil.move(os.path.join(main_path, f),main_path+"Html files")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"Html files")
                

        elif f.endswith(".png") or f.endswith(".jpg"):
            if not os.path.exists(main_path+"Photos"):
                os.mkdir(main_path+"Photos")
                shutil.move(os.path.join(main_path, f),main_path+"Photos")
            else:
                shutil.move(os.path.join(main_path, f),main_path+"Photos")
                
               
