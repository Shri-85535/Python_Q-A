if __name__ == '__main__':
    N = int(input())
    list = []
    while N != 0:
        task = input()
        if 'insert' in task:
            actual = task, *position, number = task.split()
            list.insert(int(actual[1]), int(actual[2]))
            N = N - 1
        elif 'print' in task:
            print(list)
            N = N - 1
        elif 'remove' in task:
            actual = task, *number = task.split()
            list.remove(int(actual[1]))
            N = N - 1
        elif 'append' in task:
            actual = task, *number = task.split()
            list.append(int(actual[1]))
            N = N - 1
        elif 'sort' in task:
            list.sort()
            N = N - 1
        elif 'pop' in task:
            list.pop()
            N = N - 1
        elif 'reverse' in task:
            list.reverse()
            N = N - 1
        else:
            print('Invalid Command')


