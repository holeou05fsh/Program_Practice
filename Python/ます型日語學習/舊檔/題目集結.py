import os
import json
import random

# a = os.path.exists('ます型題目(3字).json')
# print(a)  
dict_sum = {}
for i in range(11):
    if os.path.exists('ます型題目('+str(i+1)+'字).json'):
        with open('ます型題目('+str(i+1)+'字).json','r') as fp:
            a = json.load(fp)
        dict_sum.update(a)
        
with open('ます型題目(總和).json','w') as fp:
    json.dump(dict_sum, fp)        

with open('ます型題目(總和).json','r') as fp:
    a = json.load(fp)
    # print(a)
li = [i for i in a.keys()]
print(len(li))

# print(dict_sum)

# dict_list = [i for i in dict_sum.keys()]
# # print(dict_list)
# q_num = random.randint(0,len(dict_list))
# # print(q_num)
# if len(dict_sum[dict_list[q_num]]) == 1:
#     q_num2 = random.randint(0,0)
# else:
#     q_num2 = random.randint(0,len(dict_sum[dict_list[q_num]]))
# # print(q_num2)
# # print(dict_sum[dict_list[q_num]][q_num2])

# while len(dict_sum[dict_list[q_num]]) < 1:  
#     q_num = random.randint(0,len(dict_list))
#     if len(dict_sum[dict_list[q_num]]) == 1:
#         q_num2 = random.randint(0,0)
#     else:
#         q_num2 = random.randint(0,len(dict_sum[dict_list[q_num]]))

# print(dict_list[q_num])
# print(dict_sum[dict_list[q_num]][q_num2])