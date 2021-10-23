import tkinter as tk
import json
import random


window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var_sw = tk.StringVar()
l = tk.Label(window, textvariable=var_sw, bg='green', font=('Arial', 12), width=15,
             height=2).pack()


with open('ます型二題以上(總和)(含翻譯).json', 'r',encoding='utf-8') as fp:
    c = json.load(fp)
    
single_list = [i for i in c.keys()]
num_sw = random.sample(range(len(single_list)),5)
num_qu = random.sample(range(len(c[single_list[num_sw[0]]])),2)
# print(num_qu)


def hit_me():
    sw = '234'+single_list[num_sw[0]]
    qu_1 = list(c[single_list[num_sw[0]]][num_qu[0]].keys())[0]
    qu_tl_1 = c[single_list[num_sw[0]]][num_qu[0]][list(c[single_list[num_sw[0]]][num_qu[0]].keys())[0]]
    qu_2 = list(c[single_list[num_sw[0]]][num_qu[1]].keys())[0]
    qu_tl_2 = c[single_list[num_sw[0]]][num_qu[1]][list(c[single_list[num_sw[0]]][num_qu[1]].keys())[0]]
    var_sw.set(sw)
def hit_me1():
    sw = single_list[num_sw[1]]
    qu_1 = list(c[single_list[num_sw[0]]][num_qu[0]].keys())[0]
    qu_tl_1 = c[single_list[num_sw[0]]][num_qu[0]][list(c[single_list[num_sw[0]]][num_qu[0]].keys())[0]]
    qu_2 = list(c[single_list[num_sw[0]]][num_qu[1]].keys())[0]
    qu_tl_2 = c[single_list[num_sw[0]]][num_qu[1]][list(c[single_list[num_sw[0]]][num_qu[1]].keys())[0]]
    var_sw.set(sw)
def hit_me2():
    sw = single_list[num_sw[2]]
    qu_1 = list(c[single_list[num_sw[0]]][num_qu[0]].keys())[0]
    qu_tl_1 = c[single_list[num_sw[0]]][num_qu[0]][list(c[single_list[num_sw[0]]][num_qu[0]].keys())[0]]
    qu_2 = list(c[single_list[num_sw[0]]][num_qu[1]].keys())[0]
    qu_tl_2 = c[single_list[num_sw[0]]][num_qu[1]][list(c[single_list[num_sw[0]]][num_qu[1]].keys())[0]]
    var_sw.set(sw)


b = tk.Button(window, text='1', width=15,
              height=2, command=hit_me).pack()
b1 = tk.Button(window, text='2', width=15,
              height=2, command=hit_me1).pack()
b2 = tk.Button(window, text='3', width=15,
              height=2, command=hit_me2).pack()
print(type(var_sw),var_sw)
window.mainloop()