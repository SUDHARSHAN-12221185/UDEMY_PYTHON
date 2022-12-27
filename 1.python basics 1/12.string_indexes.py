selfish="01234567"
       # 01234567
       # 87654321  in negetives

print(selfish[0])
print(selfish[7])


''' string slicing'''
#[start:stop:stepover or increment or decrement]        stop in not including
print(selfish[0:7])
print(selfish[0:7:2])

print(selfish[1:]) #it starts from start to end
print(selfish[:5])#it starts form 0 to stop 
print(selfish[::2])# it step over two


print(selfish[-1]) #prints from last
print(selfish[::-1])#it is stepover -1 so reverses string 
