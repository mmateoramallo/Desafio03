import collections
import random

v = []
for i in range(15):
    num = random.randint(1,10)
    v.append(num)
print(v)
v_dict = collections.Counter(v)
print(v_dict)
v_dict_d = v_dict.keys()
cont = 0 
for i in range(len(v_dict_d)):
    cont +=1

print(cont)

#Obtengo los valores
v_dic_values = v_dict.values()