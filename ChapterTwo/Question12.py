#(7% Investment Return) Some investment advisors say that it’s
#reasonable to expect a 7% return over the long term in the stock market.
#Assuming that you begin with $1000 and leave your money invested,
#calculate and display how much money you’ll have after 10, 20 and 30
#years. Use the following formula for determining these amounts:
#a = p(1 + r)**n
#where
#p is the original amount invested (i.e., the principal of $1000),
#r is the annual rate of return (7%),
#n is the number of years (10, 20 or 30) and
#a is the amount on deposit at the end of the
#nth year.


p = 1000
r = 0.07
n1 = 10
n2 = 20
n3 = 30

#After 10 years
tenth_year_amount_on_deposit = p * ((1 + r)**n1)
print("The ROI after the tenth year is", tenth_year_amount_on_deposit)

#After 20 years
twentieth_year_amount_on_deposit = p * ((1 + r)**n2)
print("The ROI after the twentieth year is", twentieth_year_amount_on_deposit)

#After 30 years
thirtieth_year_amount_on_deposit = p * ((1 + r)**n3)
print("The ROI after the thirtieth year is", thirtieth_year_amount_on_deposit)
