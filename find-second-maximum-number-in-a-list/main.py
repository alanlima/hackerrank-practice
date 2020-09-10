if __name__ == '__main__':
    n = int(input())

    arr = [ int(x) for x in set(input().split()) ]

    arr.sort()

    print(arr[-2])
