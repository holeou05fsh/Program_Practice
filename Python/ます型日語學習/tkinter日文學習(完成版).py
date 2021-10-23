import tkinter as tk
import json
import random
from gtts import gTTS
from pygame import mixer
import tempfile

#%%------------------------------每日五單字------------------------------

with open('ます型二題以上(總和)(含翻譯).json', 'r',encoding='utf-8') as fp:
    c = json.load(fp)

window = tk.Tk()
window.title('JapanLesson')
window.geometry('1500x850')
window.minsize(width=300, height=200)
window.config(background='skyblue')
window.iconbitmap('01.ico')

single_list = [i for i in c.keys()]
num_sw = random.sample(range(len(single_list)),5)
num_qu = random.sample(range(len(c[single_list[num_sw[0]]])),2)
num_qu1 = random.sample(range(len(c[single_list[num_sw[1]]])),2)
num_qu2 = random.sample(range(len(c[single_list[num_sw[2]]])),2)
num_qu3 = random.sample(range(len(c[single_list[num_sw[3]]])),2)
num_qu4 = random.sample(range(len(c[single_list[num_sw[4]]])),2)

var_sw = tk.StringVar()
p_var_sw = tk.StringVar()
var_qu = tk.StringVar()
var_qu_1 = tk.StringVar()
var_qu_2 = tk.StringVar()
var_qu_tl_2 = tk.StringVar()
var_sw_m = tk.StringVar()

l = tk.Label(window,fg='#3A0088',bg='skyblue',font=('新細明體',24),height=6,width=10)
l.grid(row=0,column=0,padx=80)  #,padx=100
l_1 = tk.Label(window,textvariable=p_var_sw,fg='#3A0088',bg='skyblue',font=('新細明體',24))
l_1.place(x=60,y=195)

l2 = tk.Label(window,textvariable=var_sw_m,fg='#3A0088',bg='skyblue',font=('新細明體',15),justify = 'left',height=25,width=50,anchor='w')#
l2.grid(row=0,column=1, sticky=tk.N)

l4 = tk.Label(window,textvariable=var_qu,relief="sunken",bg='#DDDDDD',font=('新細明體',20),justify = 'left',height=6,width=60,anchor='w')
l4.grid(row=1,column=1)

def sw_page():
    global sw
    global qu_1
    global qu_2
    sw = single_list[num_sw[0]]
    qu_1 = list(c[single_list[num_sw[0]]][num_qu[0]].keys())[0]
    qu_tl_1 = c[single_list[num_sw[0]]][num_qu[0]][list(c[single_list[num_sw[0]]][num_qu[0]].keys())[0]]
    qu_2 = list(c[single_list[num_sw[0]]][num_qu[1]].keys())[0]
    qu_tl_2 = c[single_list[num_sw[0]]][num_qu[1]][list(c[single_list[num_sw[0]]][num_qu[1]].keys())[0]]
    with open('ます型二題以上(總和)(意思)/'+ sw +'.txt', 'r',encoding='utf-8') as fp:
        a = '\n'+'\n'+fp.read()
    var_sw.set(sw)
    p_var_sw.set('ます型：\n\n' + sw)
    var_qu.set('\n'+' ①   '+ qu_1 +'\n'+'        '+ qu_tl_1 +'\n'+'\n'+' ②   '+ qu_2 +'\n'+'        '+ qu_tl_2 +'\n')
    var_sw_m.set(a)
def sw_page1():
    global sw
    global qu_1
    global qu_2
    sw = single_list[num_sw[1]]
    qu_1 = list(c[single_list[num_sw[1]]][num_qu1[0]].keys())[0]
    qu_tl_1 = c[single_list[num_sw[1]]][num_qu1[0]][list(c[single_list[num_sw[1]]][num_qu1[0]].keys())[0]]
    qu_2 = list(c[single_list[num_sw[1]]][num_qu1[1]].keys())[0]
    qu_tl_2 = c[single_list[num_sw[1]]][num_qu1[1]][list(c[single_list[num_sw[1]]][num_qu1[1]].keys())[0]]
    with open('ます型二題以上(總和)(意思)/'+ sw +'.txt', 'r',encoding='utf-8') as fp:
        a = '\n'+'\n'+fp.read()
    var_sw.set(sw)
    p_var_sw.set('ます型：\n\n' + sw)
    var_qu.set('\n'+' ①  '+ qu_1 +'\n'+'       '+ qu_tl_1 +'\n'+'\n'+' ②  '+ qu_2 +'\n'+'       '+ qu_tl_2 +'\n')
    var_sw_m.set(a)
