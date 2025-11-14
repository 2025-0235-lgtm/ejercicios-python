cards = [
    '4242424242424242',
    '4000056655665556',
    '5555555555554444',
    '378282246310005',
    '6011111111111117'
]

for x in cards:
    maskedCard = ""

    if x.startswith('4'):
        maskedCard = x[:4] + 'XXXXXXXX' + x[-4:]
    elif x.startswith('5') or x.startswith('3'):
        maskedCard = x[:6] + 'XXXXXX' + x[-4:]
    elif x.startswith('6'):
        maskedCard = x[:4] + 'XXXXXX' + x[-6:]
    else:
        continue

    print(maskedCard)
