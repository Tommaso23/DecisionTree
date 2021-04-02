class DecisionTree:

    def __init__(self, attribute, attrname=None, branches=None):
        self.attribute = attribute
        self.attrname = attrname or attribute
        self.branches = branches or {}



    def __call__(self, example):
        attr_value = example[self.attribute]
        return self.branches[attr_value](example)


    def add(self, value, subtree):
        self.branches[value] = subtree


    def display(self, indent=0):
        name = self.attrname
        print('TEST', name)
        for (val, subtree) in self.branches.items():
            print(' ' * 4 * indent, name, '=', val, '==>', end=' ')
            subtree.display()






















