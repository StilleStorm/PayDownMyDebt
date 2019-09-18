# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 16:53:55 2018

@author: StilleStorm
"""
# Example debt balance and interest rate per annum
balance = 999999
annualInterestRate = 0.18

# basic variables. m for months. monthly interest rate speaks for itself.
m = 12
monthlyInterestRate = annualInterestRate / 12

#Defining main outstanding debtr couting function
def outstandingDebt(m, ans):
    """function calculates outstanding debt for m months in future.
    it counts only minimal payments paid. Rounded to 2 decimal places"""
    
    #Set of variables for iteration
    #count for counting down months, pb for first time previus balance, analogic for current balance
    count = m
    currbalance = balance
    
    #Iteration for counting  down month by month saldo
    while count > 0:
        #changing current balance by lowering amout by monthly payment for current month
        #and adding monthly interest rates
        #print 
        currbalance = round(currbalance - ans, 2)
        currbalance = round(currbalance + currbalance * monthlyInterestRate, 2)
        #changingcount
        count -= 1
        # remove hashtag in line below if you want to see month by mont saldo
        #print(currbalance)
    
    #when cont for numbers of months runs down print summary of balance after given period    
    if count == 0:
        saldo = round(currbalance, 2)
        return saldo

#Defining function for bisection search of regular monthly payment to pay down debt
def bisectpayments(balance, monthlyInterestRate):
    """Find minimum monthly payment to pay down debt
    balance is current balance of debt
    monthlyInterestRate is exactly what it is named
    it uses outstandingDebt function where you can eventually tweak period of payments"""
    

    epsilon = 0.01 #precision meter
    low = balance / m #initial lower bound. Balance dealt in 12 without counting interest
    high = (balance * (1 + monthlyInterestRate) ** m) / m #initial higher bound. Balance paid with interest once after a year.
    ans = (high + low)/2.0 #initial guess for the answer
    
    #looping to check if f outstandingDebt will return proper saldo after each bisection and new guess.
    while abs(outstandingDebt(m, ans)) > epsilon:
        
        
        if outstandingDebt(m, ans) < 0: #if value of saldo after using bisected guess is lower than zero
            high = ans #higher bound is bisected ghuess
            ans = (high + low)/2.0 #and new guess is made
        
        elif outstandingDebt(m, ans) > epsilon: #if value of saldo after using bisected guess is higher than our precision marker
            low = ans #then lower bound is bisected guess
            ans = (high + low)/2.0 # and new guess is made
    
    print ("Lowest Payment: " + str(round(ans, 2)))  # print the amount of monthly payments to pay down debt  

#call function to print out stuff        
bisectpayments(balance, monthlyInterestRate) 
        
        
