# all imports here
from FYP import *
import numpy as np
from PIL import Image

obj = Signals()
class Images:
    
    
    def get_transpose(self, matrix):
        '''
        This function takes a matrix as a parmeter and returns 
        the transpose of the matrix.
        '''
        result = []
        print(matrix)
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(matrix[j][i])
          #  print(row)
            result.append(row)
            
        return result
                
    
    def get_max(self,matrix):
        '''
        This function takes a martix as a parameter and returns the
        maximum value in the matrix.
        '''
        maxs = 0
        for rows in matrix:
            for values in rows:
                if values > maxs:
                    maxs = values
        return maxs
    
    def get_image(self,matrix,name,n):
        '''
        This function takes a matrix as parameter, transforms and
        saves that matrix as an image.
        '''
        result = []
        first = []
        for i in range(3):
            first.append(matrix[i])
        result.append(first)
        second = []
        
        for i in range(3,6):
            second.append(matrix[i])
        result.append(second)
        
        third = []
        for i in range(6,9):
            third.append(matrix[i])
        result.append(third)
        
        print(result)
        myarr = np.asarray(result)
        #print("numpy  ",myarr)
        img = Image.fromarray(myarr, "I")
        img = img.resize((100,100))
        img.save(str(name)+".png")
        
        
        
    def normalize(self, matrix, maxs):
        '''
        This function takes a matrix as a parameter, normalizes 
        its values and the returns the matrix.
        '''
        ratio = 255 - maxs
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                
                matrix[i][j] = matrix[i][j] + ratio
                matrix[i][j] = matrix[i][j]/255
        return matrix
    
    def noiseless(self,filepath,n):
        devices = ['Device-1','Device-2','Device-3','Device-4','Device-5','Device-6','Device-7','Device-8','Device-9']
        
        
        complete = []
        for d in devices:
            filename = filepath+'/'+d+'-rtt.txt'
            rtt = obj.extractRTT(filename)
            filename = filepath+'/'+d+'-rssi.txt'
            rssi = obj.extractSignal(filename)
            
            for i in range(len(rssi)):
                rssi[i] = obj.computeSNR(rssi[i])
            
            power = []
            for i in range(len(rssi)):
                power.append(obj.power(rssi[i],rtt[i]))
            
            complete.append(power)
        print(complete)
        complete = self.get_transpose(complete)
        
        maxs = self.get_max(complete)
        complete = self.normalize(complete, maxs)
        print(complete)
        
        for i in range(len(complete)):
            self.get_image(complete[i],filepath+'/result/'+str(i),n)
        
if __name__ == "__main__":
    

    
