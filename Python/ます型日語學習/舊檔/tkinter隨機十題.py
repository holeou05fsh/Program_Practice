import tkinter as tk
import random
import json

with open('ます型二題以上(總和).json','r') as fp:
    a = json.load(fp)
li = [i for i in a.keys()]
list_num = random.sample(range(len(li)),10)
question_num = random.randint(0, len(a[li[list_num[0]]])-1)
question_num1 = random.randint(0, len(a[li[list_num[1]]])-1)
question_num2 = random.randint(0, len(a[li[list_num[2]]])-1)
question_num3 = random.randint(0, len(a[li[list_num[3]]])-1)
question_num4 = random.randint(0, len(a[li[list_num[4]]])-1)
question_num5 = random.randint(0, len(a[li[list_num[5]]])-1)
question_num6 = random.randint(0, len(a[li[list_num[6]]])-1)
question_num7 = random.randint(0, len(a[li[list_num[7]]])-1)
question_num8 = random.randint(0, len(a[li[list_num[8]]])-1)
question_num9 = random.randint(0, len(a[li[list_num[9]]])-1)


window = tk.Tk()
window.title('my window')
window.geometry('800x600')
window.config(background='skyblue')

var_su = tk.StringVar()
var_x = tk.StringVar()
var_Q = tk.StringVar()
var_dic = tk.StringVar()
var_dic1 = tk.StringVar()
var_dic2 = tk.StringVar()
var_dic3 = tk.StringVar()
var = tk.StringVar()
l = tk.Label(window,bg='skyblue',font=('新細明體',28),textvariable=var_Q
             ,width=90,height=8).place(x=0,y=0)
l2 = tk.Label(window,bg='skyblue',font=('新細明體',28)
             ,width=90,height=5)
l2.place(x=0,y=430)
l3 = tk.Label(window,bg='skyblue',fg='red',font=('新細明體',36),text='隨機十題').place(x=36,y=36)

def answer():
    answer = str(var.get())
    if x == dic[answer]:
        l2.config(textvariable=var_su,fg='green')
        l2.place(x=0,y=430)
    else:
        l2.config(textvariable=var_x,fg='red')
        l2.place(x=0,y=430)
def Radiobutton():
    r1 = tk.Radiobutton(window, textvariable=var_dic,font=('新細明體',24),
                        bg='skyblue',variable=var, value='A',
                        command=answer)
    r1.place(x=80,y=300)
    r2 = tk.Radiobutton(window, textvariable=var_dic1,font=('新細明體',24),
                        bg='skyblue',variable=var, value='B',
                        command=answer)
    r2.place(x=450,y=300)
    r3 = tk.Radiobutton(window, textvariable=var_dic2,font=('新細明體',24),
                        bg='skyblue',variable=var, value='C',
                        command=answer)
    r3.place(x=850,y=300)
    r4 = tk.Radiobutton(window, textvariable=var_dic3,font=('新細明體',24),
                        bg='skyblue',variable=var, value='D',
                        command=answer)
    r4.place(x=1250,y=300)
    r1.deselect()
    r2.deselect()
    r3.deselect()
    r4.deselect()
    
    
def question():
    l2.place_forget()
    Radiobutton()
    b.configure(fg="yellow")     
    global x
    x = li[list_num[0]]
    var_x.set('錯誤 X\n\n'+" 正確答案： "+x)
    question = a[x]
    q = question[question_num]
    L = random.sample(range(0, 4), 4)
    
    li_num = random.sample(range(0, len(li)), 3)
    while list_num in li_num:
        li_num = random.sample(range(0, len(li)), 3)
    
    list =[x,li[li_num[0]],li[li_num[1]],li[li_num[2]]]
    global dic
    dic = {'A':list[L[0]],'B':list[L[1]],'C':list[L[2]],'D':list[L[3]]}
    var_dic.set('A.'+ dic['A'])
    var_dic1.set('B.'+ dic['B'])
    var_dic2.set('C.'+ dic['C'])
    var_dic3.set('D.'+ dic['D'])
    global Q
    Q = q.replace(x,'_'*len(x))
    var_Q.set(Q)
    var_su.set('正確 O')
def question1():
    l2.place_forget()
    Radiobutton()
    b1.configure(fg="yellow") 
    global x
    x = li[list_num[1]]
    var_x.set('錯誤 X\n\n'+" 正確答案： "+x)
    question = a[x]
    q = question[question_num1]
    L = random.sample(range(0, 4), 4)
    
    li_num = random.sample(range(0, len(li)), 3)
    while list_num in li_num:
        li_num = random.sample(range(0, len(li)), 3)
    
    list =[x,li[li_num[0]],li[li_num[1]],li[li_num[2]]]
    global dic
    dic = {'A':list[L[0]],'B':list[L[1]],'C':list[L[2]],'D':list[L[3]]}
    var_dic.set('A.'+ dic['A'])
    var_dic1.set('B.'+ dic['B'])
    var_dic2.set('C.'+ dic['C'])
    var_dic3.set('D.'+ dic['D'])
    global Q
    Q = q.replace(x,'_'*len(x))
    var_Q.set(Q)
    var_su.set('正確 O')
