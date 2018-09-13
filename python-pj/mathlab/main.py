# coding: utf-8
import input_data as datain
#datain.out2csv()
import bayes_classify as bc
import numpy as np
import matplotlib.pyplot as plt
import sklearn.metrics as cmat


def predict(data=datain.predictdata):
    i = 0
    for x in data:
        res = bc.predict(x)
        if res is 1:
            print("{0}:{1}".format(x, 'Spam'))
            i += 1
    print("Num:",i)

matrix = []
def ConfusionMatrixPng(cm,classlist):

    fig = plt.figure()
    plt.clf()
    ax = fig.add_subplot(111)
    #ax.set_aspect(1)
    norm_conf = []
    c2 = 0
    for i in cm:
        a = 0
        c1 = 0
        tmp_arr = []
        a = sum(i)
        for j in i:
            tmp_arr.append(float(j) / float(a))
            plt.text(c1,c2,'%.4f' % (float(j) / float(a)), ha='center', va='center', fontsize=20)
            c1 += 1
        c2 += 1
        norm_conf.append(tmp_arr)

    res = ax.imshow(np.array(norm_conf),
                    interpolation='nearest')
    width = len(cm)
    height = len(cm[0])
    cb = fig.colorbar(res)
    alphabet = classlist
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.xticks(range(width), alphabet[:width])
    # plt.xticks('orientation', 'vertical')
    # locs, labels = xticks([1,2,3,4], ['Frogs', 'Hogs', 'Bogs', 'Slogs'])
    # setp(alphabet, 'rotation', 'vertical')
    plt.yticks(range(height), alphabet[:height])
    plt.savefig('confusion_matrix.png', format='png')
    plt.show()

def confusionmat_gen():
    tmp = datain.traindata
    sflags = [x[0] for x in tmp]
    data = [x[1] for x in tmp]
    pflags = []
    for i in data:
        pflags.append(bc.predict(i))
        '''
                pflag
        _____|ham   | spam |
             +++++++++++++++
sflag   ham  |      +      |
        spam |      +      |
             +++++++++++++++
        '''
    ConfusionMatrixPng(cmat.confusion_matrix(sflags, pflags), ['ham', 'spam'])
