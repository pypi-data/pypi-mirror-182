def ispalin(string,onlylow=True):
    temp_list= [[],[]]
    if onlylow:
        for i in string.lower():
            temp_list[0].append(i)
    elif onlylow == False:
        for i in string:
            temp_list[0].append(i)
    temp_list[1]=temp_list[0][::-1]
    if temp_list[0] == temp_list[1]: return True
    else: return False