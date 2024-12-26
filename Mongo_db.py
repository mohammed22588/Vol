import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["AutoTrading_bot"]

class Mongdb():
	def find(collection, ticker):
    mycol_24hrTicker = db["mycol_24hrTicker"]
    
	def add(collection, ticker, Event_time, Price_change_percent, Last_price, Volume, QuoteVolume, Count, Price_change_percent, Volume,QuoteVolume, Count, Price_change_percent, Volume, QuoteVolume, Count, 0, 0, 0, _hour, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, _hour)
	mycol_24hrTicker = db["mycol_24hrTicker"]
    
    def update_every24h_document(ticker, Event_time, Price_change_percent, Volume, QuoteVolume, Count, Price_change_percent, Last_price, Volume, QuoteVolume, Count, Volume, QuoteVolume, Count, 0, 0, 0, Volume, QuoteVolume, Count, Volume, QuoteVolume, Count, 0, 0, 0, 0, 0, _hour)
    mycol_24hrTicker = db["mycol_24hrTicker"]
    
    def update_every1h_document(ticker, Event_time, Price_change, Price_change_percent, Volume, QuoteVolume, Count, Price_change_percent, Last_price, Volume, QuoteVolume, Count, Volume, QuoteVolume, Count, 0, 0, 0, 0, 0, 0, 0, 0, _hour)
    mycol_24hrTicker = db["mycol_24hrTicker"]
    
    def update_document(ticker, Event_time, Price_change_percent, Volume, QuoteVolume, Count, Last_price, Total_Volume_24h, Total_Quote_Volume_24h, Volume, QuoteVolume, Count, Total_Volume_1h, Total_Quote_Volume_1h, Total_Count_1h, Volume, QuoteVolume, Count, Pct_Total_Volume_1h, Pct_Total_Count_1h, alerts_24h, alerts_1h, Tps_1h):
        mycol_24hrTicker = db["mycol_24hrTicker"]
       