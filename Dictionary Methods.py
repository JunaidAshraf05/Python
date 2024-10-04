ep1 = {122:33,455:55,6666:444}
ep2 = {222:3333 , 55555:55555}
ep1.update(ep2)
print(ep1)

# if you want to clear ep1
ep1.clear(ep1)
#if you want to remove any pair in dic 
ep1.pop(455)
print(ep1)

del ep1[122]
print(ep1)