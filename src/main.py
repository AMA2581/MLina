import os
from File.FileMGR import FileMGR

def main():
    # Assuming the AutoMPG dataset is a CSV file
    datasetPath = os.path.join('AutoMPG', 'auto-mpg.data')  # Adjust path as needed

    # Read the dataset using FileMGR
    data = FileMGR.fileReader(datasetPath)

    # Now you can work with the data
    print(data.head())

if __name__ == '__main__':
    main()