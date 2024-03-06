s="a python script"
print(s[0])
print(s[2])
print(s[2:7])
print(s[:8])
print(s[8:])
print(s[2:999])

message = 'document "cv.doc" was printed on printer: XEROX'
print(message.find(':'))
print(message[message.find(':')+2:])

print(message[message.find('"')+1:])
tmp=message[message.find('"')+1:]
print(tmp[:tmp.find('"')])

q = "THE EYES"
print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])

g="a gentleman"
print(g[3],g[6],g[7],g[2],g[0],g[4],g[5],g[1],g[8:99])

line='Program "Kropka nad i" nadamy o: 22:00'

time = line[line.find(':')+2:]
tmp = line[line.find('"')+1:]
title=tmp[:tmp.find('"'):]

print(title+' ' + time)

print((45*5+50)*20+1023-2002)