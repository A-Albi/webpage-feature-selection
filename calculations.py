from sklearn.feature_selection import chi2
from sklearn.feature_selection import mutual_info_classif
from sklearn.model_selection import train_test_split
from sklearn.decomposition import RandomizedPCA
from sklearn import svm
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

# CSE 5820
# August 29, 2018

# This file utilizes sklearn to carry out the Principal Components Analysis, the Information Gain,
# and the Chi-Squared computations, as well as the Support Vector Machine testing on its accuracy.

def information_gain(x, y):
    sizes = np.shape(x)
    cols = sizes[1]

    # Obtain the Information Gain values
    information_gain_values = mutual_info_classif(x, y)

    # Maximum information gain reflects relevance of each feature
    feature_order = np.argsort(information_gain_values)[::-1][:cols]
    return feature_order


def chi_squared(x, y):
    # Obtain the Chi-Squared values
    chi_squared_values, _ = chi2(x, y)

    # Minimum chi-squared values indicate more relevant features
    feature_order = np.argsort(chi_squared_values)
    return feature_order


def principal_component_analysis(x):
    sizes = np.shape(x)
    cols = sizes[1]

    # Obtain the Principal Components, which are ordered by eigenvalues
    principal_components = RandomizedPCA(n_components=cols)
    principal_components.fit_transform(x)
    eigenvalues = principal_components.explained_variance_

    # Maximum eigenvalues reflect importance of each feature
    feature_order = np.argsort(eigenvalues)[::-1][:cols]
    return feature_order


# Feeds selected features x and labels y into the Support Vector Machine

def support_vector_machine(x, y, t_size):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=t_size, random_state=42)
    classifier = svm.SVC()
    classifier.fit(x_train, y_train)
    return classifier.score(x_test, y_test)
