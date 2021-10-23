import random
import json

def binarySearch (arr, s, e, x): 
    if e >= s: 
        mid = int(s + (e - s)/2)
        if arr[mid] == x: 
            return mid 
        elif arr[mid] > x: 
            return binarySearch(arr, s, mid-1, x) 
        else: 
            return binarySearch(arr, mid+1, e, x) 
    else: 
        return None
    

with open('ます型單字(3字).json','r') as fp:
    a = json.load(fp)
print(a)
li = ['くれます', 'ずれます', 'なります', 'はめます', 'ばてます', 'もてます', 'やります', '上げます', '上ります', '下げます', '下します', '下ります']

question = [['エスクロー業務を提供する会社が、家に関する税や保険料が全て支払済みであること確認してくれます。', '日本ではレストランに入るといつも、注文する前に水とおしぼりを出してくれます。', '中のヒーターと布団が温めてくれます。', '作業効率と商品販促活動の改善のための、デジタルメディアの使い方を教えてくれます。'], [], [], [], [], ['あなたが再びライブに行ける機会がもてますように。'], ['自分でやります。', '私がやります。', 'もちろんやります！', 'そろそろやります。', '今すぐやります。', 'またゲームをやりますか', '誰がそれをやりますか？', 'それは私がやります。', '私ならやりますよ。', '花に水をやります。'], ['一年間の練習の成果を是非ともご鑑賞いただきたく、お招き申し上げます。', '間違いなくセンサデバイスを受け取ったら、すぐに私があなたに連絡を差し上げます。', 'あなたの偉業が日本の未来を切り拓いたことに、お祝い申し上げます。', '以下で言及されている会社は、子会社であることをご報告申し上げます。', '副市長の私、山田が市長の鈴木に代わりまして歓迎のご挨拶を申し上げます。', 'ご連泊のお客様は、お手数ですが敷地内駐車場にご移動をお願い申し上げます。', '多大なご迷惑とご心配をおかけ致しましたことをお詫び申し上げます。', 'この度の発送の遅れによって、ご迷惑をお掛けいたしましたことをお詫び申し上げます。', '今後とも変わらぬご厚誼とご指導のほど、よろしくお願い申し上げます。', '今回の地震によって被災された皆様方に、心からお見舞い申し上げます'], [], ['減力液はネガの濃度を下げます。', 'その仕事の優先度を下げます。'], ['本当にこの要請内容を却下しますか？'], ['坂を下ります。']]
# print(q[3])

arr = li
li_num_single = random.randint(0,len(li))
x = li[li_num_single]
result = binarySearch(arr, 0, len(arr)-1, x) 
# print(result)
# print(q[result])

try:
    question_num = random.randint(0, len(question[result])-1)
    q = question[result][question_num]
    L = random.sample(range(0, 4), 4)
    
    li_num = random.sample(range(0, len(li)), 3)
    while li_num_single in li_num:
        li_num = random.sample(range(0, len(li)), 3)
    
    list =[x,li[li_num[0]],li[li_num[1]],li[li_num[2]]]
    dic = {'A':list[L[0]],'B':list[L[1]],'C':list[L[2]],'D':list[L[3]]}
    # print(dic['A'])
    Q = q.replace(x,'_'*len(x))
    print(Q)
    print('A.{}  B.{}  C.{}  D.{}'.format(dic['A'],dic['B'],dic['C'],dic['D']))
    if x == dic[input('答案：').upper()]:
        print('正確 O')
    else:
        print('錯誤 X')
        print("正確答案:",x)
except:
    print("暫無題目")
