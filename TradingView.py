from tradingview_ta import TA_Handler, Interval

output = TA_Handler(symbol='BTCUSDT', screener = 'Crypto', exchange='Binance', interval=Interval.INTERVAL_1_MINUTE)

#output.get_analysis().summary
#output.get_analysis().indicators

symbols = ['ETHUSDT', 'BNBUSDT', 'XECUSDT', 'MATICUSDT', 'SOLUSDT', 'EOSUSDT',
        'BCHUSDT', 'ONEUSDT', 'GRTUSDT', 'AVAXUSDT']

for symbol in symbols:
    output = TA_Handler(symbol=symbol, screener = 'Crypto', exchange='Binance', interval=Interval.INTERVAL_1_MINUTE)
    print('Symbol : ' + symbol)
    print(output.get_analysis().summary)
