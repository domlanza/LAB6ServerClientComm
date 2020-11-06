#DominicLanza
import socket
import hmac
import hashlib


sock = socket.socket()
host = '192.168.1.234'
port = 54321
sock.bind(('', port))
sock.listen(5)
secretKey ='12345'
content = []
hashCode = []
code = ''
def generate_hashcode():
    message = 'abcde'
    LETTERS = 'abcdefghijklmnopqrstuvwxyz'

    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                    translated = translated + LETTERS[num]
                else:
                    translated = translated + symbol
        content.append(translated)
        code = hmac.new(secretKey, translated, hashlib.md5)
        hashCode.append(code.hexdigest())
    return hashCode


while True:
    c, addr = sock.accept()
    print 'Got connection from', addr
    print "Receiving..."
    l = c.recv(1024)
    code = str(l)
    print l
    while (l):
        print "Receiving..."
        l = c.recv(1024)
    print "Done Receiving"
    c.send('Thank you for connecting')
    c.close()                            
    break
print code
msg = generate_hashcode()
index = msg.index(code)
print "The message is ", content[index]
