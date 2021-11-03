import socket
from times import *
from FYP2 import *
from FYP import *
from classification import *
import time

def server_socket(message,port):
    # create the socket
    # AF_INET == ipv4
    # SOCK_STREAM == TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', port))
    s.listen(10)
    clientsocket, address = s.accept()
    clientsocket.send(bytes(message,"utf-8"))
    clientsocket.close()   

if __name__ == "__main__":
    timex = current_time()
    new_time = inc_time(timex)
    
    ips = ['192.168.137.22','192.168.137.195','192.168.137.142','192.168.137.240','192.168.137.129','192.168.137.108','192.168.137.26',
               '192.168.137.123','192.168.137.162']
    port = 1234
    
    print("Establishing Communication .....")
    for ip in ips:
        print("pinging with ", ip)
        server_socket(new_time,port)
        port+=1
        time.sleep(0.4)
    
    print("collecting RSSI .....")
    print("collecting RTT......")
    time.sleep(12)

    print("\n\n")
    #server_socket(new_time)
    obj = Detection()
    obj1 = Signals()

    zone = obj.main('C:/Users/abdul/OneDrive/Desktop/New folder/FYP/final/final/data/result')


    print("zone ==> ",zone) 
    print("\n\n")
    print("forming images")

    
    print("predicting from model")
    objc = classification()
   
    val = objc.predict('C:/Users/abdul/OneDrive/Desktop/New folder/FYP/final/final/data/images')
    if val == 0:
        print("Human present")
    else:
        print("Human not present")