from socket import *
from threading import *
from requests import *



def connect_to_host(host, port):

    lock_object = Semaphore(value=1)
    try:
        sckt = socket(AF_INET, SOCK_STREAM)
        sckt.connect((host, port))
        sckt.send('Hello\r\n')
        results = sckt.recv(100)
        lock_object.acquire()
        print 'Port %d open'% port
        print str(results)
    except:
        lock_object.acquire()
        print 'Port %d closed'% port
    finally:
        lock_object.release()
        sckt.close()

   # with open('received_file', 'wb') as f:
    #    print 'file opened'
     #   while True:
      #      print('receiving data...')
            #print('data=%s', results)
           # if not results:
           #     break
        # write data to a file
          #  f.write(results)


def scan_ports(host, ports):
    try:
        tgtIP = gethostbyname(host)

    except:
        print "Could not resolve host:'%s'"%host
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\nScanning: ' + tgtName[0]
    except:
        print '\n Scanning: ' + tgtIP
    setdefaulttimeout(1)
    for port in ports:
        t = Thread(target=connect_to_host, args=(host, int(port)))
        t.start()



def main():
    ports = range(9089, 9091)
    ports= map(str, ports)
    scan_ports('localhost', ports)

if __name__ == '__main__':
    main()


