# Sample_Code

## Description

During the past two years in Undergrad, I have worked with two projects that involved Python:
    - As an undergrad Research Assistant at the University of Notre Dame, I worked on the Database for the BLS model (Baumeister, 
    Christiane, et al. “Tracking Weekly State-Level Economic Conditions.” 2021). This project developed a 
    weekly economic activity index for the 50 U.S. states. I used Python to request and treat the data, run a dynamic factor model
    to create the index, and output the results. 

    - In my senior thesis, I am adapting the BLS model to Brazil, as I am creating the first weekly economic activity index for Brazil
    to use a dynamic factor model. 


In this folder, I have added the files used in my Senior Thesis to create the input file for the dynamic factor model. To run the codes, use
the script "SeniorThesis_Main.py". It cointains a list of all the series used in the model. Every script contains a list describing the series 
involved in each step. 


Definition: 
SeniorThesis_IPEADATA.py: Get the series released by IpeaData.

SeniorThesis_FED.py: Get the series released by FRED.

SeniorThesis_CEIC.py: Get the series released by CEIC.

SeniorThesis_Apple.py: Get the series released by Apple.

SeniorThesis_DailyCollapse.py: Convert series from daily frequency to weekly frequency.

SeniorThesis_IterpolateInflation.py: Iterpolate monthly inflation into weekly. 

SeniorThesis_DateAdjustment_weekly.py: Adjust report date of weekly frequency, moving it to Saturdays

SeniorThesis_RealValues.py: Deflate required series.

/Scripts/SeniorThesis_MovingAverage.py: Get moving average for some of the series.

SeniorThesis_SeasonalAdjustment.py: Seasonal Adjustment

SeniorThesis_DateAdjustment.py: Adjust report date of monthly/quarterly series

SeniorThesis_MainOutput.py: Create SeniorThesis_MainOutput.csv file. 
