
import Mongo_db as Mongdb
import Eqution as Eq
import Telegram as Tb
from os import  system
print(system("cls"))

def volume_24(ticker, Event_time, Price_change, Price_change_percent, Weighted_average_price, Last_price, Open_price, High_price, Low_price, Volume, QuoteVolume, Count,
	Last_quantity, Best_bid_price, Best_bid_quantity, Best_ask_price, Best_ask_quantity,date_time, time_stamp , _year, _month, _day, _hour, _minute, _secand
	):
	
	find_ticker = Mongdb.mycol_24hrTicker.find_one({"ticker": ticker})
# New ticker
	if find_ticker == None:
		print("New ticker", ticker)
		New_ticker = {"ticker":ticker, "Event_time":Event_time, "Price_change_percent":Price_change_percent, "Last_price":Last_price,
			
			"Volume":Volume, "QuoteVolume":QuoteVolume, "Count":Count, "Price_change_percent":Price_change_percent,

			"Start_Volume_24h":Volume, "Start_Quote_Volume_24h":QuoteVolume, "Start_Count_24h":Count, "Start_Pct_24h":Price_change_percent,
			"Last_Volume_24h":Volume, "Last_Quote_Volume_24h":QuoteVolume, "Last_Count_24h":Count,
			"Total_Volume_24h":0, "Total_Quote_Volume_24h":0, "Total_Count_24h":0,

			"Start_Volume_1h":Volume, "Start_Quote_Volume_1h":QuoteVolume, "Start_Count_1h":Count, "Start_Pct_1h":Price_change_percent,
			"Last_Volume_1h":Volume, "Last_Quote_Volume_1h":QuoteVolume, "Last_Count_1h":Count,
			"Total_Volume_1h":0, "Total_Quote_Volume_1h":0, "Total_Count_1h":0,"Hour":_hour,
			
			"Last_1h_Pct_Volume":0,
			"Last_1h_Pct_Count":0,
			"Last_Tps_1h":0,
			"Tps_1h":0,

			"Last_2h_Pct_Volume":0,
			"Last_2h_Pct_Count":0,
			"Last_Tps_2h":0,
			"Tps_2h":0,

			"Last_3h_Pct_Volume":0,
			"Last_3h_Pct_Count":0,
			"Last_Tps_3h":0,
			"Tps_3h":0,

			"Last_4h_Pct_Volume":0,
			"Last_4h_Pct_Count":0,
			"Last_Tps_4h":0,
			"Tps_4h":0,

			"Pct_Total_Volume_1h": 0,
			"Pct_Total_Count_1h": 0,

			"alerts_24h":0, 
			"alerts_1h":0,
			"Hour":_hour

		}

		Mongdb.mycol_24hrTicker.insert_one(New_ticker)


# Update every 24h
	if find_ticker != None and _hour == 2 and _minute == 0:
		print("24h", ticker, Event_time, Price_change, Price_change_percent, Weighted_average_price, Last_price, Open_price, High_price, Low_price, Volume, QuoteVolume, Count)
		Mongdb.mycol_24hrTicker.update_one({"ticker":ticker}, 
			{ "$set": 
				{
					"Event_time":Event_time, "Price_change_percent":Price_change_percent,
					"Volume":Volume, "QuoteVolume":QuoteVolume, "Count":Count, "Price_change_percent":Price_change_percent, "Last_price":Last_price,

					"Start_Volume_24h":Volume, "Start_Quote_Volume_24h":QuoteVolume, "Start_Count_24h":Count,
					"Last_Volume_24h":Volume, "Last_Quote_Volume_24h":QuoteVolume, "Last_Count_24h":Count,
					"Total_Volume_24h":0, "Total_Quote_Volume_24h":0, "Total_Count_24h":0,

					"Start_Volume_1h":Volume, "Start_Quote_Volume_1h":QuoteVolume, "Start_Count_1h":Count,
					"Last_Volume_1h":Volume, "Last_Quote_Volume_1h":QuoteVolume, "Last_Count_1h":Count,
					"Total_Volume_1h":0, "Total_Quote_Volume_1h":0, "Total_Count_1h":0,

					"alerts_24h":0, 
					"alerts_1h":0,"Hour":_hour

				}
			})
		

