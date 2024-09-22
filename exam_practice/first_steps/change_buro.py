bitcoin = int(input())
chinese_joana = float(input())
commission = float(input())

bitcoin_amount = bitcoin * 1168
chinese_joana_change = chinese_joana * 0.15
chinese_joana_change_levs = chinese_joana_change * 1.76
sum_in_levs = bitcoin_amount + chinese_joana_change_levs
sum_in_euro = sum_in_levs / 1.95
commission_amount = sum_in_euro * (commission / 100)
total_amount = sum_in_euro - commission_amount

print(f'{total_amount:.2f}')
