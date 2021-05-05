def calculateTotalBill(priceArray, timeofShopping, primeCustomer):

    all_price = priceArray[1:]
    total = sum(all_price)
    hr =  int(timeofShopping[:2])
    min = int(timeofShopping[3:5])  
    s = ''

    am_or_pm = 'am' if hr<=11 else 'pm'

    if int(hr > 12):
        hr = hr % 12

    if len(all_price) == 2:
        if (hr == 11 and am_or_pm == 'pm') or (hr == 12 and min == 0 and am_or_pm=='am'):
            total = max(all_price)

    s += 'Unit Price'.ljust(18) + ': ' + str(total).rjust(len(str(total))+1) + '\n'

    if am_or_pm == 'pm':
        if (hr == 10) or (hr == 11 and min == 0):
            s += '30% discount'.ljust(18) + ': ' +'-'+ str(int(total*0.3)) + '\n'
            total = total - total * 0.3

    if total >= 1000:
        total -= 100
        s += 'Flat R100 discount: '.ljust(18) + '-'+ str(100) + '\n'
    else: 
        s += 'Flat R100 discount: '.ljust(18) +  str(0) + '\n'

    w = len('Deliverycharge')
    s += '-' * 25 + '\n'
    s += 'Total'.ljust(w) + ': ' + str(int(total)) + '\n'
    s += 'Tax'.ljust(w) + ': ' + str(int(total*0.12)) + '\n'
    total += total*0.12
    
    if primeCustomer:
        s += 'Deliverycharge'.ljust(w) + ': ' + str(0) + '\n'
    else:
        s += 'Deliverycharge'.ljust(w) + ': ' + str(40) + '\n'
        total += 40
    
    s += '-' * 25 + '\n'
    s += 'Net Total'.ljust(w) + ': ' + str(int(total)) + '\n'
        
    print(s)


calculateTotalBill(priceArray=[2, 400, 500], timeofShopping='22:30:00', primeCustomer=0)