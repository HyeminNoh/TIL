def solution(s):
    answer_list=[]
    for letter in s:
        if answer_list and answer_list[-1]==letter:
                answer_list.pop()
        else:
            answer_list.append(letter)
    if not answer_list:
        return 1
    if answer_list:
        return 0