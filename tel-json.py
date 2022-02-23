from cmath import e
import codecs
import json
from pyexpat.errors import codes
import re 
import matplotlib.pyplot as plt

q="test"
q=input('tel me a word :) =>')






hp_dict =	{}


with open('result.json', 'r', errors='ignore') as myfile:   
    
    data=myfile.read()
    dataaa= json.load(codecs.open('result.json' , 'r' , 'utf8'))

obj = json.loads(data)


#print(obj)
#print(dataaa['messages'])
messages=dataaa['messages']

hpcount=0

print('please w8 ...')
for msg in messages:
    txt=msg["text"]
    
    #if txt=="هعپ":
    if re.search(q,str(txt) ):
        
        rawtxt =msg["date"]
        xx = re.findall("^(\d\d\d\d-\d\d-\d\d)", rawtxt)
        x=xx[0]
        if x in hp_dict:
            x_count=hp_dict.get(x)
            x_count=x_count+1
            hp_dict.update({x: x_count}) 
        else:
            hp_dict.update({x: 1}) 
        #print(txt+"=====>"+x[0])
        hpcount=1+hpcount
    else:
        
        rawtxt =msg["date"]
        xx = re.findall("^(\d\d\d\d-\d\d-\d\d)", rawtxt)
        x=xx[0]
        if x in hp_dict:
            pass
        else:
            try:
                hp_dict.update({x: 0}) 
                #print(txt+"=====>"+x[0])
            except:
                print(e)
        
        


print(hp_dict)




key_list = list(hp_dict.keys())
key_value = list(hp_dict.values())

print('days count:'+str(len(key_list)))




# x axis values
x = key_list
# corresponding y axis values
y = key_value

# plotting the points
plt.plot(x, y, color='green', linestyle='dashed', linewidth = 3,
		marker='o', markerfacecolor='blue', markersize=12)

# setting x and y axis range
y.sort()
print(y)
yy=y[-1]/10
yylim=y[-1]+yy
plt.ylim(1,)
plt.xlim(1,len(x))

# naming the x axis
plt.xlabel('x - '+str(q)+' TIME')
# naming the y axis
plt.ylabel('y - '+str(q)+' COUNT')

# giving a title to my graph
plt.title('total'+str(q)+"="+str(hpcount))

# function to show the plot
plt.show()



