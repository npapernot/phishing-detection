from sklearn import tree
from sklearn.metrics import accuracy_score

import numpy as np


def load_data():
    """
    This helper function loads the dataset saved in the CSV file
    and returns 4 numpy arrays containing the training set inputs
    and labels, and the testing set inputs and labels.
    """

    # Load the training data from the CSV file
    training_data = np.genfromtxt('training.csv', delimiter=',', dtype=np.int32)

    """
    Each row of the CSV file contains the features collected on a website
    as well as whether that website was used for phishing or not.
    We now separate the inputs (features collected on each website)
    from the output labels (whether the website is used for phishing).
    """

    # Extract the inputs from the training data array (all columns but the last one)
    inputs = training_data[:,:-1]

    # Extract the outputs from the training data array (last column)
    outputs = training_data[:, -1]

    # Separate the training (first 2,000 websites) and testing data (last 456)
    training_inputs = inputs[:2000]
    training_outputs = outputs[:2000]
    testing_inputs = inputs[2000:]
    testing_outputs = outputs[2000:]

    # Return the four arrays
    return training_inputs, training_outputs, testing_inputs, testing_outputs


if __name__ == '__main__':
    # Load the training data
    train_inputs, train_outputs, test_inputs, test_outputs = load_data()

    # Create a decision tree classifier model using scikit-learn
    classifier = tree.DecisionTreeClassifier()

    # Train the decision tree classifier
    classifier.fit(train_inputs, train_outputs)

    # Use the trained classifier to make predictions on the test data
    predictions = classifier.predict(test_inputs)

    # Return the accuracy (percentage of phishing websites correctly predicted)
    print accuracy_score(test_outputs, predictions)