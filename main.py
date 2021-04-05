"""
Questo file contiene le funzioni per effettuare i test sui 3 dataset scelti.

Per effettuare i test bisogna commentare la parte di codice relativa ai restanti due dataset che non si vuole testare.

Testare un dataset alla volta
"""


from test import *
from decisiontreelearner import *
import matplotlib.pyplot as plt


# DataSet 1: CAR EVALUATION_____________________________________________________________________________________________

car_names = {0: 'buying', 1: 'maint', 2: 'doors', 3: 'persons', 4: 'lug_boot', 5: 'safety', 6: 'evaluation'}
car_values = {0: ['vhigh', 'high', 'med', 'low'],
              1: ['vhigh', 'high', 'med', 'low'],
              2: ['2', '3', '4', '5more'],
              3: ['2', '4', 'more'],
              4: ['small', 'med', 'big'],
              5: ['low', 'med', 'high'],
              6: ['unacc', 'acc', 'good', 'vgood']}

dataset = create_dataset('car.txt', car_names, 6, car_values)
dataset.examples, val, test = train_val_test(dataset, 60, 20)

threshold = []
train_results = []
val_results = []
test_results = []

for i in range(0, 100):
    tree = decision_tree_learner(dataset, error_threshold=i)
    threshold.append(i)
    train_results.append(accuracy(dataset.examples, 6, tree))
    val_results.append(accuracy(val, 6, tree))
    test_results.append(accuracy(test, 6, tree))

# DataSet 2: BALANCE SCALE______________________________________________________________________________________________

bs_names = {0: 'balanced', 1: 'left-weight', 2: 'left-distance', 3: 'right-weight', 4: 'right-distance'}
bs_values = {0: ['L', 'B', 'R'],
             1: ['1', '2', '3', '4', '5'],
             2: ['1', '2', '3', '4', '5'],
             3: ['1', '2', '3', '4', '5'],
             4: ['1', '2', '3', '4', '5'],
             5: ['1', '2', '3', '4', '5']}

'''dataset = create_dataset('balance-scale.txt', bs_names, 0, bs_values)
dataset.examples, val, test = train_val_test(dataset, 60, 20)


threshold = []
train_results = []
val_results = []
test_results = []

for i in range(0, 100):
    tree = decision_tree_learner(dataset, error_threshold=i)
    threshold.append(i)
    train_results.append(accuracy(dataset.examples, 0, tree))
    val_results.append(accuracy(val, 0, tree))
    test_results.append(accuracy(test, 0, tree))'''


# DataSet 3: TIC TAC TOE________________________________________________________________________________________________
ttt_names = {0: 'top-left-square', 1: 'top-middle-square', 2: 'top-right-square', 3: 'middle-left-square',
             4: 'middle-middle-square', 5: 'middle-right-square', 6: 'bottom-left-square', 7: 'bottom-middle-square',
             8: 'bottom-right-square', 9: 'outcome'}
ttt_values = {0: ['x', 'o', 'b'],
             1: ['x', 'o', 'b'],
             2: ['x', 'o', 'b'],
             3: ['x', 'o', 'b'],
             4: ['x', 'o', 'b'],
             5: ['x', 'o', 'b'],
             6: ['x', 'o', 'b'],
             7: ['x', 'o', 'b'],
             8: ['x', 'o', 'b'],
             9: ['positive', 'negative']}



''''dataset = create_dataset('tic-tac-toe.txt', ttt_names, 9, ttt_values)
dataset.examples, val, test = train_val_test(dataset, 60, 20)

threshold = []
train_results = []
val_results = []
test_results = []

for i in range(0, 100):
    tree = decision_tree_learner(dataset, error_threshold=i)
    threshold.append(i)
    train_results.append(accuracy(dataset.examples, 9, tree))
    val_results.append(accuracy(val, 9, tree))
    test_results.append(accuracy(test, 9, tree))'''



# LASCIARE LA SEGUENTE PARTE SEMPRE NON COMMENTATA

max_index = val_results.index(max(val_results))
print('train_accuracy without pruning', train_results[0], '%')
print('val_accuracy without pruning', val_results[0], '%')
print('test_accuracy without pruning', test_results[0], '%')
print('train_accuracy at index of max val result: ', train_results[max_index], '%')
print('val_accuracy at index of max val result: ', val_results[max_index], '%')
print('test_accuracy at index of max val result: ', test_results[max_index], '%')
print('error threshold to reach max value: ', max_index)


plt.scatter(max_index, val_results[max_index])
plt.plot(threshold, train_results, label="train")
plt.plot(threshold, val_results, label="val")
plt.plot(threshold, test_results, label="test")
plt.legend()
plt.xlabel('error_threshold')
plt.ylabel('accuracy')
plt.show()

print("percentage of improvement on test_set after pruning: ", test_results[max_index] - test_results[0], '%')



