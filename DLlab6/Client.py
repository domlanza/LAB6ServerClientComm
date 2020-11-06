#Dominic Lanza
import hmac
import hashlib
import socket
secretKey = '12345'

msg = 'xyzde'
digest_maker = hmac.new(secretKey, msg, hashlib.md5)
digest = digest_maker.hexdigest()

print "Hash: ", digest

sock = socket.socket()
host = '192.168.1.234'
port = 54321

sock.connect((host, port))


l = digest
print 'Sending...'
sock.send(l)



print "Done Sending"
sock.shutdown(socket.SHUT_WR)
print s.recv(1024)
sock.close()
