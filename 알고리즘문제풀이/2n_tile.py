def solution(n):
    lst = []
    for rpt in range(0, n+1):
        if rpt < 2:
            lst.append(1)
        else:
            lst.append((lst[rpt-1] + lst[rpt-2])% 1000000007)
    return lst[n]
