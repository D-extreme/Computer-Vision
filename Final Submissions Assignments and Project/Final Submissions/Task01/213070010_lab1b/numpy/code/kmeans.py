import os
import random
import numpy as np
import matplotlib.pyplot as plt

# * YOU ARE NOT ALLOWED TO IMPORT ANYTHING ELSE  *#

seed = 0
random.seed(seed)
os.environ['PYTHONHASHSEED'] = str(seed)
np.random.seed(seed)


# Here is a template for the KMeans clustering class
# The class has two functions "fit" and "predict" that you need to implement
# The fit function generates and stores  cluster centers for the
# given data
# The predict function assigns the input data to clusters
# (as learned by the fit function)
#  The input X should be a numpy array of of dimensions (n_data, n_features)
#  n_data is the dataset size
#  n_features is the feature dimension. For example for 3D datapoints,
#  n_features will be 3
#  Do not hard code n_features to any value - We will test your code on
# high dimension data


class KMeans(object):
    def __init__(self, n_clusters):
        super(KMeans, self).__init__()
        self.n_clusters = n_clusters
        self.centers = None

    def fit(self, X):
        if self.centers is None:
            # Intialise self.centers
            # TODO#
            arr = []  # creating an empty list
            for i in range(self.n_clusters):
                arr.append(X[np.random.randint(len(X))])  # Appending random N elements from X as centers
            self.centers = arr  # Initialization of the center

            # TODO#
        while True:
            # Assign data points to clusters
            # TODO#
            # Initialization of Cluster list
            clusters = []
            for p in range(self.n_clusters):
                clusters.append([])

            # Initialization of Cluster Indices
            index_values = []
            for i in X:
                dist = list(map(lambda x: np.linalg.norm(x - i),
                                self.centers))  # finding the minimum distance of data point from the centers
                index_values.append(np.argmin(dist))  # appending the index of minimum distance center
                clusters[np.argmin(dist)].append(i)  # adding the data point to the corresponding cluster data
            # TODO#

            # Update cluster centers
            # TODO#
            new_centers = []
            for i in range(len(clusters)):
                new_centers.append(np.mean(clusters[i], axis=0))  # finding the mean of each cluster
            # TODO#

            # Breaking condition
            # TODO#
            if np.linalg.norm(np.array(new_centers) - np.array(
                    self.centers)) < 0.02:  # checking if the new centers differs significantly from the previous ones
                break  # if yes, break the loop and exit
            else:
                self.centers = new_centers  # if no, update the centers
            # TODO#

    # Returns a numpy array of dimensions (n_data,)
    def predict(self, X):
        # Assign data points to clusters
        # TODO#
        index_values = []
        for i in X:
            dist = list(map(lambda x: np.linalg.norm(x - i),
                            self.centers))  # finding the minimum distance of data point from the centers
            index_values.append(np.argmin(dist))  # appending the index of minimum distance center
        return np.array(index_values)
        # TODO#


# Feel free to experiment with this


NUM_CLUSTERS = 3

# Create data such that it naturally forms clusters in 2D space 
# shape of this numpy array should be (n_data, n_features)
# here n_data is the dataset size (should be 600)
# here n_features is the dataset size (should be 2)
n_data = 600
n_features = 2
std = 0.7  # Standard deviation
arr1 = np.random.normal([3, 2], std, size=(n_data//2, n_features))  # Normal distribution around [3,2] with standard deviation 0.7
arr2 = np.random.normal([1, 5], std, size=(n_data//2, n_features))  # Normal distribution around [1,5] with standard deviation 0.7
arr3 = np.random.normal([0, 1], std, size=(n_data//2, n_features))  # Normal distribution around [0,1] with standard deviation 0.7

# TODO#
dataIn = np.concatenate((arr1, arr2, arr3), axis=0)

# show data
plt.figure()
plt.scatter(dataIn[:, 0], dataIn[:, 1], alpha=0.3, marker='o')
plt.title('Input Data')
plt.savefig('../results/inputCluster.png')

kmm = KMeans(n_clusters=NUM_CLUSTERS)
kmm.fit(dataIn)
preds = kmm.predict(dataIn)
plt.figure()
colors = ['b', 'r', 'g', 'c', 'm', 'y', 'k', 'lime', 'turquoise', 'blueviolet', 'crimson', 'peru', 'maroon']
for ci in range(NUM_CLUSTERS):
    indices = preds == ci
    plt.scatter(dataIn[indices, 0], dataIn[indices, 1], alpha=0.3, marker='o', color=colors[ci % len(colors)],
                label='Cluster {}'.format(ci))
    plt.legend()
    plt.title('Clustered Data')
    plt.savefig('../results/outputCluster.png')
