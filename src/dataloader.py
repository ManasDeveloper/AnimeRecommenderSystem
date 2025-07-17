import pandas as pd 

class AnimeDataLoader:
    def __init__(self,original_csv:str,processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv


    def load_and_process(self):
        df = pd.read_csv(self.original_csv,encoding='utf-8',on_bad_lines="skip").dropna() # drop all the rows with null values
        required_cols = {"Name","Genres","sypnopsis"}

        missing = required_cols - set(df.columns) # check if the required columns are present in the dataframe

        if missing:
            raise ValueError(f"Missing columns in the dataset: {missing}")
        
        # combine the required columns into a single column
        df["combined_info"] = (
            "Title : " + df["Name"] +  " Overview : " + df["sypnopsis"] + " Genres : " + df["Genres"]
        )

        df["combined_info"].to_csv(self.processed_csv, index=False, encoding='utf-8') # save the processed data to a new csv file

        return self.processed_csv