# Update every 1h
	if find_ticker["Hour"] != _hour:
		print("1h", ticker, Event_time, Price_change, Price_change_percent, Weighted_average_price, Last_price, Open_price, High_price, Low_price, Volume, QuoteVolume, Count)
		Mongdb.mycol_24hrTicker.update_one({"ticker":ticker}, 
		{ "$set": 
			{
				"Event_time":Event_time, "Price_change":Price_change, "Price_change_percent":Price_change_percent,
				"Volume":Volume, "QuoteVolume":QuoteVolume, "Count":Count, "Price_change_percent":Price_change_percent, "Last_price":Last_price,
				"Start_Volume_1h":Volume, "Start_Quote_Volume_1h":QuoteVolume, "Start_Count_1h":Count,
				"Last_Volume_1h":Volume, "Last_Quote_Volume_1h":QuoteVolume, "Last_Count_1h":Count,
				"Total_Volume_1h":0, "Total_Quote_Volume_1h":0, "Total_Count_1h":0,"alerts_1h":0, 

				"Pct_Total_Volume_1h": 0,
				"Pct_Total_Count_1h": 0,

				"alerts_1h":0,
				"Tps_1h":0,
				"Hour":_hour
			}
		})

# sand message and Update Volume, QuoteVolume, Count
	if find_ticker != None:
		Pct = ((Last_price *100) /  find_ticker['Last_price']) - 100
		Spread = ((Best_ask_price *100) /  Best_bid_price) - 100

		if (Pct > 0.4):
# 24h updata ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			New_Volume_24h = Volume - find_ticker['Last_Volume_24h']
			Total_Volume_24h = find_ticker['Total_Volume_24h'] + New_Volume_24h
			Pct_Total_Volume_24h = (Total_Volume_24h / find_ticker['Start_Volume_24h']) * 100
			pct_New_Volume_24h = (New_Volume_24h / Volume) * 100
			New_Quote_Volume_24h = QuoteVolume - find_ticker['Last_Quote_Volume_24h']
			Total_Quote_Volume_24h = find_ticker['Total_Quote_Volume_24h'] + New_Quote_Volume_24h
			Pct_Quote_Volume_24h = (Total_Quote_Volume_24h / find_ticker['Start_Quote_Volume_24h']) * 100
			pct_New_Quote_Volume_24h = (New_Quote_Volume_24h / QuoteVolume) * 100

			New_Count_24h = Count - find_ticker['Last_Count_24h']
			Total_Count_24h = find_ticker['Total_Count_24h'] + New_Count_24h
			Pct_Total_Count_24h = (Total_Count_24h / find_ticker['Start_Count_24h']) * 100
			pct_New_Count_24h = (New_Count_24h / Count) * 100

			alerts_24h = int(find_ticker['alerts_24h'] + 1)

# 1h updata ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			New_Volume_1h = Volume - find_ticker['Last_Volume_1h']
			Total_Volume_1h = find_ticker['Total_Volume_1h'] + New_Volume_1h
			Pct_Total_Volume_1h = (Total_Volume_1h / find_ticker['Start_Volume_1h']) * 100
			pct_New_Volume_1h = (New_Volume_1h / Volume) * 100
			
			New_Quote_1h = QuoteVolume - find_ticker['Last_Quote_Volume_1h']
			Total_Quote_Volume_1h = find_ticker['Total_Quote_Volume_1h'] + New_Quote_1h
			Pct_Total_Quote_Volume_1h = (Total_Quote_Volume_1h / find_ticker['Start_Quote_Volume_1h']) * 100
			pct_New_Quote_1h = (New_Quote_1h / QuoteVolume) * 100

			
			New_Count_1h = Count - find_ticker['Last_Count_1h']
			Total_Count_1h = find_ticker['Total_Count_1h'] + New_Count_1h
			Pct_Total_Count_1h = (Total_Count_1h / find_ticker['Start_Count_1h']) * 100
			pct_New_Count_1h = (New_Count_1h / Count) * 100

			alerts_1h = int(find_ticker['alerts_1h'] + 1)

			time_stamp,time_del, duration, time_weekly, minutes, par_second = Eq.Calc_time(find_ticker['Event_time'])
			Volume_K_M, Quote_K_M, Count_K_M, Up_down = Eq.K_M(New_Volume_1h, New_Quote_1h, New_Count_1h, Last_price, Weighted_average_price)
# Tps ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
			Tps = New_Count_1h / par_second
			Tps_1h = Total_Count_1h / _minute

			#print(f"Tps: {round(Tps, 3)} Tps_1h: {round(Tps_1h, 1)}  {ticker}")

			

# Update alerts, Volume, TPS, Alerts


