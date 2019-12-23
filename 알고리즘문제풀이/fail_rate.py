def solution(N, stages):
    stages.sort(reverse = False)
    fail_rate = {}
    for stage in range(1,N+1):
        fail_rate[stage]=(stages.count(stage)/len(stages))
        if stage in stages:
            while stage in stages:
                stages.remove(stage)
    return sorted(fail_rate, key=lambda x : fail_rate[x], reverse=True)

# while문 땜에 시간 효율성 떨어짐