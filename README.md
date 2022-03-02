# EEGEyeExtension

- This is the Github Repo for the Brain-Computer Interfaces research conducted by Abdelrahman Abdelmonsef and Brian Xiang @ **Swarthmore college**. The repo is built upon the coding interface provided by EEGEyeNet repository: https://github.com/ardkastrati/EEGEyeNet. If you have your own ideas or want to understand the details of the code, you need to head to this repo and read README.md file explaining the general details. If you just want to reproduce our results, you can just follow the instructions below.
  
- First of all, your python enviroment should have the proper installations listed in these three files:\
  1- general_requirments.txt\
  2- standard_ml_requirments.txt\
  3- tensorflow_requirements.txt
  
- You can access the dataset used in these models through https://osf.io/ktv7m/. Make sure you download data from the folder named **Prepared**. For this task, you need to download the dots file only. Place these files in the folder named **Tasks**.

- Run the **TranslatingLR.py** using python. You should expect four additional files in the Tasks folder after running this code.

- To adjust the settings and determine the training and testing datasets, you can do this in the **config.py** file. The file is well commented and, hopefully, can guide you to what you need to change. By default, the testing and training will be done using the minimally preprocessed dots data. However, if you want to change the data to use, make sure you specify so through the config['dataset'] and config['preprocessing'] fields. **If you changed any of the two fields, make sure you have the corresponding data labelled correctly**.  

- Following this, you can now run **main.py** and wait for the results

 
