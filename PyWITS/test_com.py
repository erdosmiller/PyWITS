from wits0 import *
import socket,time


comm = WITS0Communicator('192.168.15.85', 4000)
try:
    while True:
        data = comm.read_pason_data()
        if not data == []:
            print data
        time.sleep(1)
finally:
    comm.close()

