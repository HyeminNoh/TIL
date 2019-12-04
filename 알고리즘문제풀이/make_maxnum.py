def solution(number, k):
    result = []
    for n in number:
        while result and result[-1] < n and k > 0:
            result.pop()
            k -= 1
        result.append(n)
    while k > 0:
        result.pop()
        k-=1
    return "".join(result)