import pingparsing   #used for executing the shell command 'ping' and helps parse it for further use
import time
import subprocess
import argparse
from threading import Thread


class Raspberrypi:
    
   
    def ping(self, dest_ip):
        '''
        This function takes a destination ip, pings
        to that ip and returns a list containing minimum, average and maximum round
        trip time.
        '''

        ping_parser = pingparsing.PingParsing() # creating an object
        transmitter = pingparsing.PingTransmitter() # create transmitter
        transmitter.destination = dest_ip # set ip for the destination
        transmitter.count = 2 # set number of packets to send
        result = transmitter.ping() # get result and saving it in a variable
        x = ping_parser.parse(result).as_dict() # converting the result into a dictionary format
        return [x['rtt_min'],x['rtt_avg'],x['rtt_max']]

    def main(self, ip, iterations, filename):
        '''
        This function takes ip , no of data points of rtt and filename/path(to save the data) as
        parameter. It calls the ping function with the given ip and then saves the data in the file
        of the given filename.
        '''

        file = open(filename, 'w') # opening file to save the collected data
        file.write("No." + "\t"+"MIN-RTT/ms" + "\t"+"AVG-RTT/ms" + "\t"+"MAX-RTT/ms" +"\n")
        for i in range(iterations):
            time = self.ping(ip)
            file.write(str(i+1) + "\t" + "\t" +str(time[0])+ "\t"+ "\t"  +str(time[1])+ "\t"+ "\t"  +str(time[2])+"\n")
            print(time , "milli-seconds")
        file.close()
    
    def signalStrength(self,filename, iterations):
       
        '''
        This function takes filename (to save the collected data), iterations(no. of data points to collect)
        as parameter. Then it saves the collected signal level and link quality of the connected network in the file
        with the given filename.
        '''

        parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
        parser.add_argument(dest='interface', nargs='?', default='wlan0',
        help='wlan interface (default: wlan0)')
        args = parser.parse_args()

        file = open(filename,'w')
        i =0
        while i<iterations:
            cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True,
                                stdout=subprocess.PIPE)
            for line in cmd.stdout:
                if 'Link Quality' in line:
                    file.write(line.lstrip(' '),)
                    print (line.lstrip(' ')),
                elif 'Not-Associated' in line:
                    print ('No signal')
            time.sleep(1)
            i+= 1

if __name__ == "__main__":
    obj = Raspberrypi()
