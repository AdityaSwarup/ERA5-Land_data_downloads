#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:38:02 2023

@author: adityaswarup
"""

import cdsapi
import os

path = 'ENTER YOUR WORKING DIRECTORY HERE' # Please verify where your files are being downloaded.


def data_download(variables, start_year, end_year, path):
    
    '''
    Please refer to the following documentation for ERA5-Land
    https://confluence.ecmwf.int/display/CKB/ERA5-Land%3A+data+documentation#ERA5Land:datadocumentation-Dataformat
    
    To get the api request, enter the relevant details in the following CDS
    webpage:
    https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-land?tab=form
    
    Please ensure that you have a valid login.
    
    Definition
    ----------
    data_download(variables, start_year, end_year)

    Input           Format          Description
    -----           -----           -----------
    variables       List of Str     A list of variables as outlined by ECMWF 
                                    ERA5Land documentation.
    
    start_year      Int             The year from which you want to start
                                    data downloads.
                                    
    end_year        Int             The year from which you want to end 
                                    data downloads.
                                    
    path            Str             The folder in which your data will be 
                                    downloaded.
    
    
    Output          Format          Description
    -----           -----           -----------
    netcdf.zip      file            Multiple files are outputted. The number 
                                    of files outputted is related to your 
                                    variables, start_year, and end_year. The 
                                    files will be named by variable and year.
                                    
    Message         Str             Checks in your specified directory whether 
                                    or not your file has been downloaded.           
                                    
    Example
    --------
    >>> variables = ["total_precipitation", "2m_temperature"]
    
    >>> data_download(variables, 2015, 2023)
    
    total_precipitation_2015.netcdf.zip has been downloaded!
    total_precipitation_2016.netcdf.zip has been downloaded!
    total_precipitation_2017.netcdf.zip has been downloaded!
    total_precipitation_2018.netcdf.zip has been downloaded!
    total_precipitation_2019.netcdf.zip has been downloaded!
    total_precipitation_2020.netcdf.zip has been downloaded!
    total_precipitation_2021.netcdf.zip has been downloaded!
    total_precipitation_2022.netcdf.zip has been downloaded!
    total_precipitation_2023.netcdf.zip has been downloaded!
    2m_temperature_2015.netcdf.zip has been downloaded!
    2m_temperature_2016.netcdf.zip has been downloaded!
    2m_temperature_2017.netcdf.zip has been downloaded!
    2m_temperature_2018.netcdf.zip has been downloaded!
    2m_temperature_2019.netcdf.zip has been downloaded!
    2m_temperature_2020.netcdf.zip has been downloaded!
    2m_temperature_2021.netcdf.zip has been downloaded!
    2m_temperature_2022.netcdf.zip has been downloaded!
    2m_temperature_2023.netcdf.zip has been downloaded!
    
    You will notice the following files downloaded in your specified location:
    total_precipitation_2015.netcdf.zip
    total_precipitation_2016.netcdf.zip
    total_precipitation_2017.netcdf.zip
    total_precipitation_2018.netcdf.zip
    total_precipitation_2019.netcdf.zip
    total_precipitation_2020.netcdf.zip
    total_precipitation_2021.netcdf.zip
    total_precipitation_2022.netcdf.zip
    total_precipitation_2023.netcdf.zip
    2m_temperature_2015.netcdf.zip
    2m_temperature_2016.netcdf.zip
    2m_temperature_2017.netcdf.zip
    2m_temperature_2018.netcdf.zip
    2m_temperature_2019.netcdf.zip
    2m_temperature_2020.netcdf.zip
    2m_temperature_2021.netcdf.zip
    2m_temperature_2022.netcdf.zip
    2m_temperature_2023.netcdf.zip
    
    For more information on this code visit:
        https://github.com/AdityaSwarup/ERA5-Land_data_downloads
    
    History
    -------
    Written by - Aditya Swarup Sep 2023
    '''
    
    c = cdsapi.Client()
    
    assert os.path.exists(path), \
        "Path unspecified. Please ensure that you have checked where your files will be downloaded. If so, input it in the variable 'path'."
    
    
    i = start_year
    
    years = []
    
    while i <= end_year:
        years.append(str(i))
        i += 1
    
    lst_of_files = [] # A list of all your downloaded files should occur here.
    
    for variable in variables: 
        for year in years:    
            c.retrieve(
                'reanalysis-era5-land',
                {
                    'variable': [
                        variable,
                    ],
                    'year': year, 
                    'month': ['01','02','03','04','05','06','07','08','09','10','11','12',],
                    'day': [
                        '01', '02', '03',
                        '04', '05', '06',
                        '07', '08', '09',
                        '10', '11', '12',
                        '13', '14', '15',
                        '16', '17', '18',
                        '19', '20', '21',
                        '22', '23', '24',
                        '25', '26', '27',
                        '28', '29', '30',
                        '31',
                    ],
                    'time': [
                        '00:00', '01:00', '02:00',
                        '03:00', '04:00', '05:00',
                        '06:00', '07:00', '08:00',
                        '09:00', '10:00', '11:00',
                        '12:00', '13:00', '14:00',
                        '15:00', '16:00', '17:00',
                        '18:00', '19:00', '20:00',
                        '21:00', '22:00', '23:00',
                    ],
                    'area': [
                        30, -20, 27,
                        -18,
                    ],
                    'format': 'netcdf.zip',
                },
                variable + '_' + year + '.netcdf.zip')
            
            lst_of_files.append(variable + '_' + year + '.netcdf.zip')
    
    for file in lst_of_files:
        if os.path.isfile(path + '/' + file):
            print(file + " has been downloaded!")
        
        else:
            print('There has been an issue with' + file + 
                  ". Please check your path folder and potentially redownload the file.")
                



# Testing!! 
###############################################################################

# Test 1 (Raising an AssertionError due to path not specified.):   
# lst_of_variables = ['10m_u_component_of_wind', '10m_v_component_of_wind'] 
# path_unspecified = 'testing'
# data_download(lst_of_variables, 2020, 2023, path_unspecified) #Should return AssertionError

# Test 2 (All files have been downloaded)
# lst_of_variables = ['10m_u_component_of_wind', '10m_v_component_of_wind'] 
# path_correct = '/Users/adityaswarup/.spyder-py3/ERA5 test'
# data_download(lst_of_variables, 2020, 2023, path_correct) #Should download all files + print messages saying it has been downloaded.

    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
