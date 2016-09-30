from sklearn.linear_model import LogisticRegression as lr
from sklearn.metrics import accuracy_score

import numpy as np

from decision_tree import load_data


if __name__ == '__main__':
    print "Tutorial: Training a logistic regression to detect phishing websites"

    # Load the training data
    train_inputs, train_outputs, test_inputs, test_outputs = load_data()
    print "Training data loaded."

    # Create a logistic regression classifier model using scikit-learn
    classifier = lr()
    print "Logistic regression classifier created."

    print "Beginning model training."
    # Train the logistic regression classifier
    classifier.fit(train_inputs, train_outputs)
    print "Model training completed."

    # Use the trained classifier to make predictions on the test data
    predictions = classifier.predict(test_inputs)
    print "Predictions on testing data computed."

    # Print the accuracy (percentage of phishing websites correctly predicted)
    accuracy = 100.0 * accuracy_score(test_outputs, predictions)
    print "The accuracy of your logistic regression on testing data is: " + str(accuracy)
