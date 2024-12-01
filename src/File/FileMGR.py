import pandas as pd

class FileMGR:
    def fileReader(path):
        if path.endswith('.csv'):
            data = pd.read_csv(path)
        elif path.endswith('.data'):
        # Assuming the data file uses whitespace as delimiter
            data = pd.read_csv(path, sep=',')
        elif path.endswith('.xlsx'):
            data = pd.read_excel(path)
        else:
            raise ValueError("Unsupported file format.")

        return data
