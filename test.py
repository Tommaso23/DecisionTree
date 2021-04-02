from dataset import *
from copy import deepcopy
from datetime import datetime
import random


def accuracy(examples, target, tree):
    i = 0
    for e in examples:
        if e[target] != tree(e):
            i += 1
    return 100 - (i / len(examples) * 100)


def train_val_test(dataset, perc_train, perc_val):

    training_set = []
    validation_set = []
    test_set = []

    random.seed(datetime.now())
    random.shuffle(dataset.examples)

    dim_train = int((len(dataset.examples) / 100) * perc_train)
    dim_val = int((len(dataset.examples) / 100) * perc_val)
    dim_test = int((len(dataset.examples)))
    for i in dataset.examples[0:dim_train]:
        training_set.append(i)

    for i in dataset.examples[dim_train:dim_train+dim_val]:
        validation_set.append(i)

    for i in dataset.examples[dim_train+dim_val:dim_test]:
        test_set.append(i)
    return training_set, validation_set, test_set


def set_inputs(attributes, target):
    inputs = deepcopy(attributes)
    inputs.pop(inputs.index(target))
    return inputs


def create_dataset(file, attrnames, target_index, values):
    dset = list()
    parts = []
    for line in open(file).readlines():
        parts = line.rstrip()
        parts = line.split(',')
        parts = [p.rstrip() for p in parts]
        dset.append(parts)

    examples = []
    for i in range(len(dset)):
        example = {}
        for j in range(len(dset[0])):
            example[j] = dset[i][j]
        examples.append(example)
    attributes = [k for k in range(len(examples[0]))]
    inputs = set_inputs(attributes, target_index)

    return DataSet(file, examples, inputs, attributes, target_index, attrnames, values)
