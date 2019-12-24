# 한개의 테스트 케이스에서 시간초과 발생
def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights[::-1]
    on_bridge=[0]*bridge_length
    time=0
    while truck_weights:
        time+=1
        on_bridge.pop(0)
        if sum(on_bridge)+truck_weights[-1]<=weight:
            on_bridge.append(truck_weights.pop())
        else:
            on_bridge.append(0)
    return time+bridge_length