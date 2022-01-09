# Sample_Code

## Description

During the past two years in Undergrad, I have worked extensively on creating macroeconomic activity index in two different projects:

    - As an undergrad Research Assistant at the University of Notre Dame, I worked on the Database for the BLS model 
    (Baumeister, Christiane, et al. “Tracking Weekly State-Level Economic Conditions.” 2021). This project developed a 
    weekly economic activity index for the 50 U.S. states. I used Python to request and treat the data, run a dynamic 
    factor model to create the index, and output the results. 

    - In my senior thesis, I am adapting the BLS model to Brazil, as I am creating the first weekly economic activity 
    index for Brazil to use a dynamic factor model. 


Given the intersaction of my Senior Thesis with the confidential files of my Research Assistant position, I am only adding here a reduced version
of two out of 35 scripts used in my seniors thesis.


SAMPLE1 : This file uses Selenium to request a sample of CEIC series used in my Senior Thesis and output the requested information in a csv file in a
standard format. OUTPUT: Sample_data.csv

SAMPLE2: This file treats the data acquired in Sample1 and output it in the format required by the dynamic factor model scripts. OUTPUT: Sample_Data_Treated.csv

I have hidden/modified some details of the original scripts throughout the code. 
