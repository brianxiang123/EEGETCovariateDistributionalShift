# EEGETCovariateDistributionalShift

This is the Github Repo for the data processing step for the research done in Vector-Based Data Improves Left-Right
Eye-Tracking Classifier Performance After a Covariate Distributional Shift by Brian Xiang and Abdelrahman Abdelmonsef @ **Swarthmore College**. 

## Downloading the datasets

1. Navigate to https://osf.io/ktv7m/. 
2. On the left, you will find two folders, the first of which is named "Dropbox: EEGEyeNet." If this first folder has a (+) sign next to it, click on the (+) sign. Otherwise, go to the next step directly. 
3. Four folders should pop up. Open the folder named **Prepared** (Click the + sign next to the folder named "prepared"). 
4. Scroll until you see four files that start with "LR_task_with."
5. Download the second to last one to your device ('LR_task_with_antisaccade_synchronised_min.npz').
6. Scroll until you see eight files that start with "Direction_task_with."
5. Download the third one to your device ('Direction_task_with_dots_synchronised_min.npz').
7. Place the downloaded datasets into the folder named **Tasks**.

## Python Requirements

Verify that your python environment contains proper installations for the three files listed below:\
1. general_requirments.txt\
2. standard_ml_requirments.txt\
3. tensorflow_requirements.txt

## Data Processing

1. Run **TranslatingLR.py**. You should now have a file called 'LR_task_with_dots_synchronised_min.npz' in the **Tasks** folder.
2. The remaining code is built upon the coding interface provided by the EEGEyeNet repository: https://github.com/ardkastrati/EEGEyeNet. A detailed explanation of the interface is provided there. 
3. Adjust the **config.py** file to select training and testing datasets. NOTE: By default, the testing and training will be done using the minimally preprocessed dots data (large grid paradigm). However, if you want to change the data to use, make sure you specify so through the config['dataset'] and config['preprocessing'] fields. **If you changed any of the two fields, make sure you have the corresponding data labeled correctly**.  
4. By default, specifying the training set also uses the same dataset as the testting set. To create a covariate distributional shift, first train models using one dataset and then set config['retrain'] = False and specify the location of the trained models with config['load_experiment_dir'] (the models should be under a folder named 'runs')
5. Once the training and testing datasets have been determined, run **main.py** and wait for the results.

If you have any comments or suggestions, you can contact us at bxiang1@swarthmore.edu and/or ayahia1@swarthmore.edu.


 
