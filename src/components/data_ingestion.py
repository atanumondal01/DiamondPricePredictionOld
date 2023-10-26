import os #for creating path to store output 
import sys  #for logging and exception
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#data ingestion will do the splitting 
#output will be in train and test files

## intialize the data ingestion configuration


##we need to give train and test path to our data ingestion
#data ingestion gives the train and test data as output

@dataclass
class DataIngestionconfig:#u can use init but would be lengthy
    train_data_path=os.path.join('artifacts','train.csv')
    test_data_path=os.path.join('artifacts','test.csv')
    raw_data_path=os.path.join('artifacts','raw.csv')

  #data is saved in artifacts as train.csv

## create a data ingestion class
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method starts')

        try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            #this will make the artifacts folder if not exist
            #folder laction self.ingestion_config.raw_data_path
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
             #for raw.csv
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Raw data is getting created")

            logging.info("Train test split")
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)
            #doing this cause we want train and test data to be seperate file
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )

        except Exception as e:
            logging.info('Error occured in Data Ingestion config')
            raise CustomException(e,sys)