def question2():
    l2.place_forget()
    Radiobutton()
    b2.configure(fg="yellow") 
    global x
    x = li[list_num[2]]
    var_x.set('錯誤 X\n\n'+" 正確答案： "+x)
    question = a[x]
    q = question[question_num2]
    L = random.sample(range(0, 4), 4)
    
    li_num = random.sample(range(0, len(li)), 3)
    while list_num in li_num:
        li_num = random.sample(range(0, len(li)), 3)
    
    list =[x,li[li_num[0]],li[li_num[1]],li[li_num[2]]]
    global dic
    dic = {'A':list[L[0]],'B':list[L[1]],'C':list[L[2]],'D':list[L[3]]}
    var_dic.set('A.'+ dic['A'])
    var_dic1.set('B.'+ dic['B'])
    var_dic2.set('C.'+ dic['C'])
    var_dic3.set('D.'+ dic['D'])
    global Q
    Q = q.replace(x,'_'*len(x))
    var_Q.set(Q)
    var_su.set('正確 O')
def question3():
    l2.place_forget()
    Radiobutton()
    b3.configure(fg="yellow") 
    global x
    x = li[list_num[3]]
    var_x.set('錯誤 X\n\n'+" 正確答案： "+x)
    question = a[x]
    q = question[question_num3]
    L = random.sample(range(0, 4), 4)
    
    li_num = random.sample(range(0, len(li)), 3)
    while list_num in li_num:
        li_num = random.sample(range(0, len(li)), 3)
    
    list =[x,li[li_num[0]],li[li_num[1]],li[li_num[2]]]
    global dic
    dic = {'A':list[L[0]],'B':list[L[1]],'C':list[L[2]],'D':list[L[3]]}
    var_dic.set('A.'+ dic['A'])
    var_dic1.set('B.'+ dic['B'])
    var_dic2.set('C.'+ dic['C'])
    var_dic3.set('D.'+ dic['D'])
    global Q
    Q = q.replace(x,'_'*len(x))
    var_Q.set(Q)
    var_su.set('正確 O')
def question4():
    l2.place_forget()
    Radiobutton()
    b4.configure(fg="yellow") 
    global x
    x = li[list_num[4]]
    var_x.set('錯誤 X\n\n'+" 正確答案： "+x)
    question = a[x]
    q = question[question_num4]
    L = random.sample(range(0, 4), 4)
    
    li_num = random.sample(range(0, len(li)), 3)
    while list_num in li_num:
        li_num = random.sample(range(0, len(li)), 3)
    
    list =[x,li[li_num[0]],li[li_num[1]],li[li_num[2]]]
    global dic
    dic = {'A':list[L[0]],'B':list[L[1]],'C':list[L[2]],'D':list[L[3]]}
    var_dic.set('A.'+ dic['A'])
    var_dic1.set('B.'+ dic['B'])
    var_dic2.set('C.'+ dic['C'])
    var_dic3.set('D.'+ dic['D'])
    global Q
    Q = q.replace(x,'_'*len(x))
    var_Q.set(Q)
    var_su.set('正確 O')
def question5():
    l2.place_forget()
    Radiobutton()
    b5.configure(fg="yellow") 
    global x
    x = li[list_num[5]]
    var_x.set('錯誤 X\n\n'+" 正確答案： "+x)
    question = a[x]
    q = question[question_num5]
    L = random.sample(range(0, 4), 4)
    
    li_num = random.sample(range(0, len(li)), 3)
    while list_num in li_num:
        li_num = random.sample(range(0, len(li)), 3)
    
    list =[x,li[li_num[0]],li[li_num[1]],li[li_num[2]]]
    global dic
    dic = {'A':list[L[0]],'B':list[L[1]],'C':list[L[2]],'D':list[L[3]]}
    var_dic.set('A.'+ dic['A'])
    var_dic1.set('B.'+ dic['B'])
    var_dic2.set('C.'+ dic['C'])
    var_dic3.set('D.'+ dic['D'])
    global Q
    Q = q.replace(x,'_'*len(x))
    var_Q.set(Q)
    var_su.set('正確 O')
