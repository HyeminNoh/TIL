def solution(arr):
    answer = []
    for v in arr:
        if not answer:
            answer.append(v)
        else:
            if pre_v != v:
                answer.append(v)
        pre_v = v
    return answer