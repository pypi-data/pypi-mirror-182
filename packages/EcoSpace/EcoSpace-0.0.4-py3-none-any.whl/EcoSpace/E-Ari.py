from base64 import b85encode
from hashlib import md5

class E_Ari():
    def __init__(self,text):
        self.text = text
    def Encrypt(self):
        t1 = ''
        for i in self.text:
            if ord(i) < 48 or (ord(i) < 65 and ord(i) > 57) or ord(i) > 122 or (ord(i) >= 91 and ord(i) <= 94):
                return None
            num = ord(i)+1
            if ord(i) == 122:
                num = 97
            elif ord(i) == 90:
                num = 65
            t1 += chr(num)
        t2,t3 = t1[::-1],''
        for i in self.text:
            t3 += bin(ord(i)) + '2'
        t4,t5 = md5(t3.encode('utf-8')).hexdigest().upper(),''
        for i in t2:
            if i.istitle():
                t5 += (i+'1')
            else:
                t5 += (i.upper()+'2')
        return t5+t4
    def Decryption(self):
        t1,t2,t3,t4,t5 = self.text[:-32],self.text[-32:],'','',''
        for i in range(0,len(t1)):
            if i % 2 == 1:continue
            if t1[i+1] == '2':
                t3 += (t1[i].lower())
            else:t3 += (t1[i].upper())
        for i in t3:
            if ord(i) < 48 or (ord(i) < 65 and ord(i) > 57) or ord(i) > 122 or (ord(i) >= 91 and ord(i) <= 94):
                return "Error~"
            num = ord(i)-1
            if ord(i) == 97:
                num = 122
            elif ord(i) == 65:
                num = 90
            t4 += chr(num)
        text = t4[::-1]
        for i in text:
            t5 += bin(ord(i)) + '2'
        if md5(t5.encode('utf-8')).hexdigest().upper() == t2:
            return text
        else:return "Error~"
