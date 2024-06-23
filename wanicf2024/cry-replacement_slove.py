import replacement_diary
import hashlib

target_diary=replacement_diary.diary
decode=[]
for sentence in target_diary:
    decode.append(hex(sentence))
word_list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9","!","@","#","$","%","^","&","*","(",")","_","-","=","+","[","]","{","}",";",":","'","\"",",","<",".",">","/","?","\\","|","`","~"]
ans=""
decode_dict={}
for word in word_list:
    x = ord(word) #アスキーコードを取得
    x = hashlib.md5(str(x).encode()).hexdigest() #md5でハッシュ化
    decode_dict[word]=x
for data in decode:
    for word in word_list:
        if decode_dict[word]==data[2:]:
            ans+=word
print(ans)