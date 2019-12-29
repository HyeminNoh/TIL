def solution(skill, skill_trees):
    skill = list(skill)
    count = len(skill_trees)
    for tree in skill_trees:
        index=[]
        tree = list(tree)
        for skill_order in skill:
            if skill_order in tree:
                index.append(tree.index(skill_order))
            else:
                index.append(len(tree))
        if sorted(index)!=index:
            count-=1
    return count