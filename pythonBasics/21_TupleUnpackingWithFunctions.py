stock_prices =[('Apple',200),('Google',300),('Amazon',500),('MicroSoft',600),('Citi',600)]
for item in stock_prices:
    print(item)

for item in enumerate(stock_prices):
    print(item)

for stock_name,stock_price in stock_prices: # Tuple Unpacking
    print(stock_price+0.1*stock_price)

def find_highest_hrs_emp_name1(arglist):
    emp_names=[]
    emp_hrs = []
    for x,y in arglist:
        emp_names.append(x)
        emp_hrs.append(y)

    highest_hrs = max(emp_hrs)
    index_of_highest_hrs = emp_hrs.index(highest_hrs)
    highest_hrs_emp_name = emp_names[index_of_highest_hrs]
    return highest_hrs_emp_name

def find_highest_hrs_emp_name2(arglist):
    curr_max_hrs = 0
    emp_of_the_month = ''
    for empname,emphrs in arglist:
        if emphrs > curr_max_hrs:
            curr_max_hrs = emphrs
            emp_of_the_month = empname
        else:
            pass
    return (curr_max_hrs,emp_of_the_month)


work_hours =[('Ramana',100),('Billy',140),('Gowri',50),('Swamy',300),('Chinna',400)]
# Write a function to unpack the above list of tuples and find the highest hrs employee name
empname = find_highest_hrs_emp_name1(work_hours)
print(empname)

empname = find_highest_hrs_emp_name2(work_hours)
print(empname)

maxhrs,empl_name = find_highest_hrs_emp_name2(work_hours) # This is also tuple unpacking,
# The tuple will assign the results to the variables maxhrs,empl_name directly
print(maxhrs)
print(empl_name)
