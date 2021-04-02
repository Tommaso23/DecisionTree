class DecisionLeaf:


    def __init__(self, result, nodes = 1):
        self.nodes = nodes
        self.result = result

    def __call__(self, example):
        return self.result

    def display(self):
        print('RESULT =', self.result)










