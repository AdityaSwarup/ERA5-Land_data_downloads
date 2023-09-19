#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:48:54 2023

@author: adityaswarup
"""

import netCDF4
import numpy as np
import os
import shutil

list_of_u10_files = []
list_of_v10_files = []

for file in os.listdir("/Users/adityaswarup/.spyder-py3/ERA5 test"):
    if file.startswith("10m_u") and file.endswith('.nc'):
        list_of_u10_files.append(os.path.join("/Users/adityaswarup/.spyder-py3/ERA5 test", file))
    
    if file.startswith("10m_v") and file.endswith('.nc'):
        list_of_v10_files.append(os.path.join("/Users/adityaswarup/.spyder-py3/ERA5 test", file))

def wind_modulus(start_year, end_year):
    '''
    Code is slightly broken. The files are being created which is a good sign.
    They're just not updating properly. Can't seem to put netcdf files into
    write mode. 
    '''
    i = start_year

    years = [] #Creates a list of years.
    
    while i <= end_year:
        years.append(str(i))
        i += 1
    
    for year in years:
        
        
        for file in list_of_u10_files:
            
            if year in file:
                
                wind_u10 = netCDF4.Dataset(file).variables['u10'][:]
                
                wind_modulus_file_name = str.replace(file, "10m_u_component_of_wind", 
                                                "10m_wind_modulus")
                
                shutil.copy2(os.path.join("/Users/adityaswarup/.spyder-py3/ERA5 test", 
                                          file), 
                             os.path.join("/Users/adityaswarup/.spyder-py3/ERA5 test", 
                                                       wind_modulus_file_name))
                
        
        for file in list_of_v10_files:
            
            if year in file:
                
                wind_v10 = netCDF4.Dataset(file).variables['v10'][:]
        
        wind_modulus_file = netCDF4.Dataset(
            os.path.join("/Users/adityaswarup/.spyder-py3/ERA5 test", 
                         wind_modulus_file_name), 'a')
        
        wind_modulus_file.renameVariable('u10', 'wind_modulus10')
        
        if wind_u10.shape != wind_v10.shape:
            '''
            The only thing here that won't match up, if at all, is time
            which is the first component of the shape of these datasets.
            This if-else statement is just a quick fix for this. The whole
            issue is avoidable if for the current year, you specify a cutoff
            time. The difference in time occurs mainly because of request 
            timing.
            
            '''
            
            if wind_u10.shape[0] < wind_v10.shape[0]:
                wind_v10[:wind_u10.shape[0]]
            
            else:
                wind_u10[:wind_v10.shape[0]]
            
        else:        
            wind_modulus_calc = lambda u, v: np.sqrt(u**2 + v**2)
            vfunc = np.vectorize(wind_modulus_calc)
            wind_modulus = vfunc(wind_u10, wind_v10)
            
            wind_modulus_file.variables['wind_modulus10'][:] = wind_modulus
        
        
# wind_modulus(2020,2023)







