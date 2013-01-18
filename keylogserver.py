import re, collections, sys
import socket

HOST = ''
PORT = 1337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()

f = open('backup.txt', 'w+')
a = open('keymap.txt', 'r+')

d = {}
for line in a.readlines():
	l = line.split()
	try:
		d[l[1]] = l[3]
	except IndexError:
		d[l[1]] = hex(int(l[1]))
		
print d['19']
	
while 1:
	data = conn.recv(1024)
	if not data: break
	f.write(data)
	try:
		q = data.split()
		for v,i in enumerate(q):
			if i in d.keys():
				try:
					if q[v-1] != 'press':
						pass
					else:
						print d[i]
				except:
					print d[i]
	except:
		pass
		
		
conn.close()