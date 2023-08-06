import subprocess

def help():
    print("json data of 100 students - google_search_img.json100students")
    print("Faker Hindi names and countries - google_search_img.fakecountries()")
    print("Create fake profile - google_search_img.fakeprofile()")
    print("Get n largest values of an array - google_search_img.nlargest()")
    print("Text label above each bar - google_search_img.bartextlabel()")
    print("Ex2(Create csv, Read csv, make plot) - google_search_img.e2allinone()")
    print("Draw the line graph of temp values - google_search_img.airqlinegraph()")
    print("Draw a box plot for temp values - google_search_img.airqualityboxplot()")
    print("Read air quality, find mean mm - google_search_img.airqmeanmaxetc()")
    print("Ceaser Cipher - google_search_img.ceasercipher()")
    print("Affine cipher - google_search_img.affinecipher()")
    print("Mono cipher - google_search_img.monocipher()")
    print("Vigner cipher - google_search_img.vignercipher()")
    subprocess.call(["rm", "prog1.py"])

def vignercipher():
    code = """def generateKey(string,key):
    key=list(key)
    if len(string)==len(key):
        return(key)
    else:
        for i in range(len(string)-len(key)):
            key.append(key[i%len(key)])
        return ("".join(key))

def cipherText(string,key):
    cipher_text=[]
    for i in range(len(string)):
        x=(ord(string[i])+
                ord(key[i]))%26
        x +=ord('A')
        cipher_text.append(chr(x))
    return ("".join(cipher_text))
def cipherText(string,key):
    cipher_text=[]
    for i in range(len(string)):
        x=(ord(string[i])+
                ord(key[i]))%26
        x +=ord('A')
        cipher_text.append(chr(x))
    return("".join(cipher_text))
def originalText(cipher_text,key):
    orig_text=[]
    for i in range(len(cipher_text)):
        x=(ord(cipher_text[i])-
                ord(key[i])+26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return ("".join(orig_text))

string="INDIRACOLLEGE"
keyword="TYCYBER"
key=generateKey(string,keyword)
cipher_text=cipherText(string,key)
print("original Text:",string)
print("Cipher Text:",cipher_text)
print("original/decrypted text:",originalText(cipher_text,key))"""
    file = open("vigner.py", 'w')
    file.write(code)
    file.close()
    subprocess.call(["rm", "prog1.py"])

def monocipher():
    code = """keys={'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n'}
reverse_keys={}
for key,value in keys.items():
    reverse_keys[value]=key
def encrypt(text):
    text=str(text)
    encrypting=[]
    for l in text:
        encrypting.append(keys.get(l,l))
    print(''.join(encrypting))
def decipher(text):
    text=str(text)
    decrypted=[]
    for l in text:
        decrypted.append(reverse_keys.get(l,l))
    print(''.join(decrypted))

print("encrypted string ")
encrypt("indiracollege")
print("decrypted string ")
decipher("sun")"""
    file = open("mono.py", 'w')
    file.write(code)
    file.close()
    subprocess.call(["rm", "prog1.py"])

def affinecipher():
    code = """def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y
 
def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m
 
 
# affine cipher encryption function
# returns the cipher text
def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                  + ord('A')) for t in text.upper().replace(' ', '') ])
 
 
# affine cipher decryption function
# returns original text
def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                    % 26) + ord('A')) for c in cipher ])
 
 
# Driver Code to test the above functions
def main():
    # declaring text and key
    text = 'AFFINE CIPHER'
    key = [17, 20]
 
    # calling encryption function
    affine_encrypted_text = affine_encrypt(text, key)
 
    print('Encrypted Text: {}'.format( affine_encrypted_text ))
 
    # calling decryption function
    print('Decrypted Text: {}'.format
    ( affine_decrypt(affine_encrypted_text, key) ))
 
 
if __name__ == '__main__':
    main()"""

    file = open("affine.py", 'w')
    file.write(code)
    file.close()
    subprocess.call(["rm", "prog1.py"])


def ceasercipher():
    code = """def encypt_func(txt, s):  
    result = ""  
  
  
# transverse the plain txt  
    for i in range(len(txt)):  
        char = txt[i]  
        # encypt_func uppercase characters in plain txt  
  
        if (char.isupper()):  
            result += chr((ord(char) + s - 64) % 26 + 65)  
        # encypt_func lowercase characters in plain txt  
        else:  
            result += chr((ord(char) + s - 96) % 26 + 97)  
    return result  
# check the above function  
txt = "CEASER CIPHER EXAMPLE"  
s = 4  
  
print("Plain txt : " + txt)  
print("Shift pattern : " + str(s))  
print("Cipher: " + encypt_func(txt, s))  """
    file =  open("ceasercipher.py", 'w')
    file.write(code)
    file.close()
    subprocess.call(["rm", "prog1.py"])

