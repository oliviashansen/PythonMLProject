from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC


def SKLearnKnnClassifier(training, testing, training_labels, testing_labels, k):
    '''leverage Scikit-learn to implement the k nearest neighbors algorithm
    Args:
        training: the subset of data corresponding to the training data as a numpy matrix
        testing:  the subset of data corresponding to the testing data as a numpy matrix
        training_labels: the labels for the training data as a numpy array
        testing_labels: the labels for the testing data as a numpy array
        k: the number of nearest neighbors to use

    This should instantiate the class from scikit learn, then call
    `.fit` and `.predict`. It should then compare results similar to
    NNClassifier to return a % correct.
    
    See how easy it is to use scikit learn?
    '''
    # instantiate model
    model = KNeighborsClassifier(n_neighbors=k)

    # fit model to training data
    # training the model on the training data and training labels
    model.fit(training,training_labels)

    # predict test labels
    # generating a numpy array of the predicted labels from the testing data 
    predicted_test_labels = model.predict(testing)
    
    # percent of predicted labels that matched actual
    x = sum(predicted_test_labels == testing_labels) / len(testing_labels) 

    # return % where prediction matched actual
    return x

def SKLearnSVMClassifier(training, testing, training_labels, testing_labels):
    '''leverage Scikit-learn to implement the support vector machine classifier
    Args:
        training: the subset of data corresponding to the training data as a numpy matrix
        testing:  the subset of data corresponding to the testing data as a numpy matrix
        training_labels: the labels for the training data as a numpy array
        testing_labels: the labels for the testing data as a numpy array

    This should instantiate the class from scikit learn, then call
    `.fit` and `.predict`. It should then compare results similar to
    NNClassifier to return a % correct.
    
    See how easy it is to use scikit learn?
    '''
    # instantiate model
    model = SVC()

    # fit model to training data
    # training the model on the training data and training labels
    model.fit(training, training_labels)

    # predict test labels
    # generating a numpy array of the predicted labels from the testing data
    predicted_test_labels = model.predict(testing)
    
    # percent of predicted labels that matched actual
    x = ((sum(predicted_test_labels == testing_labels)) / len(testing_labels)) 

    # return % where prediction matched actual
    return x