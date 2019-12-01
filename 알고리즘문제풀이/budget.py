def solution(d, budget):
    answer=0
    d.sort()
    for cost in d:
        budget -= cost
        answer += 1
        if budget < 0:
            answer -=1
            break
    return answer