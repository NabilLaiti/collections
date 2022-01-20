listOne = [i for i in range(1, 11)]
listTwo = [i for i in range(2, 21, 2)]


def addAndDisplayList(l1, l2):
    print('---------')
    print('Plus sommen')
    for i in range(min(len(l1), len(l2))):
        print("{:<2} + {:<2} = {:<5}".format(l1[i], l2[i], l1[i] + l2[i]))


def substractAndDisplayLists(l1, l2):
    print('---------')
    print('Min sommen')
    for i in range(min(len(l1), len(l2))):
        print("{:<2} - {:<2} = {:<5}".format(l1[i], l2[i], l1[i] - l2[i]))


def multiplyAndDisplayLists(l1, l2):
    print('---------')
    print('Keer sommen')
    for i in range(min(len(l1), len(l2))):
        print("{:<2} * {:<2} = {:<5}".format(l1[i], l2[i], l1[i] * l2[i]))


def divideAndDisplayLists(l1, l2):
    print('---------')
    print('Delen door')
    for i in range(min(len(l1), len(l2))):
        print("{:<2} / {:<2} = {:<5}".format(l1[i], l2[i], l1[i] / l2[i]))

