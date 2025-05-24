# Setting up a continuous training pipeline using Apache Airflow, FastAPI, Flask, and Docker

This project demonstrates the setup of a continuous training pipeline for machine learning models using Apache Airflow, FastAPI, Flask, and Docker. The project operates on a tabular dataset [Diabetes Data Set](https://www.kaggle.com/datasets/mathchi/diabetes-data-set) from Kaggle.

![image](https://github.com/ghm-group/continuous-training-pipeline-airflow/assets/153216815/91f22331-8a13-4987-a5c1-1a2ebefbcae5)

## Installations

Use the folder of the docker given in the repository above:

```bash
docker compose up -d
```
Once you run the compose, you'll find the container in your docker desktop.

Some of the packages you'll need to install are :

```bash
pip install scikit-learn
pip install pycaret
pip install xgboost
```

If you find some problems related to pycaret package, do check the following link :
[PyCaret](https://github.com/pycaret/pycaret).

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/ghm-group/continuous-training-pipeline-airflow.git
    cd projetDiabetes
    ```
    once you're there, you can see the project structure perfectly.
   
2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
    Make sure you have all the packages running.

3. Preprocess the data:

    The file Diabetes.ipynb contains all necessary informations regarding data processing and also models comparision. 
    the plots and graphes displays the data quality and also the models performances. For any information do check the pdf file 
    provided within the repository.

4. Results :

    * Model Training : 

    in this part we used Zeppelin notebook to compare data, you can use any IDE or program that can handle python or has a python interpretor:

    For example : here we can test the outliers
    ![image](https://github.com/ghm-group/continuous-training-pipeline-airflow/assets/153216815/f947d1e6-0d88-4553-8a53-458d589fc814)

    And here we can see the performances:

    ![image](https://github.com/ghm-group/continuous-training-pipeline-airflow/assets/153216815/1ded2cb3-380d-4ee1-91d2-0f3263aa7551)

    * Fast API testing : 

    Run the following command:
    
    ```bash
    uvicorn APITask:app --reload
    ```


    We enter some random variables to test : 
    
    ![image](https://github.com/ghm-group/continuous-training-pipeline-airflow/assets/153216815/772ca30c-6980-40c2-908f-9ba7dd77ddb3)


    * Airflow : 
    ![image](https://github.com/ghm-group/continuous-training-pipeline-airflow/assets/153216815/b03d6334-9402-4a3a-aa89-cd20f79d7595)

    the code of this part is provided in the dags folder inside projetDiabetes, once we run the dag this appears in Airflow Interface:

   ![image](https://github.com/ghm-group/continuous-training-pipeline-airflow/assets/153216815/29310216-3085-4151-aabc-99f41d76280f)


    * Flask project : 

    Flask Application is the one in the folder :
   ![image](https://github.com/ghm-group/continuous-training-pipeline-airflow/assets/153216815/8750ee61-9354-4200-a28b-242a5001fa4e)


    1St thing that will appear is :
    ![image](https://github.com/ghm-group/continuous-training-pipeline-airflow/assets/153216815/436830fd-1aa7-494e-806f-eac5dc06fad8)


    We enter random values to test as following:
    ![image](https://github.com/ghm-group/continuous-training-pipeline-airflow/assets/153216815/279c7389-d122-4209-9469-4ecb3b67f322)



    the result is this:
    ![image](https://github.com/ghm-group/continuous-training-pipeline-airflow/assets/153216815/6a83ff45-cfc9-40f4-9ba9-13b65264c84a)





## Collaborators : 

The contributors for this project:

- [LAYOUNE Ghita](https://github.com/Bam04bi)
- [HANIM Hanae](https://github.com/hhanae)
- [YOUSFI Meryem](https://github.com/MeryemYOUSFI15)
