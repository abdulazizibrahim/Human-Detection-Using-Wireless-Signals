class Localisation:
    
    def RSSI_threshold(self, mean, threshold):
        '''
        This function computes and returns RSSI Threshold by
        subtracting RSSI mean with the threshold value.
        '''
    
        return (mean - threshold)


    def variance(self, RSSI_threshold, RSSI_input):
        '''
        This function computes and returns variance by
        subtracting RSSI Threshold with the RSSI Input.
        '''
        return(RSSI_threshold - RSSI_input)
    
    def get_zone(self,variances):
        '''
        This function takes a list of variances as parameter.
        Computes the maximum variance from the zones and returns that
        zone.
        '''
        zones = []
        
        zone_A = variances[0] + variances[1] + variances[3] + variances[4]
        
        zones.append(zone_A)
        
        zone_B = variances[1] + variances[2] + variances[4] + variances[5]
        
        zones.append(zone_B)
        
        zone_C = variances[3] + variances[4] + variances[6] + variances[7]
        
        zones.append(zone_C)
        
        zone_D = variances[4] + variances[5] + variances[7] + variances[8]
        
        zones.append(zone_D)
        
        maxs = max(zones)
        
        result = []
        if zone_A == maxs:
            result.append('A')
        if zone_B == maxs:
            result.append('B')
        if zone_C == maxs:
            result.append('C')
        if zone_D == maxs:
            result.append('D')

        return result
