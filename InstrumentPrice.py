#Code for SOCIETE GENERALE Support/DevOPS position by VANEESH JHA

import datetime
import yfinance as yf

##used yfinance - yfinance is an api to connect to Yahoo Finance

##function to get price for given instrument
def instrumentPrice(instrument=""):  
    if isinstance(instrument, str):        
        instrumentdata=yf.Ticker(instrument) ##ticker function allows to access ticker data
        tickerinfo=instrumentdata.info

        if tickerinfo['logo_url'] == '':
            print("Instrument Name Does not exist")
        else:
            instrumentName = tickerinfo['shortName'] ##From output dictionary we get Instrument name by using key value pairs
            today = datetime.datetime.today().isoformat() ##getting current date in order to get the latest price
            DF = instrumentdata.history(period='1d',start="2021-1-1",end=today[:10])
            price = DF['Close'].iloc[-1]
            print(instrumentName + " PRICE: " + str(price))
    else:
        print("Enter valid values")
    

val = input("Enter INSTRUMENT NAME: ")
instrumentPrice(val)
