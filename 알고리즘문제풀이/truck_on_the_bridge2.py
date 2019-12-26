'''
sum 함수를 대체하여 on_bridge_weight이라는 변수 생성
다리 위 무게를 체크하도록 함! 
-> 시간복잡도 줄임
'''

def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights[::-1]
    on_bridge = [0]*bridge_length
    time = 0
    on_bridge_weight = 0
    while truck_weights:
        time+=1
        out = on_bridge.pop(0)
        if out != 0:
            on_bridge_weight -= out
        if on_bridge_weight+truck_weights[-1]<=weight:
            go_in = truck_weights.pop()
            on_bridge.append(go_in)
            if go_in != 0:
                on_bridge_weight += go_in
        else:
            on_bridge.append(0)
    return time+bridge_length