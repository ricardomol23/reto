matriz1 = [
    [43, 12, 53],
    [42, 43, 71],
    [21, 67, 82]
]

transpuesta2 = list(map(list, zip(*matriz1)))
print(transpuesta2)