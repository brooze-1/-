a=input('请输入要查询的文件（记得添加扩展名）：')
f=open(a,'r',encoding='utf-8')
n=input('请输入要查询的姓名：')
num=0
r=f.read()
for name in r:
    if name.count(n)>0:
        num+=1
        print('{}在其中'.format(n))
print('{}:{}'.format(n,num))
f.close()
