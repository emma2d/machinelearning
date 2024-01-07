# Machine Learning Module

***
Author: Emma Dunleavy

Student Number: g00425660

Module: Machine Learning Winter 2023/24 

Lecturer: Ian McLoughlin
***

***

This repo contains two Jupyter Notebooks, one for tasks and one for project.

#### Versions installed 

NumPy version: 1.23.5

Matplotlib version: 3.7.0

Sklearn version: 1.2.1

Seaborn version: 0.12.2

Pandas version: 1.5.3

## Tasks

#### Libraries required 

import numpy as np

import pandas as pd

import scipy.stats as ss

import scipy.stats as ss and from this library use .chi2_contingency and f_oneway

import seaborn as sns

import matplotlib.pyplot as plt

import sklearn as sk

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.neighbors import KNeighborsClassifier

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler

from sklearn.inspection import DecisionBoundaryDisplay

from sklearn.metrics import accuracy_score

import sklearn.preprocessing as pre

import sklearn.decomposition as dec

#### List of tasks
1. Square roots [1]
2. Chi-Square test [2], [3]
3. Penguins data set [4], [5], [6], [9]
4. Iris data set [7], [8]
5. Principal component analysis [10]

#### References 

[1] Programming and Scripting Module weekly task https://github.com/emma2d/pands-problem-sheet. [Accessed 4 Oct. 2023].

[2] docs.scipy.org. (n.d.). scipy.stats.chi2_contingency — SciPy v1.8.0 Manual. [online] Available at: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html. [Accessed 16 Oct. 2023].

[3] docs.scipy.org. (n.d.). scipy.stats.chi2_contingency — SciPy v1.8.0 Manual. [online] Available at: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html. [Accessed 16 Oct. 2023].

[4] mwaskom/seaborn-data:Data repositoryfor seaborn examples. Oct. 31, 2023. url: https://github.com/mwaskom/seaborn-data/blob/master/penguins.csv. [Accessed 31 Oct. 2023].

[5] The Pandas Development Team (2022). pandas.DataFrame.info — pandas 1.4.1 documentation. [online] pandas.pydata.org. Available at: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html.
[Accessed 31 Oct. 2023].

[6] https://www.hackdeploy.com/python-t-test-a-friendly-guide/. [Accessed 31 Oct. 2023].

[7] www.linkedin.com. (n.d.). Data Science Tutorial in Python. [online] Available at: https://www.linkedin.com/pulse/data-science-tutorial-python-ambica-nandimandalam [Accessed 19 Nov. 2023].

[8] scikit-learn. (n.d.). Nearest Neighbors Classification. [online] Available at: https://scikit-learn.org/stable/auto_examples/neighbors/plot_classification.html#sphx-glr-auto-examples-neighbours-plot-classification-py [Accessed 20 Nov. 2023].

[9] hZach (2022). How to Modify a Matplotlib Histogram Color (With Examples). [online] Statology. Available at: https://www.statology.org/matplotlib-histogram-color/. [Accessed 20 Nov. 2023].

[10] Lever, J., Krzywinski, M. and Altman, N. (2017). Principal component analysis. Nature Methods, [online] 14(7), pp.641–642. doi:https://doi.org/10.1038/nmeth.4346. [Accessed 31 Dec. 2023].

***

## Project

The project is to create a notebook exploring classification algorithms applied on the iris flower data set associated with Ronald A Fisher.

    Explain what supervised learning is and then explain what classification algorithms are.
    Describe at least one common classification algorithm and implement it using the scikit-learn Python library.
    Throughout your notebook, use appropriate plots, mathematical notation, and diagrams to explain the relevant concepts.


View using https://nbviewer.org/ to ensure all images are rendered correctly. Image saved in folder "images"

The Iris Data Set was both read in from a cvs file, found in a folder "Data" saved in teh repo. Note, for some of the visualisations the dataset was imports from the scikit learn database.

#### Required Librares

import matplotlib.pyplot as plt

import seaborn as sns

import numpy as np

import pandas as pd

import sklearn as sk

from sklearn import datasets

from sklearn.linear_model import LogisticRegression

from sklearn.tree import DecisionTreeClassifier

from sklearn.neighbors import KNeighborsClassifier

from sklearn.pipeline import Pipeline

from sklearn.preprocessing import StandardScaler

from sklearn.inspection import DecisionBoundaryDisplay

from sklearn.datasets import load_iris

from sklearn.model_selection import train_test_split

from sklearn.pipeline import make_pipeline

from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import classification_report, confusion_matrix

Refer to project.ipynb for list of references used. 

*** 

End
   


*** 

End
   
