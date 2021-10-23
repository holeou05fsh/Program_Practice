import tkinter as tk
import json
import random
from gtts import gTTS
from pygame import mixer
import tempfile

with open('ます型二題以上(總和)(含翻譯).json', 'r',encoding='utf-8') as fp:
    c = json.load(fp)

window = tk.Tk()
# window2 = tk.Toplevel()
window.title('JapaneseLesson')
window.geometry('600x400+500+200')
window.minsize(width=300, height=200)
window.config(background='skyblue')

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
q = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font="arial 26",text="✍ 測驗 ➲",pady=10).place(x=1200,y=410)
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

but = tk.Button(window,bd=0,relief="groove",compound=tk.CENTER,
    bg="skyblue",fg="blue",activeforeground="pink",activebackground="skyblue",
    font="arial 26",text="隨機十題",pady=10)
img = image(2) # 1=normal, 2=small, 3=smallest
but.config(image=img)
but.place(x=30,y=30)


window.mainloop()
