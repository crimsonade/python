username= dict(firstname='isaac', last= 'mensah')
username['age']= 23
username['location']= 'Ofankor Barrier'
print(username)
print(username['age'])

firstnames=['john','jerry','jack']
lastnames=['stones','smith','kane']

userinfo= {k:v for (k,v) in zip(firstnames,lastnames)}
print(userinfo)


us_name= dict.fromkeys(('john','jerry','jack'),23)
print(us_name)

username.update(userinfo)
print(username)

username.pop('age'and 'location')
print(username)

k= username.keys()

for ky in username:
    print(ky,'\t\t\t',username[ky])
print('\n')
for vl in username.values():
    print(vl)

li= list(userinfo)
print(li)