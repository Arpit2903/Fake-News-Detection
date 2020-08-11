# Fake-News-Detection
* Fake news is an invention – a lie created out of nothing – that takes the appearance of real news with the aim of deceiving people. This project aims to classify the news as fake or real using the various ML models.

## Final Project
* Implemented Simple logistic regression, Random forest and Neural network to predict the news.
* Comparison of Accuracies for all the implemented models are as below:  
|----------------------------------------------------|    
| Machine learning model&nbsp;&nbsp;&nbsp;&nbsp;   	| Accuracy&nbsp;|  
|------------------------------------	|--------------|  
| Naive Bayes classifier&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| 72.12%&nbsp;&nbsp;&nbsp;&nbsp;|  
| Decision Tree classifier&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| 81.00%&nbsp;&nbsp;&nbsp;&nbsp;|  
| Logistic Regression&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| 90.32%&nbsp;&nbsp;&nbsp;&nbsp;|   
| Support Vector Machine&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| 91.36%&nbsp;&nbsp;&nbsp;&nbsp;|  
| Random forest&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| 81.58%&nbsp;&nbsp;&nbsp;&nbsp;|  
| Neural Network&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| 92.69%&nbsp;&nbsp;&nbsp;&nbsp;|  
|-----------------------------------------------------|  

## Milestone-2 
* To merge multiple datasets into one, run the following python script. Before running the script, specify the files configuration to be merged in the main.py
```
python main.py
```  
* Merged dataset contains the pre-Processed data which does not have
    - Missing/null values
    - Duplicate records
* Merged dataset is stored into noSQL database (MongoDB). Steps to store dataset into MongoDB are mentioned in the [dataset/README.md](https://github.com/Arpit2903/Fake-News-Detection/tree/master/dataset) 
* Before running various ML models, the data is pre-processed to:
    - Remove noisy/stopwords 
    - Converting news articles into Document vector for ML model
* Code for preprocessing the data and training the ML models is located in the notebook [fake_news_classification.ipynb](https://github.com/Arpit2903/Fake-News-Detection/blob/master/fake_news_classification.ipynb) 
* Train Machine learning models for news classification:
    - Reading data from mongoDB database
    - Splitting the dataset into training and test dataset
    - Training the models using Naive Baise, Support vector machine, Random forest
    - Comparing the accuracy of models

## Milestone-1
* Detailed information on [Milestone-1](https://github.com/Arpit2903/Fake-News-Detection/blob/master/Milestone1.pdf)