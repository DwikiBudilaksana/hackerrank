def myFunc(e):
    return e[1]

if __name__ == '__main__':
    list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name, score])
        
    list.sort(key=myFunc)
    secMin = 1
    newList = []
    for i in range(1, len(list)):
        if list[0][1] == list[i][1]:
            secMin += 1
        elif list[i][1] == list[secMin][1]:
            newList.append(list[i][0])
    
    newList.sort()
    for x in newList:
        print(x)