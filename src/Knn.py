from math import sqrt

class Knn:
    # calculates euclidean distance (basically)
    def euclidean_distance(self, p1, p2):
        return sqrt(sum((x - y)**2 for x, y in zip(p1, p2)))

    # calculates knn of the query based on train dataset
    # with the count of k
    def knn(self, train, query, k):
        distance = []
        for features, label in train:
            dist = self.euclidean_distance(features, query)
            distance.append((dist, label))
        distance.sort(key=lambda x: x[0])
        k_near = [label for _, label in distance[:k]]
        return max(set(k_near), key=k_near.count)