def question6():
    l2.place_forget()
    Radiobutton()
    b6.configure(fg="yellow") 
    global x
    x = li[list_num[6]]
    var_x.set('錯誤 X\n\n'+" 正確答案： "+x)
    question = a[x]
    q = question[question_num6]
    L = random.sample(range(0, 4), 4)
    
    li_num = random.sample(range(0, len(li)), 3)
    while list_num in li_num:
        li_num = random.sample(range(0, len(li)), 3)
    
    list =[x,li[li_num[0]],li[li_num[1]],li[li_num[2]]]
    global dic
    dic = {'A':list[L[0]],'B':list[L[1]],'C':list[L[2]],'D':list[L[3]]}
    var_dic.set('A.'+ dic['A'])
    var_dic1.set('B.'+ dic['B'])
    var_dic2.set('C.'+ dic['C'])
    var_dic3.set('D.'+ dic['D'])
    global Q
    Q = q.replace(x,'_'*len(x))
    var_Q.set(Q)
    var_su.set('正確 O')
def question7():
    l2.place_forget()
    Radiobutton()
    b7.configure(fg="yellow") 
    global x
    x = li[list_num[7]]
    var_x.set('錯誤 X\n\n'+" 正確答案： "+x)
    question = a[x]
    q = question[question_num7]
    L = random.sample(range(0, 4), 4)
    
    li_num = random.sample(range(0, len(li)), 3)
    while list_num in li_num:
        li_num = random.sample(range(0, len(li)), 3)
    
    list =[x,li[li_num[0]],li[li_num[1]],li[li_num[2]]]
    global dic
    dic = {'A':list[L[0]],'B':list[L[1]],'C':list[L[2]],'D':list[L[3]]}
    var_dic.set('A.'+ dic['A'])
    var_dic1.set('B.'+ dic['B'])
    var_dic2.set('C.'+ dic['C'])
    var_dic3.set('D.'+ dic['D'])
    global Q
    Q = q.replace(x,'_'*len(x))
    var_Q.set(Q)
    var_su.set('正確 O')
def question8():
    l2.place_forget()
    Radiobutton()
    b8.configure(fg="yellow") 
    global x
    x = li[list_num[8]]
    var_x.set('錯誤 X\n\n'+" 正確答案： "+x)
    question = a[x]
    q = question[question_num8]
    L = random.sample(range(0, 4), 4)
    
    li_num = random.sample(range(0, len(li)), 3)
    while list_num in li_num:
        li_num = random.sample(range(0, len(li)), 3)
    
    list =[x,li[li_num[0]],li[li_num[1]],li[li_num[2]]]
    global dic
    dic = {'A':list[L[0]],'B':list[L[1]],'C':list[L[2]],'D':list[L[3]]}
    var_dic.set('A.'+ dic['A'])
    var_dic1.set('B.'+ dic['B'])
    var_dic2.set('C.'+ dic['C'])
    var_dic3.set('D.'+ dic['D'])
    global Q
    Q = q.replace(x,'_'*len(x))
    var_Q.set(Q)
    var_su.set('正確 O')
def question9():
    l2.place_forget()
    Radiobutton()
    b9.configure(fg="yellow") 
    global x
    x = li[list_num[9]]
    var_x.set('錯誤 X\n\n'+" 正確答案： "+x)
    question = a[x]
    q = question[question_num9]
    L = random.sample(range(0, 4), 4)
    
    li_num = random.sample(range(0, len(li)), 3)
    while list_num in li_num:
        li_num = random.sample(range(0, len(li)), 3)
    
    list =[x,li[li_num[0]],li[li_num[1]],li[li_num[2]]]
    global dic
    dic = {'A':list[L[0]],'B':list[L[1]],'C':list[L[2]],'D':list[L[3]]}
    var_dic.set('A.'+ dic['A'])
    var_dic1.set('B.'+ dic['B'])
    var_dic2.set('C.'+ dic['C'])
    var_dic3.set('D.'+ dic['D'])
    global Q
    Q = q.replace(x,'_'*len(x))
    var_Q.set(Q)
    var_su.set('正確 O')

b = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font=("arial 26",32),text="㊀",pady=10,command=question)
b.place(x=180,y=669)
b1 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font=("arial 26",32),text="㊁",pady=10,command=question1)
b1.place(x=310,y=669)
b2 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font=("arial 26",32),text="㊂",pady=10,command=question2)
b2.place(x=440,y=669)
b3 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font=("arial 26",32),text="㊃",pady=10,command=question3)
b3.place(x=570,y=669)
b4 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font=("arial 26",32),text="㊄",pady=10,command=question4)
b4.place(x=700,y=669)
b5 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font=("arial 26",32),text="㊅",pady=10,command=question5)
b5.place(x=830,y=669)
b6 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font=("arial 26",32),text="㊆",pady=10,command=question6)
b6.place(x=960,y=669)
b7 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font=("arial 26",32),text="㊇",pady=10,command=question7)
b7.place(x=1090,y=669)
b8 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font=("arial 26",32),text="㊈",pady=10,command=question8)
b8.place(x=1210,y=669)
b9 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font=("arial 26",32),text="㊉",pady=10,command=question9)
b9.place(x=1350,y=669)



window.mainloop()