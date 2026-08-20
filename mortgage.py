class Mortgage:

    def __init__(self,principal,annual_rate,years):

        self.principal=principal
        self.annual_rate=annual_rate
        self.years=years

    def monthly_payment(self):
        r=self.annual_rate/12
        n=self.years*12

        return(self.principal*((r*(1+r)**n)/((1+r)**n-1)))
    

    def amortization_schedule(self):
        balance=self.principal

       



        schedule=[]
        monthly_payment = self.monthly_payment()

        for month in range(1, self.years * 12 + 1):

            interest_payment = balance * self.annual_rate / 12
            principal_payment = monthly_payment - interest_payment

            balance = balance - principal_payment

            schedule.append([month,interest_payment,principal_payment,balance])

        return schedule
    

    def price(self,discount_rate):

        monthly_discount_rate=discount_rate/12
        n=self.years*12
        payment=self.monthly_payment()

        price=0
        for month in range (1,n+1):

            price+=(1/(1+monthly_discount_rate)**month)*payment
        return price
    

    def dv01(self,discount_rate):

        bp=0.0001

        price_rate_down=self.price(discount_rate-bp)

        price_rate_up=self.price(discount_rate+bp)


        return (price_rate_down-price_rate_up)/2


    def modified_duration(self,discount_rate):

        dv01=self.dv01(discount_rate)

        bp=0.0001

        price=self.price(discount_rate)

        return(dv01/(price*bp))
    

    def convexity(self,discount_rate):

        bp=0.0001

        price=self.price(discount_rate)

        price_rate_down=self.price(discount_rate-bp)

        price_rate_up=self.price(discount_rate+bp)


        return((price_rate_down+price_rate_up-2*price)/(price*bp**2))






mortgage=Mortgage(500000,0.05,25)


print(mortgage.DV01(0.05))