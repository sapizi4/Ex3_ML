import numpy as np
import scipy
import sys



def read_data(data):
    X = []
    #dictionary to convert sex to int
    label_dict = {'T-shirt/top': 0, 'Trouser': 1, 'Pullover': 2, 'Dress': 3, 'Coat': 4, 'Sandal': 5, 'Shirt': 6, 'Sneaker': 7, 'Bag': 8, 'Ankle boot': 9}
    with open(data, 'r') as values:
        for idx in values:
            idx = idx.strip().split(',')
            idx[0] = label_dict[idx[0]]
            X.append(np.array(idx, dtype=np.float64))
    return np.asarray(X)


# the main function.
if __name__ == "__main__":
    if __name__ == '__main__':
        args = sys.argv
        X = read_data(args[1])
        Y = np.genfromtxt(args[2], delimiter=',')
