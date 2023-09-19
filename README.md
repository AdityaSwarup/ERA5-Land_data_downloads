# ERA5-Land_data_downloads

This repository includes the script used to download data over multiple variables and multiple years. 

## Variables
The following table below is a conversion of [RDRS-v2.1](https://github.com/julemai/CaSPAr/wiki/Available-products#list-of-available-variables-in-rdrs-v2-and-rdrs-v21) 
(the list of avaliable RDRS-v2.1 variables) variables to their equivalent in [ERA5-Land](https://confluence.ecmwf.int/display/CKB/ERA5-Land%3A+data+documentation#ERA5Land:datadocumentation-Dataformat)
(the list of available ERA5-Land variables). 
| RDRS | v2.1 Name | Era5-Land | 
| :-  | :-       | :-       |
RDRS_v2.1_A_PR0_SFC |	Quantity of precipitation (CaPA)	|total_precipitation
RDRS_v2.1_P_PR0_SFC |	Quantity of precipitation (model) |	total_precipitation
RDRS_v2.1_P_FI_SFC	| Surface incoming infrared flux|	surface_net_solar_radiation
RDRS_v2.1_P_HU_09944|	Specific humidity	|Will need to be [calculated](https://confluence.ecmwf.int/pages/viewpage.action?pageId=171411214), not archived in Era5. Variables needed for this are as follows: surface_pressure, 2m_temperature, 2m_dewpoint_temperature.
RDRS_v2.1_P_P0_SFC	|Surface pressure	|surface_pressure	
RDRS_v2.1_P_FB_SFC	|Downward solar flux	|surface_solar_radiation_downwards
RDRS_v2.1_P_TT_1.5m	|Air temperature	|2m_temperature	
RDRS_v2.1_P_UUC_10m	|corrected U-component of the wind (along West-East direction)	|10m_u_component_of_wind (this is the corrected version)
RDRS_v2.1_P_VVC_10m	|corrected V-component of the wind (along South-North direction)	|10m_v_component_of_wind (this is the corrected version)
RDRS_v2.1_P_UVC_10m |	Wind Modulus (derived using UU and VV)	|Must be calculated with modulus formula which is as follows, $\sqrt{u^2 + v^2}$ which gives us the wind speed. 

