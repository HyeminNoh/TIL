def solution(arrangement):
    answer = 0
    cut=arrangement.replace('()','0')
    bar=0
    
    for i in cut:
        if i=='(':
            bar += 1
        elif i == '0' :
            answer += bar
        else:
            bar -= 1
            answer += 1
    return answer