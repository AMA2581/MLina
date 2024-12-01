import os
from File.FileMGR import FileMGR

def main():
    # Assuming the CarEvaluation dataset is a data file
    datasetPath = os.path.join('CarEvaluation', 'car.data')  # Adjust path as needed

    # Read the dataset using FileMGR
    data = FileMGR.fileReader(datasetPath)

    # Now you can work with the data
    print(data)

if __name__ == '__main__':
    main()
