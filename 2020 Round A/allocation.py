tests = int(input())
for i in range(tests):
    N, B = [int(n) for n in input().split(" ")]
    cost = list(map(int, input().split(" ")))
    cost.sort()
    total = 0
    for house in range(N):
        total += cost[house]
        if (total > B):
            print("Case #"+str(i+1)+": "+str(house))
            break