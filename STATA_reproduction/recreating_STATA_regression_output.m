%% Introduction

%Name: Vitor Furtado Farias
%Class: Econometrics I
%Activity: PS12


%% Configuration

clear, clc
data = xlsread('cps09mar.xlsx');

%% Model 1

%Toy Model based on file cps09mar.xlsx available at 
%https://www.ssc.wisc.edu/~bhansen/econometrics/

%Regressing ln_wage on education, experience, and experience_sq

o = ones(length(data),1);
x0 = data(1:end,[2,3,4]);
x = [x0,o];
y = data(1:end,1);
a = .05;
n = length(data);
k = size(x,2);

variables = ["Education"; "Experience"; "Experience_sq"; "Constant"];
%variables = ["ratio", "Constant"];
names = ["Variable", "Coef.", "Std. Err.", "Robust Std. Err.", ...
    "t", "p value", "Coef. Int. (lower)", "Conf. Int. (upper)"];
info = ["Num Obs"; strcat("F[", string(k-1),",", string(n-k),"]"); ...
    "Prob > F"; "R-squared"; "Adj R-Squared"; "Root MSE"];
headings = ["Source", "SS", "df", "MS"];
labels = ["Model"; "Residual"; "Total"];

robustregress(x,y,n,k,a,headings,labels,info,variables,names);

%% Function

function [table_1, table_2, Regression_table] = robustregress(x,y,n,k,a,headings,labels,info,variables,names);
    
    y_mean = mean(y);
    
    %beta1
    beta1 = inv(x'* x) * (x' * y);
    y_predicted = x * beta1;
    e_sq = (y - y_predicted).^2;
    s_sq = (1/(n-k)) * sum(e_sq);
    
    %SS
    %SST/SSR    
    tss = 0;
    ssr = 0;
    interior = 0;
    for i = 1:n
        tss  = tss + (y(i) - y_mean)^2;
        ssr = ssr + (y(i) - (x(i,:) * beta1))^2;
        interior = interior + (x(i,:)' * x(i,:) * e_sq(i));
    end
    
    %stderhom and stderhet
    stderhom = diag(sqrt(s_sq * inv(x' * x)));
    stderhet = diag(sqrt((n/(n-k)) * inv(x'* x) * interior * inv(x'* x)));
    %SSM
    ssm = tss - ssr;
    
    %-------------
    %MS
    msm = ssm / (k-1);
    msr = ssr / (n-k);
    tms = tss / (n-1);

    %-------------
    %Other Calculations
    mse = sqrt(msr);
    r2 = ssm/tss;
    adjr2 = 1 - (ssr*(n-1))/(tss*(n-k));
    ftest = msm / msr;
    fvalue = 1 - fcdf(ftest,k-1,n-k);
    %p, cilow, cihigh
    t = beta1./stderhom;
    p = 2*(1-tcdf(abs(t),n-k));
    cilow = beta1 - tinv(1-a/2,n-k) * stderhom;
    cihigh = beta1 + tinv(1-a/2,n-k) * stderhom;
    
    % Table 
    data = [n; ftest; fvalue; r2; adjr2; mse];
    table_1 = table(labels, [ssm;ssr;tss], [k-1;n-k;n-1], [msm; msr; tms], 'VariableNames', headings)
    table_2 = table(info,data)
    Regression_table = table(variables, beta1, stderhom, stderhet, t, p, cilow, cihigh, 'VariableNames', names)

end