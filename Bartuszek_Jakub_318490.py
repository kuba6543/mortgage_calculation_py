from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt



def read_data():
    amount_of_mortgage=Prompt.ask("Enter amount of mortgage")
    bank_fee=Prompt.ask("Enter bank fee (in per cent)")
    interest_rate=Prompt.ask("Enter interest rate (in per cent, yearly)")
    period_of_payment=Prompt.ask("Enter period of payment (in months)")
    return amount_of_mortgage, bank_fee, interest_rate, period_of_payment

def calculations(amount_of_mortgage, bank_fee, interest_rate, period_of_payment):
    interest_installment=0
    capital_installment = (amount_of_mortgage*(1+bank_fee/100))/(period_of_payment)
    for i in range(period_of_payment):
        interest_installment[i] = (((amount_of_mortgage*(1+bank_fee/100))-(i*capital_installment))*interest_rate/100)/12
    return capital_installment, interest_installment

def make_a_table(capital_installment, interest_installment, period_of_payment):
    table = Table(title="Mortgage installments")

    table.add_column("Month")
    table.add_column("Capital Installment")
    table.add_column("Interest Installment")
    table.add_column("Sum of installments")

    for i in range(period_of_payment):
        table.add_row(i,capital_installment,interest_installment,interest_installment+capital_installment)
    
    console = Console()
    console.print(table)
    return

read_data()
calculations(read_data())