def sw_page2():
    global sw
    global qu_1
    global qu_2
    sw = single_list[num_sw[2]]
    qu_1 = list(c[single_list[num_sw[2]]][num_qu2[0]].keys())[0]
    qu_tl_1 = c[single_list[num_sw[2]]][num_qu2[0]][list(c[single_list[num_sw[2]]][num_qu2[0]].keys())[0]]
    qu_2 = list(c[single_list[num_sw[2]]][num_qu2[1]].keys())[0]
    qu_tl_2 = c[single_list[num_sw[2]]][num_qu2[1]][list(c[single_list[num_sw[2]]][num_qu2[1]].keys())[0]]
    with open('ます型二題以上(總和)(意思)/'+ sw +'.txt', 'r',encoding='utf-8') as fp:
        a = '\n'+'\n'+fp.read()
    var_sw.set(sw)
    p_var_sw.set('ます型：\n\n' + sw)
    var_qu.set('\n'+' ①   '+ qu_1 +'\n'+'        '+ qu_tl_1 +'\n'+'\n'+' ②   '+ qu_2 +'\n'+'        '+ qu_tl_2 +'\n')
    var_sw_m.set(a)
def sw_page3():
    global sw
    global qu_1
    global qu_2
    sw = single_list[num_sw[3]]
    qu_1 = list(c[single_list[num_sw[3]]][num_qu3[0]].keys())[0]
    qu_tl_1 = c[single_list[num_sw[3]]][num_qu3[0]][list(c[single_list[num_sw[3]]][num_qu3[0]].keys())[0]]
    qu_2 = list(c[single_list[num_sw[3]]][num_qu3[1]].keys())[0]
    qu_tl_2 = c[single_list[num_sw[3]]][num_qu3[1]][list(c[single_list[num_sw[3]]][num_qu3[1]].keys())[0]]
    with open('ます型二題以上(總和)(意思)/'+ sw +'.txt', 'r',encoding='utf-8') as fp:
        a = '\n'+'\n'+fp.read()
    var_sw.set(sw)
    p_var_sw.set('ます型：\n\n' + sw)
    var_qu.set('\n'+' ①   '+ qu_1 +'\n'+'        '+ qu_tl_1 +'\n'+'\n'+' ②   '+ qu_2 +'\n'+'        '+ qu_tl_2 +'\n')
    var_sw_m.set(a)
def sw_page4():
    global sw
    global qu_1
    global qu_2
    sw = single_list[num_sw[4]]
    qu_1 = list(c[single_list[num_sw[4]]][num_qu4[0]].keys())[0]
    qu_tl_1 = c[single_list[num_sw[4]]][num_qu4[0]][list(c[single_list[num_sw[4]]][num_qu4[0]].keys())[0]]
    qu_2 = list(c[single_list[num_sw[4]]][num_qu4[1]].keys())[0]
    qu_tl_2 = c[single_list[num_sw[4]]][num_qu4[1]][list(c[single_list[num_sw[4]]][num_qu4[1]].keys())[0]]
    with open('ます型二題以上(總和)(意思)/'+ sw +'.txt', 'r',encoding='utf-8') as fp:
        a = '\n'+'\n'+fp.read()
    var_sw.set(sw)
    p_var_sw.set('ます型：\n\n' + sw)
    var_qu.set('\n'+' ①   '+ qu_1 +'\n'+'        '+ qu_tl_1 +'\n'+'\n'+' ②   '+ qu_2 +'\n'+'        '+ qu_tl_2 +'\n')
    var_sw_m.set(a)

def speak(single_word):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=single_word,lang="ja")
        tts.save("{}.mp3".format(fp.name))
        mixer.init()
        mixer.music.load("{}.mp3".format(fp.name))
        mixer.music.set_volume(0.1)
        mixer.music.play()
def sen():
        speak( sw )
def sen1():
        speak( qu_1 )
def sen2():
        speak(qu_2 )

p = tk.Button(window,bd=0,relief="ridge",compound=tk.CENTER,
    bg="skyblue",fg="red",activeforeground="pink",activebackground="skyblue",
    font="arial 26",text="㊀ "+single_list[num_sw[0]] ,pady=10,command=sw_page).place(x=1200,y=30)
p1 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="red",activeforeground="pink",activebackground="skyblue",
    font="arial 26",text="㊁ "+single_list[num_sw[1]],pady=10,command=sw_page1).place(x=1200,y=100)
p2 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="red",activeforeground="pink",activebackground="skyblue",
    font="arial 26",text="㊂ "+single_list[num_sw[2]],pady=10,command=sw_page2).place(x=1200,y=170)
p3 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="red",activeforeground="pink",activebackground="skyblue",
    font="arial 26",text="㊃ "+single_list[num_sw[3]],pady=10,command=sw_page3).place(x=1200,y=240)
p4 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="red",activeforeground="pink",activebackground="skyblue",
    font="arial 26",text="㊄ "+single_list[num_sw[4]],pady=10,command=sw_page4).place(x=1200,y=320)
s = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="red",activeforeground="pink",activebackground="skyblue",
    font="arial 26",text="🔊",pady=10,command=sen).place(x=0,y=169)
s1 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="red",activeforeground="pink",activebackground="skyblue",
    font="arial 26",text="🔊",pady=10,command=sen1).place(x=260,y=570)
s2 = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="red",activeforeground="pink",activebackground="skyblue",
    font="arial 26",text="🔊",pady=10,command=sen2).place(x=260,y=650)

photo1 = tk.PhotoImage(file='例句.png')
l3 = tk.Label(window,image=photo1,bg='skyblue')
l3.grid(row=1,column=0)

photo2 = tk.PhotoImage(file='01.png')
l4 = tk.Label(window,image=photo2,bg='skyblue')
l4.place(x=50,y=330)

photo = tk.PhotoImage(file='每日五單字.png')
l5 = tk.Label(window,image=photo,bg='skyblue')
l5.grid(row=1,column=2,ipadx=50)
 
def image(smp):
    img = tk.PhotoImage(file="red1.png")
    img = img.subsample(smp, smp)
    return img

#%%--------------------------------隨機十題--------------------------------
def random_tenquestion():
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
        
        
        toplevel = tk.Toplevel()
        toplevel.title('隨機十題')
        toplevel.geometry('800x800+200+50')
        toplevel.config(background='skyblue')
        
        var_su = tk.StringVar()
        var_x = tk.StringVar()
        var_Q = tk.StringVar()
        var_dic = tk.StringVar()
        var_dic1 = tk.StringVar()
        var_dic2 = tk.StringVar()
        var_dic3 = tk.StringVar()
        var = tk.StringVar()
        l = tk.Label(toplevel,bg='skyblue',font=('新細明體',28),textvariable=var_Q
                     ,width=90,height=8).place(x=0,y=0)
        l2 = tk.Label(toplevel,bg='skyblue',font=('新細明體',28)
                     ,width=90,height=5)
        l2.place(x=0,y=430)
        l3 = tk.Label(toplevel,bg='skyblue',fg='red',font=('新細明體',36),text='隨機十題').place(x=36,y=36)

        def answer():
            answer = str(var.get())
            if x == dic[answer]:
                l2.config(textvariable=var_su,fg='green')
                l2.place(x=0,y=430)
            else:
                l2.config(textvariable=var_x,fg='red')
                l2.place(x=0,y=430)
        def Radiobutton():
            r1 = tk.Radiobutton(toplevel, textvariable=var_dic,font=('新細明體',24),
                                bg='skyblue',variable=var, value='A',
                                command=answer)
            r1.place(x=80,y=300)
            r2 = tk.Radiobutton(toplevel, textvariable=var_dic1,font=('新細明體',24),
                                bg='skyblue',variable=var, value='B',
                                command=answer)
            r2.place(x=450,y=300)
            r3 = tk.Radiobutton(toplevel, textvariable=var_dic2,font=('新細明體',24),
                                bg='skyblue',variable=var, value='C',
                                command=answer)
            r3.place(x=850,y=300)
            r4 = tk.Radiobutton(toplevel, textvariable=var_dic3,font=('新細明體',24),
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
        
        b = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
            bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
            font=("arial 26",32),text="㊀",pady=10,command=question)
        b.place(x=180,y=669)
        b1 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
            bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
            font=("arial 26",32),text="㊁",pady=10,command=question1)
        b1.place(x=310,y=669)
        b2 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
            bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
            font=("arial 26",32),text="㊂",pady=10,command=question2)
        b2.place(x=440,y=669)
        b3 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
            bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
            font=("arial 26",32),text="㊃",pady=10,command=question3)
        b3.place(x=570,y=669)
        b4 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
            bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
            font=("arial 26",32),text="㊄",pady=10,command=question4)
        b4.place(x=700,y=669)
        b5 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
            bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
            font=("arial 26",32),text="㊅",pady=10,command=question5)
        b5.place(x=830,y=669)
        b6 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
            bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
            font=("arial 26",32),text="㊆",pady=10,command=question6)
        b6.place(x=960,y=669)
        b7 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
            bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
            font=("arial 26",32),text="㊇",pady=10,command=question7)
        b7.place(x=1090,y=669)
        b8 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
            bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
            font=("arial 26",32),text="㊈",pady=10,command=question8)
        b8.place(x=1210,y=669)
        b9 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
            bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
            font=("arial 26",32),text="㊉",pady=10,command=question9)
        b9.place(x=1350,y=669)


but = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font="arial 26",text="隨機十題",pady=10,command=random_tenquestion)
img = image(2) # 1=normal, 2=small, 3=smallest
but.config(image=img)
but.place(x=30,y=30)

