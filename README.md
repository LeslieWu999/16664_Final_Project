# 16664_Final_Project

This is the final project of Team XYZ, which is using deep neural networks for vehicle classification.

The dataset is given in link: https://drive.google.com/drive/u/1/folders/1mun_jxWNdAyxGvi6E0qUBH_wRFaMD24q.

After downloading trainval, test folder, the code in the main branch of this repository and model_our.pth in the master branch of this repository, the fold structure is as follows: 

.
│  
└─trainval  
└─test  
└─extract_info.py  
└─test.py  
└─16664_Project_0_52_final.ipynb  
└─classes.csv  
└─model_our.pth  

First, the path variable in extract_info.py and test.py should be changed to the corresponding trainval/test folder path in your environment, and the guid path should be changed to the root path of the whole project. By running these two codes, trainval_labels.csv and test_labels.csv, which indicate the training and testing img path will be generated for further use.

Then for the model part, you can refer to the 16664_Project_0_52_final.ipynb file, since we use colab and google drive the train the model, the path is set for the google drive, you can change it to your own path.  

If you want to train a new model from the scrach, you can run the whole code from the beginning, and don't forget to change the path.  

If you want to test the model we trained, you can just start from the following code:  
![pretrained](https://user-images.githubusercontent.com/113010716/235412794-4f6373eb-4d42-4253-bdfa-c11ca9952fa9.PNG)



After that, the result.csv of the target format will be generated.
