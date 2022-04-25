def bar(i):
    i = i + 1
    if i == 80:
        return None
    print(i)
    bar(i)

bar(5)