#%%------------------------------每日五單字測試------------------------------
def evertdayfivesw_test():
    with open('ます型二題以上(總和).json','r') as fp:
        a = json.load(fp)

    li = [i for i in a.keys()]
    list_num = num_sw*2
    question_num = random.sample(range(len(a[single_list[num_sw[0]]])),2)[0]
    question_num1 = random.sample(range(len(a[single_list[num_sw[1]]])),2)[0]
    question_num2 = random.sample(range(len(a[single_list[num_sw[2]]])),2)[0]
    question_num3 = random.sample(range(len(a[single_list[num_sw[3]]])),2)[0]
    question_num4 = random.sample(range(len(a[single_list[num_sw[4]]])),2)[0]
    question_num5 = random.sample(range(len(a[single_list[num_sw[0]]])),2)[1]
    question_num6 = random.sample(range(len(a[single_list[num_sw[1]]])),2)[1]
    question_num7 = random.sample(range(len(a[single_list[num_sw[2]]])),2)[1]
    question_num8 = random.sample(range(len(a[single_list[num_sw[3]]])),2)[1]
    question_num9 = random.sample(range(len(a[single_list[num_sw[4]]])),2)[1]
    
    toplevel = tk.Toplevel()
    toplevel.title('每日五單字測試')
    toplevel.geometry('800x800+500+50')
    toplevel.config(background='skyblue')
    
    var_su = tk.StringVar()
    var_x = tk.StringVar()
    var_Q = tk.StringVar()
    var_dic = tk.StringVar()
    var_dic1 = tk.StringVar()
    var_dic2 = tk.StringVar()
    var_dic3 = tk.StringVar()
    var = tk.StringVar()
    l = tk.Label(toplevel,bg='skyblue',font=('新細明體',28),textvariable=var_Q
                 ,width=90,height=8).place(x=0,y=0)
    l2 = tk.Label(toplevel,bg='skyblue',font=('新細明體',28)
                 ,width=90,height=5)
    l2.place(x=0,y=430)
    l3 = tk.Label(toplevel,bg='skyblue',fg='red',font=('新細明體',36),text='每日五單字測試').place(x=36,y=36)
    
    def answer():
        answer = str(var.get())
        if x == dic[answer]:
            l2.config(textvariable=var_su,fg='green')
            l2.place(x=0,y=430)
        else:
            l2.config(textvariable=var_x,fg='red')
            l2.place(x=0,y=430)
    def Radiobutton():
        r1 = tk.Radiobutton(toplevel, textvariable=var_dic,font=('新細明體',24),
                            bg='skyblue',variable=var, value='A',
                            command=answer)
        r1.place(x=80,y=300)
        r2 = tk.Radiobutton(toplevel, textvariable=var_dic1,font=('新細明體',24),
                            bg='skyblue',variable=var, value='B',
                            command=answer)
        r2.place(x=450,y=300)
        r3 = tk.Radiobutton(toplevel, textvariable=var_dic2,font=('新細明體',24),
                            bg='skyblue',variable=var, value='C',
                            command=answer)
        r3.place(x=850,y=300)
        r4 = tk.Radiobutton(toplevel, textvariable=var_dic3,font=('新細明體',24),
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
    
    b = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
        bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
        font=("arial 26",32),text="㊀",pady=10,command=question)
    b.place(x=180,y=669)
    b1 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
        bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
        font=("arial 26",32),text="㊁",pady=10,command=question1)
    b1.place(x=310,y=669)
    b2 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
        bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
        font=("arial 26",32),text="㊂",pady=10,command=question2)
    b2.place(x=440,y=669)
    b3 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
        bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
        font=("arial 26",32),text="㊃",pady=10,command=question3)
    b3.place(x=570,y=669)
    b4 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
        bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
        font=("arial 26",32),text="㊄",pady=10,command=question4)
    b4.place(x=700,y=669)
    b5 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
        bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
        font=("arial 26",32),text="㊅",pady=10,command=question5)
    b5.place(x=830,y=669)
    b6 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
        bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
        font=("arial 26",32),text="㊆",pady=10,command=question6)
    b6.place(x=960,y=669)
    b7 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
        bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
        font=("arial 26",32),text="㊇",pady=10,command=question7)
    b7.place(x=1090,y=669)
    b8 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
        bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
        font=("arial 26",32),text="㊈",pady=10,command=question8)
    b8.place(x=1210,y=669)
    b9 = tk.Button(toplevel,bd=0,relief="groove",compound=tk.CENTER,
        bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
        font=("arial 26",32),text="㊉",pady=10,command=question9)
    b9.place(x=1350,y=669)

q = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font="arial 26",text="✍ 測驗 ➲",pady=10,command=evertdayfivesw_test).place(x=1200,y=410)


window.mainloop()
