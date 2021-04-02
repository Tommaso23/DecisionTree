import math
from decisiontree import DecisionTree
from decisionleaf import DecisionLeaf



def decision_tree_learner(dataset, error_threshold):

    target = dataset.target
    values = dataset.values

    def decision_tree_learning(examples, attributes, parent_examples=()):
        if len(examples) == 0:
            return plurality_value(parent_examples)
        elif same_classification(examples):
            return DecisionLeaf(examples[0][target])
        elif len(attributes) == 0:
            return plurality_value(examples)
        elif pruning(examples) < error_threshold:
            return plurality_value(examples)
        else:
            a = importance(attributes, examples)
            tree = DecisionTree(a, dataset.attrnames[a])
            for (val_i, exs_i) in split_by(a, examples):
                subtree = decision_tree_learning(exs_i, removeall(a, attributes), examples)
                tree.add(val_i, subtree)
            return tree

    def plurality_value(examples):
        major = None
        i = 0
        for v in values[target]:
            if (count(target, v, examples) > i):
                i = count(target, v, examples)
                major = v
        return DecisionLeaf(major)

    def same_classification(examples):
        classification = examples[0][target]
        for e in examples:
            if e[target] != classification:
                return False
        return True

    def entropy_bits(examples):
        e = 0
        for v in values[target]:
            if len(examples) != 0:
                p = count(target, v, examples) / len(examples)
                if (p != 0):
                    e += ((-p) * math.log2(p))

        return e

    def information_gain(a, examples):
        n = float(len(examples))
        remainder = 0
        for (v, examples_i) in split_by(a, examples):
            remainder += ((len(examples_i) / n) * entropy_bits(examples_i))
        return entropy_bits(examples) - remainder

    def importance(attributes, examples):
        max = 0
        for a in attributes:
            if information_gain(a, examples) >= max:
                max = information_gain(a, examples)
                best = a
        return best

    def split_by(attribute, examples):

        return [(v, [e for e in examples if e[attribute] == v])
                for v in values[attribute]]

    def count(attribute, value, examples):
        i = 0
        for e in examples:
            if e[attribute] == value:
                i += 1
        return i

    def removeall(item, seq):

        if isinstance(seq, str):
            return seq.replace(item, '')
        else:
            return [x for x in seq if x != item]


    def pruning(examples): #calcola la percentuale di quelli sbagliati
        p_v = plurality_value(examples)
        num_max = count(target, p_v, examples)
        return 100 - num_max*100/len(examples)

    return decision_tree_learning(dataset.examples, dataset.inputs)

