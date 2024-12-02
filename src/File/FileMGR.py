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

        df = pd.DataFrame(data)

        return df
    
    def datasetChanger(df):
        attribute_mapping = {
            'buying': {'vhigh': 3, 'high': 2, 'med': 1, 'low': 0},
            'maint': {'vhigh': 3, 'high': 2, 'med': 1, 'low': 0},
            'doors': {'2': 0, '3': 1, '4': 2, '5more': 3},
            'persons': {'2': 0, '4': 1, 'more': 2},
            'lug_boot': {'small': 0, 'med': 1, 'big': 2},
            'safety': {'low': 0, 'med': 1, 'high': 2}
        }

        for attribute, mapping in attribute_mapping.items():
            df[attribute] = df[attribute].replace(mapping)

        return df
    

    
            
