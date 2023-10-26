import os#for creating path to store output 
import sys #for logging and exception
from src.logger import logging
from src.exception import CustomException

import pandas
from sklearn.model_selection import train_test_split

#data ingestion will do the splitting 
#output will be in train and test files

#we need to give train and test path to our data ingestion
from dataclasses import dataclass

#data ingestion gives the train and test data as output
@dataclass
class dataIngestionconfig:#u can use init but would be lengthy
    train_data_path:str=os.path.join("artifacts","train.csv")
    #data is saved in artifacts as train.csv
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","raw.csv")

class dataIngestion:
    def __init__(self):
        self.ingestion__config=dataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion starts")    

    try:
            df=pd.read_csv(os.path.join('notebooks/data','gemstone.csv'))
            logging.info('Dataset read as pandas Dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False)

            logging.info("Train test split")
            train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )            
    except Exception as e:
        logging.info("Exception occured at Igestion step")    
        raise CustomException(e,sys)
    #sys has system default exeption