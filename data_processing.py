from FYP import *
from FYP3 import *
import os
obj = Signals()
obj2 = Images()

'''
This class is used for analysis and creation of dataset.
'''
class DataProcessing:
    
    
    def extract(self,path):
        '''
        This function takes path of the dataset as parameter, using this
        dataset it ganerates and saves the image dataset. 
        '''
        devs = ['Device-1','Device-2','Device-3','Device-4','Device-5','Device-6','Device-7','Device-8','Device-9']
        count = 0
        for experiment in range(1,176):
            power = []
            for devices in devs:
                result=[]
                rssi = obj.extractSignal(path+'/'+devices+'-experiment-'+str(experiment)+'-rssi.txt')
                rtt = obj.extractRTT(path+'/'+devices+'-experiment-'+str(experiment)+'-rtt.txt')
                for i in range(len(rssi)):
                    
                    result.append(obj.power(obj.computeSNR(rssi[i]),rtt[i]))
               
                power.append(result)
            power.append(power[5])
            print('\n\n')
            print(power)
            
           
            power = obj2.get_transpose(power)
           # maxs = obj2.get_max(power)
            power = obj2.normalize(power,59)
            print(power ,"k")
            for i in range(len(power)):
                obj2.get_image(power[i],'C:/Users/abdul/OneDrive/Desktop/New folder/FYP/final/data/images/train/no-humans/no-humans-'+str(count),0)
                count+=1

            
    def max_power(self,path):
        '''
        This function takes the dataset as parameter. Computes the value
        of power and displays the maximum, minimum and average value of 
        power.
        '''
        devs = ['Device-1','Device-2','Device-3','Device-4','Device-5','Device-6','Device-7','Device-8','Device-9']
        directories = os.listdir(path)
        power = []
        for dirs in directories:
            print(dirs)
            for experiment in range(1,201):
                for devices in devs:
                    rssi = obj.extractSignal(path+'/'+dirs+'/'+devices+'-experiment-'+str(experiment)+'-rssi.txt')
                    print("device ==> ",devices, "  experiment ==> ",experiment)
                    rtt = obj.extractRTT(path+'/'+dirs+'/'+devices+'-experiment-'+str(experiment)+'-rtt.txt')
                    if '' in rtt:
                        rtt.remove('')
                    
                    if '' in rssi:
                        rssi.remove('')
                    print(rtt)
                    print(rssi)
                    for i in range(len(rssi)):
                        power.append(obj.power(obj.computeSNR(float(rssi[i])),rtt[i]))
        print("total data ==> ",len(power))
        print("max power ==> ",max(power))
        print("min power ==> ", min(power))
            
            
if __name__=="__main__":
    obj1 = DataProcessing()
    obj1.extract('C:/Users/abdul/OneDrive/Desktop/New folder/FYP/final/data/second/no-humans')
    #obj1.max_power('C:/Users/abdul/OneDrive/Desktop/New folder/FYP/final/data/second')
                