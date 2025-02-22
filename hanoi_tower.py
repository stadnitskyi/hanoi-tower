def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Перемістіть диск з {source} на {target}")
        return
    hanoi(n-1, source, auxiliary, target)
    print(f"Перемістіть диск з {source} на {target}")
    hanoi(n-1, auxiliary, target, source)
