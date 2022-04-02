#payrollHeader includes these factors = ["Employee name", "Hours Worked", "Pay Rate", "OT Pay", "Gross Pay", "Fed Tax", "State Tax", "FICA", "Net Pay"]

import pandas as pd

mydataset = {
'Employee' : [],
'Hours Worked':[],
'Pay Rate':[],
'Gross Pay': [],
'Fed Tax': [],
'State Tax': [],
'Fica': [],
'Net Pay': [],
}
#i created a dictionary that will create columned list of everything that needs to displayed

#the main script that will be loaded into the dictionary as an output
def main():
    global mydataset
    name = input("Enter Employee Name: ")
    hoursWorked = input("Enter hours employee worked: ")
    payRate = input("Enter Employee's pay rate:  ")
#these are the 3 things that need to be inputed by the user
#the main if/else script for the code to work
    if int(hoursWorked) > 40:
        overtime = int(hoursWorked) - 40
        overtimePayRate = float(payRate) * 1.5
        overtimePay = overtime * overtimePayRate
        grossPay = 40 * float(payRate) + float(overtimePay)
    else:
        grossPay = round((int(hoursWorked) * int(payRate)), 2)
    fedTax = round((grossPay * 0.10), 2)
    stateTax = round((grossPay * 0.06), 2)
    fica = round((grossPay * 0.03), 2)
    totalDeduct = round((fedTax + stateTax + fica), 2)
    netPay = grossPay - totalDeduct
#main script ends, now every variable needs to be appended to the pandas dictionary
    mydataset['Employee']+= [name]
    mydataset['Hours Worked']+= [hoursWorked]
    mydataset['Pay Rate']+= [payRate]
    mydataset['Gross Pay']+= [grossPay]
    mydataset['Fed Tax']+= [fedTax]
    mydataset['State Tax']+= [stateTax]
    mydataset['Fica']+= [fica]
    mydataset['Net Pay']+= [netPay]

#below is how I call back the dictionary
    myvar = pd.DataFrame.from_dict(mydataset)
    pd.set_option("display.max_rows",None,"display.max_columns", None,"display.width",None)
#the line right above is how i formatted the pandas display to not truncate any of the columns
    print(myvar)

counter = 0
while counter != 10:
    main()
    counter += 1
#this argument is what loops the code for 10 times