if pct_New_Volume_1h > 0.5 and pct_New_Quote_1h > 0.5 and pct_New_Count_1h > 0.5:
    # تحديث البيانات في قاعدة البيانات
    Mongdb.mycol_24hrTicker.update_one({"ticker": ticker}, 
        { "$set": 
            {
                "Event_time": Event_time, "Price_change_percent": Price_change_percent, 
                "Volume": Volume, "QuoteVolume": QuoteVolume, "Count": Count, "Price_change_percent": Price_change_percent, "Last_price": Last_price,
                
                "Total_Volume_24h": Total_Volume_24h, "Total_Quote_Volume_24h": Total_Quote_Volume_24h, "Total_Count_24h": Total_Count_24h,
                "Last_Volume_24h": Volume, "Last_Quote_Volume24h": QuoteVolume, "Last_Count24h": Count,
                
                "Total_Volume_1h": Total_Volume_1h, "Total_Quote_Volume_1h": Total_Quote_Volume_1h, "Total_Count_1h": Total_Count_1h,
                "Last_Volume_1h": Volume, "Last_Quote_Volume_1h": QuoteVolume, "Last_Count_1h": Count,
                
                "Pct_Total_Volume_1h": Pct_Total_Volume_1h,
                "Pct_Total_Count_1h": Pct_Total_Count_1h,
                
                "alerts_24h": alerts_24h,
                "alerts_1h": alerts_1h,
                
                "Tps_1h": Tps_1h,
            }
        }) 
    
    # إرسال رسالة تلجرام عند تحقق الشروط (بدون علامة تدل على أقل من 60 ثانية)
    Tb.send_message_volume(
        f"{hash}{ticker} "+ 
        f"alerts 24h:[{alerts_24h}] 1h:[{alerts_1h}]\n"+
        f"Price:[{Last_price}] [{round(Pct, 2)}{pracant}] 🚀[{round(Price_change_percent,2)}{pracant}]\n"+
        f"Vol:🔥🔥 [{round(pct_New_Volume_1h, 1)}{pracant}] Qo: [{round(pct_New_Quote_1h, 1)}{pracant}] Co: [{round(pct_New_Count_1h, 1)}{pracant}]\n"+
        f"New VOL: [{round(pct_New_Volume_1h,1)}{pracant}] 1h: [{round(Pct_Total_Volume_1h)}{pracant}] 24h: :[{round(Pct_Total_Volume_24h)}{pracant}]\n"+
        f"Count  :[{Count_K_M}] Last:[{round(find_ticker['Pct_Total_Count_1h'],2)}{pracant}] 🌷[{round(Pct_Total_Count_1h,2)}{pracant}]\n"+
        f"Volume :[{Volume_K_M}] [${Quote_K_M}]\n"+
        f"Spread:[{round(Spread, 2)}{pracant}]\n"+
        f"MYH:🔥[{round(Tps, 2)}{pracant}]\n"+
        f"MYH 1h:[{round(Tps_1h, 2)}{pracant}]"
    )

    # إرسال رسالة تلجرام عند تحقق الشروط خلال أقل من 60 ثانية
    if par_second < 60:
        date_time, time_stamp , _year, _month, _day, _hour, _minute, _secand = Eq.time_date()
        print("Websocket", f"{ticker} Vol: [{round(pct_New_Volume_1h, 1)}%] Qo: [{round(pct_New_Quote_1h, 1)}%] Co: [{round(pct_New_Count_1h, 1)}%] time: {duration}")		
        Tb.send_message_volume(
            f"{hash}{ticker} ⏰`[{duration}]` "+ 
            f"alerts 24h:`[{alerts_24h}]` 1h:`[{alerts_1h}]`\n"+
            f"Price:`[{Last_price}]` `[{round(Pct, 2)}{pracant}]` 🚀`[{round(Price_change_percent,2)}{pracant}]`\n"+
            f"Vol:🔥🔥 `[{round(pct_New_Volume_1h, 1)}{pracant}]` Qo: `[{round(pct_New_Quote_1h, 1)}{pracant}]` Co: `[{round(pct_New_Count_1h, 1)}{pracant}]`\n"+
            f"New VOL: `[{round(pct_New_Volume_1h,1)}{pracant}]` 1h: `[{round(Pct_Total_Volume_1h)}{pracant}]` 24h: :`[{round(Pct_Total_Volume_24h)}{pracant}]`\n"+
            f"Count  :`[{Count_K_M}]` Last:`[{round(find_ticker['Pct_Total_Count_1h'],2)}{pracant}]` 🌷`[{round(Pct_Total_Count_1h,2)}{pracant}]`\n"+
            f"Volume :`[{Volume_K_M}]` `[${Quote_K_M}]`\n"+
            f"Spread:`[{round(Spread, 2)}{pracant}]`\n"+
            f"MYH:🔥`[{round(Tps, 2)}{pracant}]`\n"+
            f"MYH 1h:`[{round(Tps_1h, 2)}{pracant}]`\n"+
            f"⏰ @mohammedalgorafi @mohammedalgorafi @mohammedalgotafi"
        )


					