import time
import itertools
import numpy as np
import matplotlib
matplotlib.use("TkAgg") # why?
from matplotlib import pyplot as plt
import pickle
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

import massageData

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()


def get_label(Y):
    labels = list(set(Y))
    print ('Labels: ', labels)
    return labels

def run():
    dataGetter = massageData.massageData()
    X_train, Y_train = dataGetter.getTrain() #TODO: feature extractions
    X_dev, Y_dev = dataGetter.getDev()
    clf = LogisticRegression(random_state=0, solver='lbfgs', multi_class='multinomial', verbose=1).fit(X_train, Y_train)
    Y_dev_prediction = clf.predict(X_dev)
    print ('Prediction: ', Y_dev_prediction)
    print ('Actual Label: ', Y_dev)
    print ('Accuracy: ', clf.score(X_dev, Y_dev))
    class_names = get_label(Y_dev)
    confusion = confusion_matrix(Y_dev, Y_dev_prediction, labels=class_names)
    print ("Confusion matrix: ", confusion)

    pickle.dump(class_names, open("class_names", 'wb'))
    pickle.dump(confusion, open("confusion_matrix_3class", 'wb'))

def main():
    print ('Opening the files...')
    with open("class_names", 'rb') as f:
        class_names = pickle.load(f)

    with open("confusion_matrix_3class", 'rb') as f:
        confusion = pickle.load(f)

    print ('Finish reading the files...')

    print ('Class names: {}'.format(class_names))
    print ('Confusion matrix: {}'.format(confusion))
    np.set_printoptions(precision=2)

    # Plot non-normalized confusion matrix
    plt.figure()
    plot_confusion_matrix(confusion, classes=class_names,
                          title='Confusion matrix, without normalization')

    # # Plot normalized confusion matrix
    # plt.figure()
    # plot_confusion_matrix(confusion, classes=class_names, normalize=True,
    #                       title='Normalized confusion matrix')

    plt.show()

#TODO: want to scale this up to 10 classes: add more file, compare runtime


if __name__ == '__main__':
    #run()
    main()