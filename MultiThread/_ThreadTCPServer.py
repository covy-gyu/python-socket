from socket import *
import _thread

r_buff = 1024
host_addr = '127.0.0.1'
port = 2500

def response(key): 
    return "서버 응답 메세지"

def handler(clientsock, addr):
    while True:
        data = clientsock.recv(r_buff)
        print("from: ", addr)
        print("data: "+ repr(data))
        if not data: break
        clientsock.send(response('').encode())
        print("sent: " + repr(response('')))

if __name__ == "__main__":
    end_point = (host_addr, port)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(end_point)
    serversock.listen(5)
    while True:
        print('waiting for connection...')
        clientsock, addr = serversock.accept()
        print("...connected from: ", addr)
        _thread.start_new_thread(handler, (clientsock, addr))