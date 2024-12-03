import os
from FileMGR import FileMGR
from Knn import Knn

def main():
    # Assuming the CarEvaluation dataset is a data file
    datasetPath = os.path.join('CarEvaluation', 'car.data')

    fileMGR = FileMGR()
    knn = Knn()
    # Read the dataset using FileMGR
    df = fileMGR.fileReader(datasetPath)
    df = fileMGR.datasetChanger(df)
    data = fileMGR.dfToList(df)
    del df

    # Now you can work with the data
    correct = 0
    train_data, test_data = fileMGR.split_data(data)
    for features, true_label in test_data:
        prediction_label = knn.knn(train_data, features, 3)
        if prediction_label == true_label:
            correct += 1
        
    # change for input
    input_data = [1,2,2,2,1,2]
    
    prediction_label = knn.knn(train_data, input_data, 3)
    print(prediction_label)


    acc = correct / len(test_data)
    print(f"accuracy: {acc*100:0.3f}")

    # print(df)


if __name__ == '__main__':
    main()
