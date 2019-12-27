def solution(progresses, speeds):
    work_days = []
    answer = []
    for i,progress in enumerate(progresses):
        if (100-progress)%speeds[i] != 0:
            work_days.append(int((100-progress)/speeds[i])+1)
        else:
            work_days.append(int((100-progress)/speeds[i]))
    tmp=0
    cnt=1
    while work_days:
        tmp=work_days.pop(0)
        if not work_days:
            answer.append(cnt)
            break
        else:
            while work_days and tmp >= work_days[0] :
                work_days.pop(0)
                cnt += 1
        answer.append(cnt)
        cnt=1
    return answer