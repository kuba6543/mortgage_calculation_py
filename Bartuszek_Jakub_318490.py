from rich.console import Console
from rich.table import Table
from rich.prompt import FloatPrompt, IntPrompt

def read_args():
    amount_of_mortgage=IntPrompt.ask("Enter amount of mortgage")
    bank_fee=FloatPrompt.ask("Enter bank fee (in per cent)")
    interest_rate=FloatPrompt.ask("Enter interest rate (in per cent, yearly)")
    period_of_payment=IntPrompt.ask("Enter period of payment (in months)")
    return amount_of_mortgage, bank_fee, interest_rate, period_of_payment

def calculations(amount_of_mortgage, bank_fee, interest_rate, period_of_payment):
    installment = (amount_of_mortgage*(interest_rate/100)*(1+bank_fee/100))/(12*(1-((12/(12+(interest_rate/100)))**period_of_payment)))
    return installment

def make_a_table(installment, period_of_payment):
    sum_of_installments = 0
    table = Table(title="Mortgage installments")

    table.add_column("Month")
    table.add_column("Installment")
    table.add_column("Sum of all installments")

    for i in range(period_of_payment):
        sum_of_installments+=installment
        table.add_row(str(i+1),str(round(installment,2)),str(round(sum_of_installments,2)))
    
    console = Console()
    console.print(table)

amount_of_mortgage,bank_fee,interest_rate,period_of_payment = read_args()    

make_a_table(calculations(amount_of_mortgage,bank_fee,interest_rate,period_of_payment),period_of_payment)