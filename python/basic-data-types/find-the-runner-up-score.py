if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newlist = set(list(arr))
    newlist.remove(max(newlist))
    print(max(newlist))
