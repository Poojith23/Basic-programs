#!/usr/bin/env python
# coding: utf-8

# In[1]:


b={1,2,3,4,5,6,"python",4.5}
print(b)
print(type(b))


# In[2]:


del b


# In[4]:


b={1,2,3,4,5,6,"python",4.5}


# In[5]:


l={23,22,2,4,5,23,22,6,25}


# In[6]:


print(b-l)


# In[7]:


print(l-b)


# In[11]:


print(l.intersection)


# In[12]:


print(l|b)


# In[17]:


d=dict()
d[1]="orange"
d[2]="apple"
print(d)


# In[25]:


e={"vishal" :50,"karthi" :48}
print(e["vishal"])
e["karthi"]


# In[31]:


d=dict(list((("karthi",20),("poojith",20),("venky",20))))


# In[32]:


print(d)


# In[33]:


print(d.pop("venky"))


# In[34]:


print(d)


# In[ ]:


a=10
b=20
if a>b:
    print(a)
elif a<b:
    print(b)


# In[1]:


m=int(input("Enter the number:"))
if m%2==0:
    print("Even Number")
else:
    print("Odd Number")


# In[3]:


i=1
while i<=10:
    print(i,end=" ")
    i+=1
    if i==4:
        continue
    elif i==6:
        pass
    elif i==9:
        break


# In[6]:


i=1
while True:
    i+=1
    if i==4:
        continue
        print(i,end=" ")
    elif i==6:
        pass
        print(i,end=" ")
    elif i==9:
        break
        print(i,end=" ")


# In[11]:


s="python"
for r in s:
    print(r,end=" ")


# In[18]:


s=[23,"hash",27,"english",35.5,(2,3,4),[12,"xerox"]]
for r in s:
    print(r,end=" ")


# In[17]:


s=["hash","english",(2,3,4),[12,"xerox"]]
for i in s:
    print(s)


# In[2]:


for i in range(7):
    for j in range(5):
        print("i=",i,"j=",j)


# In[3]:


l=["purple",[2,3,4,5],"Black",(35,35,67,89),{0,"turtle",1,2,"parrot"},{1:"king",2:"queen"}]
a=len(l)
for i in range(a):
    print(l[i] , "=" , len(l[i]))
   


# In[4]:


n=int(input("Enter the number:"))
for i in range(n):
    print("* "*(i+1))


# In[2]:


class student_details:
    '''This class tells about the details of student'''
print(student_details)


# In[3]:


class teacher:
    def __init__(self):
        self.a=10
        self.b=20
    def hello(self):
        self.c-30
obj.teacher()
#obj.hello()
print(obj.__dict__)


# In[6]:


class test:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a,self.b)

t=test(2,3)
t.display()


# In[8]:


class test:
    def __init__(self,a,b):
        self.a=20
        self.b=40
        self.c=10
    def do(self):
        del self.a
        
t=test()
print(t.__dict__)
t.do()


# In[12]:


class test:
    x=20
    y=10
    def __init__(self):
        self.c=80
t1=test()
print(t1.__dict__)
print(test.x,test.y)
test.x=999
print(test.__dict__)


# In[ ]:




