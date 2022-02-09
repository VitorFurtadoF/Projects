%seasonal adjustment of weekly claims data
clear;
clc;

addpath('/Users/vitor/Desktop/Senior_Thesis/Weekly_Seasonal_Adjustment');

echo off
%Fuel_Price_Ethanol

Fuel = readmatrix('../Weekly_Seasonal_Adjustment/Spreadsheets/RealValues/Fuel_Price_Ethanol_RealValues_T.csv', 'Range', 'B2');

for jx=1:1
    s = x11(Fuel(1:end,jx),52);
    sa_Fuel(:,jx) = adjout(s.d11,1,3);
    clear s
end

writematrix(sa_Fuel, '/Users/vitor/Desktop/Senior_Thesis/Spreadsheets/SeasonalAdjustment/Fuel_Price_Ethanol_RealValues_SA.csv');

