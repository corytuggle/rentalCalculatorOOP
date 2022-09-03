### Create a Cash-on-Cash Return on Investment Calculator

class CocRoiCalc():
    def __init__(self):
        pass

# PROMPT INCOME INFO

    def setIncome(self, income):
        self.income = income

    def getIncome(self):
        print('\nAlright, let\'s calculate your income for your property.\nFirst, we need to get a bit of information from you about your rental property.')
        
        while True:
            rental_income = input('\nWhat will you be charging in rent per month?\n\nInput:  $')
            try:
                int(rental_income)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')
        
        while True:
            laundry_income = input('\nWhat amount of income do you anticipate to receive from laundry services on your property per month?\n\t(if there are no laundry services, input "0")\n\nInput:  $')
            try:
                int(laundry_income)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        while True:
            storage_income = input('\nWhat amount of income do you anticipate to receive from storage services on your property per month?\n\t(if there are no storage services, iNput "0")\n\nInput:  $')
            try:
                int(storage_income)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        while True:
            misc_income = input('\nLastly, what amount of income, if any, do you aniticipate to receive from other miscellaneous services on your property per month?\n\t(if there are no other miscellaneous services, input "0")\n\nInput:  $')
            try:
                int(misc_income)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        self.income = int(rental_income) + int(laundry_income) + int(storage_income) + int(misc_income)

        print(f'\nIt looks like your total monthly income for this property comes out to ${self.income}!')

# PROMPT EXPENSES INFO

    def setExpense(self, expense):
        self.expense = expense

    def getExpense(self):
        print('\nAlright, let\'s calculate your expenses for your property.\nFirst, we need to get a bit of information from you about your rental property.')
        
        while True:
            tax_expense = input('\nWhat will you be paying in taxes on your property per month?\n\nInput:  $')
            try:
                int(tax_expense)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        while True:    
            insurance_expense = input('\nWhat amount will you be paying for insurance coverage on your property per month?\n\t(if your tenant pays for insurance, input "0")\n\nInput:  $')
            try:
                int(insurance_expense)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        while True:
            utilities_expense = input('\nWhat amount will you be paying for utilities on your property per month?\n\t(if your tenant pays for utilities, input "0")\n\nInput:  $')
            try:
                int(utilities_expense)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        while True:
            vacancy_expense = input('\nWhat amount will you be setting aside in case of vacancy on your property per month?\n\t(if you are not setting any aside, input "0")\n\nInput:  $')
            try:
                int(vacancy_expense)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        while True:
            repair_expense = input('\nWhat amount will you be setting aside to cover repairs and capital expenditures for your property per month?\n\t(if you have no budget for repairs or cap ex, input "0")\n\nInput:  $')
            try:
                int(repair_expense)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        while True:
            propman_expense = input('\nWhat amount will you be paying on property management for your property per month?\n\t(if you have no property management, input "0")\n\nInput:  $')
            try:
                int(propman_expense)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        while True:
            mortgage_expense = input('\nWhat amount will you be paying on the mortgage for your property per month?\n\t(if you have no mortgage, input "0")\n\nInput:  $')
            try:
                int(mortgage_expense)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        while True:
            misc_expense = input('\nLastly, what amount of miscellaneous expenses (HOA fees, lawn maintenance, etc.), if any, do you aniticipate to pay on your property per month?\n\t(if you have no miscellaneous expenses, input "0")\n\nInput:  $')
            try:
                int(misc_expense)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        self.expense = int(tax_expense) + int(insurance_expense) + int(utilities_expense) + int(vacancy_expense) + int(repair_expense) + int(propman_expense) + int(mortgage_expense) + int(misc_expense)

        print(f'\nIt looks like your total monthly expenses for this property come out to ${self.expense}!')

# RELAY CASH FLOW INFO

    def setCashFLow(self, cash_flow):
        self.cash_flow = cash_flow

    def cashFlow(self):
        self.cash_flow = (property.income - property.expense)

        print('\nOk! let\'s calculate your Cash Flow now.\n\nYour Cash Flow is calculated by taking your property income (which amounts to $' + str(property.income) + '/month) and subtracting your property expenses (which amount to $' + str(property.expense) + '/month).\n\nThat means your Cash Flow comes out to $' + str(property.cash_flow) + ' per month.\n\nAll that\'s left is to calculate your investments and then we can tell you your Cash-on-Cash Return on Investment!')

# RELAY RETURN ON INVESTMENT

    def investReturn(self):
        print('\nWe almost have all of the information we need!\n\nWe just need a little info about the investments you\'ve made in your property.')

        while True:
            inv_downpayment = input('\nHow much was the down payment you paid on your property?\n\nInput:  $')
            try:
                int(inv_downpayment)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        while True:
            inv_closing = input('\nHow much did you pay in closing costs on your property?\n\t(if you did not pay closing costs, input "0")\n\nInput:  $')
            try:
                int(inv_closing)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        while True:
            inv_rehab = input('\nHow much have you spent to rehabilitate your property?\n\t(if you did not need to rehabilitate your property, input "0")\n\nInput:  $')
            try:
                int(inv_rehab)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')
            
        while True:
            inv_misc = input('\nHow much, if any, have you paid in miscellaneous investments on your property?\n\t(if you have no miscellaneous investments, input "0")\n\nInput:  $')
            try:
                int(inv_misc)
                break
            except ValueError:
                print('\nPlease input a valid integer amount.')

        self.investment = int(inv_downpayment) + int(inv_closing) + int(inv_rehab) + int(inv_misc)

        self.inv_return = ((int(property.cash_flow) * 12) / int(property.investment)) * 100

        print('\nThat\'s the last of our questions. Your Cash-on-Cash Return on Investment is calculated by taking your yearly Cash Flow (which amounts to $' + str(int(property.cash_flow) * 12) + '/year) and dividing it by the total amount of money invested into your property (which amounts to $' + str(property.investment) + '/month). We then take that figure and multiply it by 100 to get your Return on Investment Percentage!\n\n\tYour Cash-on-Cash Return on Investment comes out to :  ' + str(self.inv_return) + '%!')

        if float(self.inv_return) <= 7.5:
            print('\tThis may not be an investment worth your time....')
        
        elif float(self.inv_return) <= 15:
            print('\tThis seems like a safe investment that could lead to solid returns.')
        
        elif float(self.inv_return) > 15:
            print('\tThis seems to be a great ivenstment that should lead to fantastic returns!')


# RUN PROGRAM
# Prompt for user option

property = CocRoiCalc()


def run():
    print('\nThank you for using our Cash on Cash Return on Investment calculator!\nWhere would you like to start?')

    while True:
        option = input('\nPlease select from the following options:\n\n\tI: Calculate the Income on my property\n\tE: Calculate the Expenses on my property\n\n\tC: Calculate my Cash Flow (Income and Expenses calculations required)\n\tR: Calculate my Return on Investment (Cash Flow calculations required)\n\n\tQ: Quit terminal\n\nInput:  ')

        if option.lower() == 'q':
            print('Thank you for visiting our website! We hope to serve you again soon!')
            break
        
        elif option.lower() == 'i':
            property.getIncome()
        
        elif option.lower() == 'e':
            property.getExpense()
        
        elif option.lower() == 'c':
            property.cashFlow()
        
        elif option.lower() == 'r':
            property.investReturn()
        
        else:
            print('\nPlease select a valid option from the menu.')

run()
