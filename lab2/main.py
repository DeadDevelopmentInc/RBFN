import sys
import os
import xml.etree.ElementTree as ET
from .network import Network

def reading_datasets(path, num_class):
    folders = os.listdir(path)
    if len(folders) != num_class:
        raise Exception("Invalid class number in datasets")
    for folder in folders:
    
    return X, Y

def reading_one_file(path)
    return X

def train(network, X, Y, batch_size):
    return network

def predict(network, X):
    return predict


def main():
    try:
        if len(sys.argv[1:]) != 1:
            raise Exception("Invalid command arguments")
        tree = ET.parse(sys.argv[1:][0])
        root = tree.getroot()
        if len(root) != 1:
            raise Exception("Invalid file, check file")
        trainpath = root[0].attrib['name']
        print("Start reading datasets")
        X, Y = reading_datasets(trainpath, 3)
        print("Finish reading datasets\nStart creating and training network")
        Network net = new Network()
        net = train(net ,X, Y, bacth_size)
        flag_out = False
        while !flag-out:
            print("Choose option from list (write number of option)\n1.Recognize image\n2.Re-train network\n3.Exit ")
            choose = read()
            if choose == "1":
                print("Write path to image: ")
                pred = read_one_file(read())
                print(predict(net, pred))
            elif choose == "2":
                X, Y = read_datasets(trainpath, 3)
                net = train(net ,X, Y, bacth_size)
            else:
                flag_out = True
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()