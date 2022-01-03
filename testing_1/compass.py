def direction(facing, turn):
    list_res =['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    turns = turn // 45
    start = list_res.index(facing)
    end = (start + turns) % len(list_res)
    return list_res[end]


print(direction("S", 180))# --> N
print(direction("SE", -45))# --> E
