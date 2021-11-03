#all imports 
import os
from FYP import *
from localisation import *

obj = Signals()
obj2 = Localisation()
class Detection:
    
    def get_RSSI_input(self,values):
        '''
        This function takes raw RSSI values as input,
        applies weigthed filter to reduce noise and returns
        the new filtered value.
        '''
        
        weight,RSSI_input = 0,0
        w = 1
        for val in values:
            RSSI_input += val * w
            w += 1
            weight += w
        RSSI_input = RSSI_input/weight
        return RSSI_input
    
    def get_RSSI_mean(self,values):
        '''
        This function takes a list of RSSI_input values and then
        calculates and returns the mean of these values.
        '''
        
        samples = len(values)
        total = 0
        for val in values:
            total += val
        
        return(total/samples)
    
    def get_delta_RSSI(self,mean, inp):
        '''
        This function takes mean and RSSI_input values as input and
        then calculates and returns delta_RSSI value.
        '''
        
        return(mean-inp)
    
    def get_min_RSSI(self,values):
        '''
        This function takes a list of RSSI values as input and returns
        the minimum value.
        '''
        
        return(min(values))
    
    def get_threshold(self, mean, minimum, constant):
        '''
        This fucntion takes mean of RSSI_INPUT, minimum of RSSI_Input and some 
        constant value and then calculates and returns the threshold.
        '''
        
        return((mean-minimum)*(constant/100))
    
    def get_decision(self, threshold, delta_RSSI):
        '''
        This function takes threshold and delta_RSSI as input and then 
        returns the decision bases on the input values.
        '''
        
        if delta_RSSI < threshold:
            return 0
        else:
            return 1
    
    def main(self,base_path):
        #inside no-humans
        dir_list = os.listdir(base_path)
        final = []
        
        
        #filex = open("device-1-1.txt", 'w')
        #filex.write("RSSI_MAX" +'\t'+"RSSI_Mean" + '\t' + "RSSI_MIN" +'\n')
        
        
        for experiment in dir_list:
            decision = []
            variance = []
            path = base_path + '/' + experiment
            file_list = os.listdir(path)
            #print(file_list)
        
       
            
            for device in file_list:
                path = base_path + '/' + experiment + '/' + device
                devices = os.listdir(path)
                rssi_input = []
                for files in devices:
                    minimum = 0
                    file = path + '/' + files
                    rssi_data = obj.extractSignal(file)
                    print(rssi_data)
            
          
            
                    if minimum > min(rssi_data):
                        minimum = min(rssi_data)

                    rssi_input.append(self.get_RSSI_input(rssi_data))
                print(rssi_input)
                mean = self.get_RSSI_mean(rssi_input)
                print("mean ==>", mean)

                print("minimum ==>", minimum)
                delta = self.get_delta_RSSI(mean ,rssi_input[1])
                print("delta==>",delta)

                threshold = self.get_threshold(mean,minimum,30)
                print("threshold ==>",threshold)

                decision.append(self.get_decision(threshold, delta))

                variance.append(obj2.variance(obj2.RSSI_threshold(mean, threshold),rssi_input[1]))
                #filex.write(str(max(rssi_input)) +'\t'+ str(mean) + '\t' + str(min(rssi_input))+'\n')
            break
           # filex.close()
            count1 = 0
            count0 = 0
            for i in decision:
                if i == 1:
                    count1 += 1
                else:
                    count0 += 1
            print(decision)
            if count1 > 0:
                final.append(1)
                
            else:
                final.append(0)
                #print("Human has been detected")
                
                
        count =0
        var = None
        for i in final:
            if i == 1:
                count +=1
        if count > len(final) - count:
            print("Human has been detected")
            variance.append(variance[5])
            var = obj2.get_zone(variance)
        else:
            print("Human has not been detected")
        #print("accuracy ==>  ",(count/100)*100)
        #print(final)
        
        
        return var


if __name__ == "__main__":
    plot_rssi=[]
    # creating object of class Detection
    obj1 = Detection()
    # Base path where all data is saved
    base_path = 'C:/Users/abdul/OneDrive/Desktop/New folder/FYP/final/data/no-human'
    # Extracing and then further processing the data to get results
    obj1.main(base_path)
    
    
    
        
            
            
    
    