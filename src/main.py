import os
from File.FileMGR import FileMGR
from math import sqrt

def euclidean_distance(p1, p2):
    return sqrt(sum((x - y)**2 for x, y in zip(p1, p2)))


def knn(train, query, k):
    distance = []
    for features, label in train:
        dist = euclidean_distance(features, query)
        distance.append((dist, label))
    distance.sort(key=lambda x: x[0])
    k_near = [label for _, label in distance[:k]]
    return max(set(k_near), key=k_near.count)


def main():
    # Assuming the CarEvaluation dataset is a data file
    datasetPath = os.path.join(
        'CarEvaluation', 'car.data')  # Adjust path as needed

    fileMGR = FileMGR()
    # Read the dataset using FileMGR
    df = fileMGR.fileReader(datasetPath)
    df = fileMGR.datasetChanger(df)
    data = fileMGR.dfToList(df)
    del df

    # Now you can work with the data
    correct = 0
    train_data, test_data = fileMGR.split_data(data)
    for features, true_label in test_data:
        prediction_label = knn(train_data, features, 5)
        if prediction_label == true_label:
            correct += 1
        

    input_data = [1,2,2,2,1,2]
    prediction_label = knn(train_data, input_data, 3)
    print(prediction_label)


    acc = correct / len(test_data)
    print(f"accuracy: {acc*100:0.3f}")

    # print(df)


if __name__ == '__main__':
    main()
