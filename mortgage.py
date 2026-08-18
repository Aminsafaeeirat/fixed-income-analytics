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



mortgage=Mortgage(500000,0.05,25)


print(mortgage.amortization_schedule()[:5])