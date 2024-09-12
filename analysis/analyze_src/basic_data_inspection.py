from abc import ABC, abstractmethod
import pandas as pd


#Abstract class for Data Inspection Strategires
#This class defines a comman interface for data inspection startegy
#subclasses must implement the isnpect method


class DataInspectionStrategy(ABC):
    @abstractmethod
    def inspect(self,df: pd.DataFrame):
        '''
        Perform a specific type of data inspection
        
        
        Parameters:
        df (pd.DataFrame): The data frame on which the inspection is performed
        
        Returns:
        None: This method prints the inspection results directly
        '''
        pass
    
    




class DataInspectionStrategy(DataInspectionStrategy):
    def inspect(self,df: pd.DataFrame):
        '''
        Inspects and prints the data types and non null counts of
        
        Parameters:
        df(pd.Dataframe): The Dataframe to be inspected
        
        '''
        
        print("Data Types and Non-Null Counts")
        print(df.info())
        
    
class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df:pd.DataFrame):
        """
        Prints Summary Statistics for numerical and categorical features
        
        Parameters:
        df(pd.DataFrame): The Dataframe to be inspected
        
        Returns:
        None: Prints summary statistics to the console
        
        """  
        print("\nSummary Statistics (Numeircal Features")
        print(df.describe())
        print("\n Summary Statistics (Categorical Features)")
        print(df.describe(include = ["0"]))
        

# Context Class that uses a DataInspectionStrategy
# -------------------------------------------------
# This class allows you to switch between different data inspector strategies

class DataInspector:
    def __init__(self, strategy:DataInspectionStrategy):
        
        self._strategy = strategy
        """
        Initializes the DataInspector with a specific inspection
        
        Parameters:
        strategy (DataInspectionStrategy): The Strategy to be used
        
        Returns:
        None
       """
    
    def set_strategy(self,strategy: DataInspectionStrategy):
        """
        Sets a new strategy for the DataInspector
        
        Parameters:
        startegy: DataInspectionStrategy
        
        Returns:
        None
        """
        self._strategy = strategy
        
    def execute_inspection(self, df:pd.DataFrame):
        """
        Excecutes the inspection using the current startegy.
        
        Parameters:
        df (pd.DataFrame): The DataFrame to be inspected
        
        Returns:
        None: Executes the stratgey's inspection method
        """
        
        self._strategy.inspect(df)
        

if __name__ == "__main__":
    pass
    
    
       
       
       