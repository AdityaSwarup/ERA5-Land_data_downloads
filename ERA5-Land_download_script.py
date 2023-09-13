#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 15:38:02 2023

@author: adityaswarup
"""

import cdsapi

current_year = 2023
i = 2022 # make i whatever you want the start year to be.

years = []

# Appends all the years required as Str into years.
while i <= current_year:
    years.append(str(i))
    i += 1

def data_download(variable):
    # variable is of type str. It is any one of the variables
    # specified in the ERA5-Land documentation: 
    # https://confluence.ecmwf.int/display/CKB/ERA5-Land%3A+data+documentation#ERA5Land:datadocumentation-Dataformat
    c = cdsapi.Client()
    
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
                    60, -132, 26,
                    -60,
                ],
                'format': 'netcdf.zip',
            },
            variable + '_' + year + '.netcdf.zip')

data_download('total_precipitation')