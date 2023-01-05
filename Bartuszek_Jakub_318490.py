try:
    from rich.console import Console
    from rich.table import Table
    from rich.prompt import FloatPrompt, IntPrompt
except:
    raise Exception("Rich not installed, please install Rich using command: pip install rich")

def read_args():
    amount_of_mortgage=IntPrompt.ask("Enter amount of mortgage")
    bank_fee=FloatPrompt.ask("Enter bank fee (in per cent)")
    interest_rate=FloatPrompt.ask("Enter interest rate (in per cent, yearly)")
    period_of_payment=IntPrompt.ask("Enter period of payment (in months)")
    return amount_of_mortgage, bank_fee, interest_rate, period_of_payment

def calculations_of_installment(amount_of_mortgage, bank_fee, interest_rate, period_of_payment):
    wibor=[6.64,5.12]
    installment=[]
    if period_of_payment<13:
        interest_rate_with_wibor = interest_rate + float(wibor[0])
        for i in range(period_of_payment):
            installment.append((amount_of_mortgage*((interest_rate_with_wibor))/100)*(1+bank_fee/100)/(12*(1-((12/(12+((interest_rate_with_wibor)/100)))**period_of_payment))))
    if period_of_payment<25:
        interest_rate_with_wibor = interest_rate + float(wibor[0])
        for i in range(12):
            installment.append((amount_of_mortgage*((interest_rate_with_wibor))/100)*(1+bank_fee/100)/(12*(1-((12/(12+((interest_rate_with_wibor)/100)))**period_of_payment))))    
        interest_rate_with_wibor = interest_rate + float(wibor[1])
        for i in range(period_of_payment-12):
            installment.append((amount_of_mortgage*((interest_rate_with_wibor)/100)*(1+bank_fee/100))/(12*(1-((12/(12+((interest_rate_with_wibor)/100)))**period_of_payment))))
    else:
        interest_rate_with_wibor = interest_rate + float(wibor[0])
        for i in range(12):
            installment.append((amount_of_mortgage*((interest_rate_with_wibor)/100)*(1+bank_fee/100))/(12*(1-((12/(12+((interest_rate_with_wibor)/100)))**period_of_payment))))    
        interest_rate_with_wibor = interest_rate + float(wibor[1])
        for i in range(12):
            installment.append((amount_of_mortgage*((interest_rate_with_wibor)/100)*(1+bank_fee/100))/(12*(1-((12/(12+((interest_rate_with_wibor)/100)))**period_of_payment))))
        interest_rate_with_wibor = 5
        for i in range(period_of_payment-24):
            installment.append((amount_of_mortgage*((interest_rate_with_wibor)/100)*(1+bank_fee/100))/(12*(1-((12/(12+((interest_rate_with_wibor)/100)))**period_of_payment))))
    return installment

def make_a_table(installment, period_of_payment):
    sum_of_installments = 0
    table = Table(title="Mortgage installments")

    table.add_column("Month")
    table.add_column("Installment")
    table.add_column("Sum of all installments")

    for i in range(period_of_payment):
        sum_of_installments+=installment[i]
        table.add_row(str(i+1),str(round(installment[i],2)),str(round(sum_of_installments,2)))
    return table

def print_table(table):
    console = Console()
    console.print(table)

amount_of_mortgage,bank_fee,interest_rate,period_of_payment = read_args()    
installment = calculations_of_installment(amount_of_mortgage, bank_fee, interest_rate, period_of_payment)
table = make_a_table(installment,period_of_payment)
print_table(table)