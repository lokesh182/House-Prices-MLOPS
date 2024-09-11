import os
import zipfile
from abc import ABC,abstractmethod

import pandas as pd


#define an abstract class

class DataIngestor(ABC):
    @abstractmethod
    def ingest(self,file_path: str) -> pd.DataFrame:
        """
        Abstarct Method to ingest data from a given file
        """
        pass
    
    #implement a concrete class for ZIP Ingestion
class ZipDataIngestor(DataIngestor):
        def ingest(self,file_path: str) -> pd.DataFrame:
            """extracts a .zip file and returns the content as a pandas Dataframe"""
            #Ensure the file is a .zip file
            if not file_path.endswith(".zip"):
                raise ValueError("The Provided File is not a .zip file")
            
            #Extract the zip file
            with zipfile.ZipFile(file_path,"r") as zip_ref:
                #Extract all the files
                zip_ref.extractall("extracted_data")
            
            #Find the extracted CSV file (assuming there is one CSV file inside the zip)
            extracted_files = os.listdir("extracted_data")
            csv_files = [f for f in extracted_files if f.endswith(".csv")]
            
            if len(csv_files) == 0:
                raise FileNotFoundError("No CSV file found in the extracted files")
            if len(csv_files) > 1:
                raise ValueError("Multiple CSV files found in the extracted files")
            
            csv_file_path = os.path.join("extracted_data",*csv_files)
            df = pd.read_csv(csv_file_path)
            
            return df
        
            #Implement a concrete class for CSV Ingestion
class DataIngestorFactory(DataIngestor):
    @staticmethod
    def get_data_ingestor(file_extension: str) -> DataIngestor:
        """Returns the appropriate DataIngestor based on the file extension"""
        
        if file_extension == ".zip":
            return ZipDataIngestor()
        
        else:
            raise ValueError(f"No ingestor available for file extension:{file_extension}")
            
            
            
if __name__ == "__main__":
    file_path = "/home/lokesh18/House-Prices-MLOPS/data/archive.zip"
    file_extension = os.path.splitext(file_path)[1]
    
    data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    
    df = data_ingestor.ingest(file_path)
    
    print(df.head())