def json100students():
    code = """from faker import Faker
import json
from random import randint
fake = Faker()

def input_data(x):
    student_data = {}
    for i in range(0,x):
        student_data[i] = {}
        student_data[i]['id'] = randint(1,100)
        student_data[i]['name'] = fake.name()
        student_data[i]['address'] = fake.address()
        student_data[i]['latitude'] = str(fake.latitude())
        student_data[i]['longitude'] = str(fake.longitude())
    print(student_data)

    with open('students.json','w') as fp:
        json.dump(student_data,fp)

def main():
    input_data(10)
main()"""
    file =  open("100students.py", 'w')
    file.write(code)
    file.close()
    subprocess.call(["rm", "prog1.py"])

def fakecountries():
    code = """from faker import Faker 
  
#'hi_IN' changed the language
fake = Faker('hi_IN')      
  
for i in range(0, 10): 
    print('Name=', fake.name(),'Country=', fake.country())
         """

    file = open("fakecountries.py", 'w')
    file.write(code)
    file.close()
    subprocess.call(["rm", "prog1.py"])

def fakeprofile():
    code = """from faker import Faker 
fake = Faker()
print(fake.profile())"""

    file = open("fakeprofile.py", 'w')
    file.write(code)
    file.close()
    subprocess.call(["rm", "prog1.py"])

def nlargest():
    code = """import numpy as np
x=np.arange(10)
print("original array:",x)
np.random.shuffle(x)
print("shuffled array:",x)
n=1
print("largest element in array",x[np.argsort(x)[-n:]])"""
    file = open("nlargest.py", 'w')
    file.write(code)
    file.close()
    subprocess.call(["rm", "prog1.py"])

def bartextlabel():
    code = """import matplotlib.pyplot as plt
x=['java', 'python', 'javascripy' , 'c' ,'c++']
y=[2.0,3,4.1,5,2.8]
plt.bar(x, y, color=('purple') , edgecolor='red')
plt.xlabel("languages")
plt.ylabel("popularity")
plt.title("population of programming language ")
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth=0.5, color='red')
plt.grid(which='minor', linestyle=':', linewidth=0.5, color='black')
for i in range(len(x)):
    plt.text(i,y[i], y[i] ,ha="center",va="bottom")
plt.show()"""
    file = open("bartextlabel.py", 'w')
    file.write(code)
    file.close()
    subprocess.call(["rm", "prog1.py"])

def e2allinone():
    code = """import csv
import pandas
import matplotlib.pyplot as plt

fields = ["Name", "Courses"]
rows = [
    ["Kiran", "CS"],
    ["Abhishek", "CS"],
    ["Govind", "Philosophy"]
]

with open("csvfile.csv", 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fields)
    writer.writerows(rows)

df = pandas.read_csv("csvfile.csv")
print(df)

fig, ax = plt.subplots(figsize=(10, 6))
bar = ax.plot(df["Name"], df["Courses"])
ax.set(title="graph", xlabel="x", ylabel="y")

fig.show()"""
    file = open("e2allinone.py", 'w')
    file.write(code)
    file.close()
    subprocess.call(["rm", "prog1.py"])

def airqlinegraph():
    code = """import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt

#Reading the file
df = pd.read_csv('AirQualityUCI.csv', sep=';', decimal=',')

#Calculating length total
len(df)

#Calculating null values
df.isna().sum()

#Removing null values
df = df[df['T'].notnull()]
df.isna().sum()

#Plotting the graph
fig, ax = plt.subplots(figsize=(5, 5))
pl = ax.plot(df['T'])
#ax.set(title="Boxplot", xlabel="x-axis", ylabel="y-axis")
fig.show()"""
    file = open("airlinegraph.py", 'w')
    file.write(code)
    file.close()
    subprocess.call(["rm", "prog1.py"])

def airqualityboxplot():
    code = """import pandas as  pd
import numpy as np
import matplotlib.pyplot as plt

#Reading the file
df = pd.read_csv('AirQualityUCI.csv', sep=';', decimal=',')

#Calculating length total
len(df)

#Calculating null values
df.isna().sum()

#Removing null values
df = df[df['T'].notnull()]
df.isna().sum()

#Plotting the graph
fig, ax = plt.subplots(figsize=(5, 5))
box_plot_data = [df['C6H6(GT)'],df['T']]
pl = ax.boxplot(box_plot_data)
ax.set(title="Boxplot", xlabel="x-axis", ylabel="y-axis")
fig.show()"""
    file = open("airqboxplot.py", 'w')
    file.write(code)
    file.close()
    subprocess.call(["rm", "prog1.py"])

def airqmeanmaxetc():
    code = """import numpy as np
import pandas as pd

#reading data
df = pd.read_csv('AirQualityUCI.csv', sep=';', decimal=",")

#Calculating null values
df.isna().sum()

#Removing null values
df = df[df['T'].notnull()]

#Calculating the mean, max, min
df['T'].mean()
df['T'].max()
df['T'].min()
df['T'].std()"""
    file = open("airqmeanmax.py", 'w')
    file.write(code)
    file.close()
    subprocess.call(["rm", "prog1.py"])


if __name__=="__main__":
    json100students()