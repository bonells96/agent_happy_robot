import pandas as pd
from app.load_checker.data_access.pandas_accessor import PandasAccessor

class CSVLoader:
    def __init__(self, file_path: str = 'example_load_data.csv'):
        self.file_path = file_path
        self.df = pd.read_csv(self.file_path)
        self.accessor = PandasAccessor(self.df)

    def get_accessor(self):
        return self.accessor