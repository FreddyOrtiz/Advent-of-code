with open('input.txt') as f:
    inputs = [line for line in f.read().splitlines()]
    a = []
    for line in inputs:
        operation, arg = line.split(' ')
        a.append([operation, int(arg)])
    accumulator = 0
    visited = [False for _ in a]
    i = 0
    while (0 <= i < len(a)) and (not visited[i]):
        visited[i] = True
        operation, arg = a[i]
        if operation == 'acc':
            accumulator += arg
            i += 1
        elif operation == 'jmp':
            i += arg
        elif operation == 'nop':
            i += 1
    terminated = i == len(a)
    _ , ans = terminated, accumulator
    print(ans)
