
import threading
import json
import Eqution as Eq
import Telegram as Tb
from os import system
system("clear")

volume_data = {}

# تحميل البيانات المخزنة إذا كانت موجودة
try:
    with open("volume_data.json", "r") as file:
        volume_data = json.load(file)
except FileNotFoundError:
    print("No previous volume data found. Starting fresh.")


def save_volume_data():
    """حفظ بيانات الفوليوم في ملف JSON"""
    print("l  you")
    with open("volume_data.json", "w") as file:
        json.dump(volume_data, file)


def volume_24(ticker, Event_time, Price_change, Price_change_percent, Weighted_average_price,
    Last2_price, Open_price, High_price, Low_price, Volume1, QuoteVolume1, Count1,
    Last_quantity, Best_bid_price, Best_bid_quantity, Best_ask_price, Best_ask_quantity,
    date_time, t_stamp , _year, _month, _day, _hour, _minute, _secand
):
    global volume_data
    updated = False
    if ticker not in volume_data:
        volume_data[ticker] = {
            "Price_change_percent": Price_change_percent, "Last_price": Last2_price, "Event_time11": Event_time,
                    
            "Volume": Volume1, "QuoteVolume": QuoteVolume1, "Count": Count1,
                    
            "Start_Volume_24h": Volume1,"Start_Quote_Volume_24h": QuoteVolume1, "Start_Count_24h": Count1, "Start_Pct_24h": Price_change_percent,
            "Last_Volume_24h": Volume1, "Last_Quote_Volume_24h": QuoteVolume1, "Last_Count_24h": Count1,
            "Total_Volume_24h": 0, "Total_Quote_Volume_24h": 0, "Total_Count_24h": 0,
                    
            "Start_Volume_1h": Volume1, "Start_Quote_Volume_1h": QuoteVolume1, "Start_Count_1h": Count1, "Start_Pct_1h": Price_change_percent,
            "Last_Volume_1h": Volume1, "Last_Quote_Volume_1h": QuoteVolume1, "Last_Count_1h": Count1,
            "Total_Volume_1h": 0, "Total_Quote_Volume_1h": 0, "Total_Count_1h": 0,
            
            "Start_Volume_24h_S": Volume1,"Start_Quote_Volume_24h_S": QuoteVolume1, "Start_Count_24h_S": Count1, "Start_Pct_24h_S": Price_change_percent,
            "Last_Volume_24h_S": Volume1, "Last_Quote_Volume_24h_S": QuoteVolume1, "Last_Count_24h_S": Count1,
            "Total_Volume_24h_S": 0, "Total_Quote_Volume_24h_S": 0, "Total_Count_24h_S": 0,

            "Start_Volume_1h_S": Volume1, "Start_Quote_Volume_1h_S": QuoteVolume1, "Start_Count_1h_S": Count1, "Start_Pct_1h_S": Price_change_percent,
            "Last_Volume_1h_S": Volume1, "Last_Quote_Volume_1h_S": QuoteVolume1, "Last_Count_1h_S": Count1,
            "Total_Volume_1h_S": 0, "Total_Quote_Volume_1h_S": 0, "Total_Count_1h_S": 0,
  
            "Last_1h_Pct_Volume": 0,
            "Last_1h_Pct_Volume_S": 0,
            "Last_1h_Pct_Count": 0,
            "Last_1h_Pct_Count_S": 0,
            "Last_Tps_1h": 0,
            "Last_Tps_1h_S": 0,
            "Tps_1h": 0,
            "Tps_1h_S": 0,
                    
            "Last_2h_Pct_Volume": 0,
            "Last_2h_Pct_Count": 0,
            "Last_Tps_2h": 0,
            "Tps_2h": 0,
                    
            "Last_3h_Pct_Volume": 0,
            "Last_3h_Pct_Count": 0,
            "Last_Tps_3h": 0,
            "Tps_3h": 0,
                    
            "Last_4h_Pct_Volume": 0,
            "Last_4h_Pct_Count": 0,
            "Last_Tps_4h": 0,
            "Tps_4h": 0,
                    
             "Pct_Total_Volume_1h": 0,
             "Pct_Total_Volume_1h_S": 0,
             "Pct_Total_Count_1h": 0,
             "Pct_Total_Count_1h_S": 0,
                    
            "alerts_24h": 0,
            "alerts_24h_S": 0,
            "alerts_1h": 0,
            "alerts_1h_S": 0,
            "Hour":_hour
        }
        updated = True

    if "Start_Count_24h_S" not in volume_data[ticker]:
        volume_data[ticker]["Start_Volume_1h_S"] = Volume1
        volume_data[ticker]["Start_Quote_Volume_1h_S"] = QuoteVolume1
        volume_data[ticker]["Start_Count_1h_S"] = Count1
        volume_data[ticker]["Start_Pct_1h_S"] = Price_change_percent
        volume_data[ticker]["Last_Volume_1h_S"] = Volume1
        volume_data[ticker]["Last_Quote_Volume_1h_S"] = QuoteVolume1
        volume_data[ticker]["Last_Count_1h_S"] = Count1
        volume_data[ticker]["Total_Volume_1h_S"] = 0
        volume_data[ticker]["Total_Quote_Volume_1h_S"] = 0
        volume_data[ticker]["Total_Count_1h_S"] = 0
        volume_data[ticker]["Start_Volume_24h_S"] = Volume1
        volume_data[ticker]["Start_Quote_Volume_24h_S"] = QuoteVolume1
        volume_data[ticker]["Start_Count_24h_S"] = Count1
        volume_data[ticker]["Start_Pct_24h_S"] = Price_change_percent
        volume_data[ticker]["Last_Volume_24h_S"] = Volume1
        volume_data[ticker]["Last_Quote_Volume_24h_S"] = QuoteVolume1
        volume_data[ticker]["Last_Count_24h_S"] = Count1
        volume_data[ticker]["Total_Volume_24h_S"] = 0
        volume_data[ticker]["Total_Quote_Volume_24h_S"] = 0
        volume_data[ticker]["Total_Count_24h_S"] = 0
        volume_data[ticker]["Last_1h_Pct_Volume_S"] = 0
        volume_data[ticker]["Last_1h_Pct_Count_S"] = 0
        volume_data[ticker]["Last_Tps_1h_S"] = 0
        volume_data[ticker]["Tps_1h_S"] = 0
        volume_data[ticker]["Pct_Total_Volume_1h_S"] = 0
        volume_data[ticker]["Pct_Total_Count_1h_S"] = 0
        volume_data[ticker]["alerts_24h_S"] = 0
        volume_data[ticker]["alerts_1h_S"] = 0
        updated = True

    if _hour == 2 and _minute == 0:
        volume_data[ticker]["Event_time11"] = Event_time
        volume_data[ticker]["Volume"] = Volume1
        volume_data[ticker]["QuoteVolume"] = QuoteVolume1
        volume_data[ticker]["Count"] = Count1
        volume_data[ticker]["Price_change_percent"] = Price_change_percent
        volume_data[ticker]["Last_price"] = Last2_price
        volume_data[ticker]["Start_Volume_24h"] = Volume1
        volume_data[ticker]["Start_Quote_Volume_24h"] = QuoteVolume1
        volume_data[ticker]["Start_Count_24h"] = Count1
        volume_data[ticker]["Last_Volume_24h"] = Volume1
        volume_data[ticker]["Last_Quote_Volume_24h"] = QuoteVolume1
        volume_data[ticker]["Last_Count_24h"] = Count1
        volume_data[ticker]["Total_Volume_24h"] = 0
        volume_data[ticker]["Total_Quote_Volume_24h"] = 0
        volume_data[ticker]["Total_Count_24h"] = 0
        volume_data[ticker]["Start_Volume_1h"] = Volume1
        volume_data[ticker]["Start_Quote_Volume_1h"] = QuoteVolume1
        volume_data[ticker]["Start_Count_1h"] = Count1
        volume_data[ticker]["Last_Volume_1h"] = Volume1
        volume_data[ticker]["Last_Quote_Volume_1h"] = QuoteVolume1
        volume_data[ticker]["Last_Count_1h"] = Count1
        volume_data[ticker]["Total_Volume_1h"] = 0
        volume_data[ticker]["Total_Quote_Volume_1h"] = 0
        volume_data[ticker]["Total_Count_1h"] = 0
        volume_data[ticker]["alerts_1h"] = 0
        volume_data[ticker]["alerts_24h"] = 0
        volume_data[ticker]["Start_Volume_24h_S"] = Volume1
        volume_data[ticker]["Start_Quote_Volume_24h_S"] = QuoteVolume1
        volume_data[ticker]["Start_Count_24h_S"] = Count1
        volume_data[ticker]["Last_Volume_24h_S"] = Volume1
        volume_data[ticker]["Last_Quote_Volume_24h_S"] = QuoteVolume1
        volume_data[ticker]["Last_Count_24h_S"] = Count1
        volume_data[ticker]["Total_Volume_24h_S"] = 0
        volume_data[ticker]["Total_Quote_Volume_24h_S"] = 0
        volume_data[ticker]["Total_Count_24h_S"] = 0
        volume_data[ticker]["Start_Volume_1h_S"] = Volume1
        volume_data[ticker]["Start_Quote_Volume_1h_S"] = QuoteVolume1
        volume_data[ticker]["Start_Count_1h_S"] = Count1
        volume_data[ticker]["Last_Volume_1h_S"] = Volume1
        volume_data[ticker]["Last_Quote_Volume_1h_S"] = QuoteVolume1
        volume_data[ticker]["Last_Count_1h_S"] = Count1
        volume_data[ticker]["Total_Volume_1h_S"] = 0
        volume_data[ticker]["Total_Quote_Volume_1h_S"] = 0
        volume_data[ticker]["Total_Count_1h_S"] = 0
        volume_data[ticker]["alerts_1h_S"] = 0
        volume_data[ticker]["alerts_24h_S"] = 0
        volume_data[ticker]["Hour"] = _hour
        updated = True

    if volume_data[ticker]["Hour"] != _hour:
        volume_data[ticker]["Event_time11"] = Event_time
        volume_data[ticker]["Price_change"] = Price_change
        volume_data[ticker]["Volume"] = Volume1
        volume_data[ticker]["QuoteVolume"] = QuoteVolume1
        volume_data[ticker]["Count"] = Count1
        volume_data[ticker]["Price_change_percent"] = Price_change_percent
        volume_data[ticker]["Last_price"] = Last2_price
        volume_data[ticker]["Start_Volume_1h"] = Volume1
        volume_data[ticker]["Start_Quote_Volume_1h"] = QuoteVolume1
        volume_data[ticker]["Start_Count_1h"] = Count1
        volume_data[ticker]["Last_Volume_1h"] = Volume1
        volume_data[ticker]["Last_Quote_Volume_1h"] = QuoteVolume1
        volume_data[ticker]["Last_Count_1h"] = Count1
        volume_data[ticker]["Total_Volume_1h"] = 0
        volume_data[ticker]["Total_Quote_Volume_1h"] = 0
        volume_data[ticker]["Total_Count_1h"] = 0
        volume_data[ticker]["alerts_1h"] = 0
        volume_data[ticker]["Pct_Total_Volume_1h"] = 0
        volume_data[ticker]["Pct_Total_Count_1h"] = 0
        volume_data[ticker]["Start_Volume_1h_S"] = Volume1
        volume_data[ticker]["Start_Quote_Volume_1h_S"] = QuoteVolume1
        volume_data[ticker]["Start_Count_1h_S"] = Count1
        volume_data[ticker]["Last_Volume_1h_S"] = Volume1
        volume_data[ticker]["Last_Quote_Volume_1h_S"] = QuoteVolume1
        volume_data[ticker]["Last_Count_1h_S"] = Count1
        volume_data[ticker]["Total_Volume_1h_S"] = 0
        volume_data[ticker]["Total_Quote_Volume_1h_S"] = 0
        volume_data[ticker]["Total_Count_1h_S"] = 0
        volume_data[ticker]["alerts_1h_S"] = 0
        volume_data[ticker]["Pct_Total_Volume_1h_S"] = 0
        volume_data[ticker]["Pct_Total_Count_1h_S"] = 0
        volume_data[ticker]["Hour"] = _hour
        updated = True

    if ticker in volume_data:
        Pct = ((Last2_price *100) /  volume_data[ticker]["Last_price"] - 100)
        Spread = ((Best_ask_price *100) /  Best_bid_price) - 100
        #print(Pct)
        if Pct > 0.4:
            New_Volume_24h = Volume1 - volume_data[ticker]["Last_Volume_24h"]
            Total_Volume_24h = volume_data[ticker]["Total_Volume_24h"] + New_Volume_24h
            Pct_Total_Volume_24h = (Total_Volume_24h / volume_data[ticker]["Start_Volume_24h"]) * 100
            pct_New_Volume_24h = (New_Volume_24h / Volume1) * 100
            New_Quote_Volume_24h = QuoteVolume1 - volume_data[ticker]["Last_Quote_Volume_24h"]
            Total_Quote_Volume_24h = volume_data[ticker]["Total_Quote_Volume_24h"] + New_Quote_Volume_24h
            Pct_Quote_Volume_24h = (Total_Quote_Volume_24h / volume_data[ticker]["Start_Quote_Volume_24h"]) * 100
            pct_New_Quote_Volume_24h = (New_Quote_Volume_24h / QuoteVolume1) * 100
            New_Count_24h = Count1 - volume_data[ticker]["Last_Count_24h"]
            Total_Count_24h = volume_data[ticker]["Total_Count_24h"] + New_Count_24h
            Pct_Total_Count_24h = (Total_Count_24h / volume_data[ticker]["Start_Count_24h"]) * 100
            pct_New_Count_24h = (New_Count_24h / Count1) * 100
            alerts_24h = int(volume_data[ticker]["alerts_24h"] + 1)
            New_Volume_1h = Volume1 - volume_data[ticker]["Last_Volume_1h"]
            Total_Volume_1h = volume_data[ticker]["Total_Volume_1h"] + New_Volume_1h
            print(f"Total_olume_1h :")
            Pct_Total_Volume_1h = (Total_Volume_1h / volume_data[ticker]["Start_Volume_1h"]) * 100
            pct_New_Volume_1h = (New_Volume_1h / Volume1) * 100
            New_Quote_1h = QuoteVolume1 - volume_data[ticker]["Last_Quote_Volume_1h"]
            Total_Quote_Volume_1h = volume_data[ticker]["Total_Quote_Volume_1h"] + New_Quote_1h
            Pct_Total_Quote_Volume_1h = (Total_Quote_Volume_1h / volume_data[ticker]["Start_Quote_Volume_1h"]) * 100
            pct_New_Quote_1h = (New_Quote_1h / QuoteVolume1) * 100
            print(f"NewQuote1h : {pct_New_Quote_1h}")
            New_Count_1h = Count1 - volume_data[ticker]["Last_Count_1h"]
            Total_Count_1h = volume_data[ticker]["Total_Count_1h"] + New_Count_1h
            Pct_Total_Count_1h = (Total_Count_1h / volume_data[ticker]["Start_Count_1h"]) * 100
            pct_New_Count_1h = (New_Count_1h / Count1) * 100
            alerts_1h = int(volume_data[ticker]["alerts_1h"] + 1)
            time_stamp, time_del, duration, time_weekly, minutes, par_second = Eq.Calc_time(volume_data[ticker]["Event_time11"], Event_time)
            Volume_K_M, Quote_K_M, Count_K_M, Total_Quote_Volume_1h_K_M, Total_Quote_Volume_24h_K_M = Eq.K_M(New_Volume_1h, New_Quote_1h, New_Count_1h, Total_Quote_Volume_1h, Total_Quote_Volume_24h)
            Tps = New_Count_1h / par_second
            Tps_1h = Total_Count_1h / _minute
            if Pct > 1.0 and pct_New_Volume_1h > 1.0 and pct_New_Quote_1h > 1.0 and pct_New_Count_1h > 1.0 and par_second < 90:
                Tb.send_message_volume(
                    f"┌ **Pumping:** `{ticker}` | {round(Pct, 2)}% | {round(Price_change_percent, 2)}%\n"
                    f"├ **Price:** `{Last2_price}`\n"
                    f"├ [1h Vol](http://t.me/jj) : {Total_Quote_Volume_1h_K_M} | {round(Pct_Total_Quote_Volume_1h, 2)}%\n"
                    f"├ **Net Vol:** {Quote_K_M} | {round(pct_New_Volume_1h, 2)}%\n"
                    f"┊ └ **in** :  {time_del}\n"
                    f"┊ └ **v** : {round(pct_New_Volume_1h, 2)}% | Q : {round(pct_New_Quote_1h, 2)}% | C: {round(pct_New_Count_1h, 2)}%\n"
                    f"┊ └ Tps : {round(Tps, 2)}% | 1h : {round(Tps_1h, 2)}%\n"
                    f"├ [24 Vol](http://t.me/jj) : {Total_Quote_Volume_24h_K_M} | **change:** {round(Pct_Quote_Volume_24h, 2)}%\n"
                    f"└ Alerts : ⏰ {alerts_24h} | **1h:**  {alerts_1h} | {round(Pct_Total_Quote_Volume_1h, 1)}% 📈\n"
                    f"\n"
                    f"🧑‍💻 Dev: @mohammedalgorafi"
                )
                volume_data[ticker]["Event_time11"] = Event_time
                volume_data[ticker]["Volume"] = Volume1
                volume_data[ticker]["QuoteVolume"] = QuoteVolume1
                volume_data[ticker]["Count"] = Count1
                volume_data[ticker]["Last_price"] = Last2_price
                volume_data[ticker]["Price_change_percent"] = Price_change_percent
                volume_data[ticker]["Total_Volume_24h"] = Total_Volume_24h
                volume_data[ticker]["Total_Quote_Volume_24h"] = Total_Quote_Volume_24h
                volume_data[ticker]["Total_Count_24h"] = Total_Count_24h
                volume_data[ticker]["Last_Volume_24h"] = Volume1
                volume_data[ticker]["Last_Quote_Volume_24h"] = QuoteVolume1
                volume_data[ticker]["Last_Count_24h"] = Last2_price
                volume_data[ticker]["Total_Volume_1h"] = Total_Volume_1h
                volume_data[ticker]["Total_Quote_Volume_1h"] = Total_Quote_Volume_1h
                volume_data[ticker]["Total_Count_1h"] = Total_Count_1h
                volume_data[ticker]["Last_Volume_1h"] = Volume1
                volume_data[ticker]["Last_Quote_Volume_1h"] = QuoteVolume1
                volume_data[ticker]["Last_Count_1h"] = Count1
                volume_data[ticker]["Pct_Total_Volume_1h"] = Pct_Total_Volume_1h
                volume_data[ticker]["Pct_Total_Count_1h"] = Pct_Total_Count_1h
                volume_data[ticker]["alerts_24h"] = alerts_24h
                volume_data[ticker]["alerts_1h"] = alerts_1h
                updated = True
            if pct_New_Volume_1h > 0.5 and pct_New_Quote_1h > 0.5 and pct_New_Count_1h > 0.5:
                message_type = "🔥" if par_second < 60 else "🟢"
                if par_second < 60:
                    message_type = f"🔥 `{ticker}` 🔥"
                    volume_display = f"{Quote_K_M} 🔥"
                else:
                    message_type = f"🟢 `{ticker}`"
                    volume_display = f"{Quote_K_M}"
                Tb.send_message_volume(
                    f"┌ **scalping:** {message_type} | {round(Pct, 2)}% | {round(Price_change_percent, 2)}%\n"
                    f"├ **Price:** `{Last2_price}`\n"
                    f"├ [1h Vol](http://t.me/jj) : {Total_Quote_Volume_1h_K_M} | {round(Pct_Total_Quote_Volume_1h, 2)}%\n"
                    f"├ **Net Vol:** {volume_display} | {round(pct_New_Volume_1h, 2)}%\n"
                    f"┊ └ **in** :  {time_del}\n"
                    f"┊ └ **v** : {round(pct_New_Volume_1h, 2)}% | Q : {round(pct_New_Quote_1h, 2)}% | C: {round(pct_New_Count_1h, 2)}%\n"
                    f"┊ └ Tps : {round(Tps, 2)}% | 1h : {round(Tps_1h, 2)}%\n"
                    f"├ [24 Vol](http://t.me/jj) : {Total_Quote_Volume_24h_K_M} | **change:** {round(Pct_Quote_Volume_24h, 2)}%\n"
                    f"└ Alerts : ⏰ {alerts_24h} | **1h:**  {alerts_1h} | {round(Pct_Total_Quote_Volume_1h, 1)}% 📈\n"
                    f"\n"
                    f"🧑‍💻 Dev: @mohammedalgorafi"
                )
                volume_data[ticker]["Event_time11"] = Event_time
                volume_data[ticker]["Volume"] = Volume1
                volume_data[ticker]["QuoteVolume"] = QuoteVolume1
                volume_data[ticker]["Count"] = Count1
                volume_data[ticker]["Last_price"] = Last2_price
                volume_data[ticker]["Price_change_percent"] = Price_change_percent
                volume_data[ticker]["Total_Volume_24h"] = Total_Volume_24h
                volume_data[ticker]["Total_Quote_Volume_24h"] = Total_Quote_Volume_24h
                volume_data[ticker]["Total_Count_24h"] = Total_Count_24h
                volume_data[ticker]["Last_Volume_24h"] = Volume1
                volume_data[ticker]["Last_Quote_Volume_24h"] = QuoteVolume1
                volume_data[ticker]["Last_Count_24h"] = Last2_price
                volume_data[ticker]["Total_Volume_1h"] = Total_Volume_1h
                volume_data[ticker]["Total_Quote_Volume_1h"] = Total_Quote_Volume_1h
                volume_data[ticker]["Total_Count_1h"] = Total_Count_1h
                volume_data[ticker]["Last_Volume_1h"] = Volume1
                volume_data[ticker]["Last_Quote_Volume_1h"] = QuoteVolume1
                volume_data[ticker]["Last_Count_1h"] = Count1
                volume_data[ticker]["Pct_Total_Volume_1h"] = Pct_Total_Volume_1h
                volume_data[ticker]["Pct_Total_Count_1h"] = Pct_Total_Count_1h
                volume_data[ticker]["alerts_24h"] = alerts_24h
                volume_data[ticker]["alerts_1h"] = alerts_1h
                updated = True
        else:
            if Pct < -(0.4):
                print("ooiiiioooooo")
                New_Volume_24h_S = Volume1 - volume_data[ticker]["Last_Volume_24h_S"]
                Total_Volume_24h_S = volume_data[ticker]["Total_Volume_24h_S"] + New_Volume_24h_S
                Pct_Total_Volume_24h_S = (Total_Volume_24h_S / volume_data[ticker]["Start_Volume_24h_S"]) * 100
                pct_New_Volume_24h_S = (New_Volume_24h_S / Volume1) * 100
                New_Quote_Volume_24h_S = QuoteVolume1 - volume_data[ticker]["Last_Quote_Volume_24h_S"]
                Total_Quote_Volume_24h_S = volume_data[ticker]["Total_Quote_Volume_24h_S"] + New_Quote_Volume_24h_S
                Pct_Quote_Volume_24h_S = (Total_Quote_Volume_24h_S / volume_data[ticker]["Start_Quote_Volume_24h_S"]) * 100
                pct_New_Quote_Volume_24h_S = (New_Quote_Volume_24h_S / QuoteVolume1) * 100
                New_Count_24h_S = Count1 - volume_data[ticker]["Last_Count_24h_S"]
                Total_Count_24h_S = volume_data[ticker]["Total_Count_24h_S"] + New_Count_24h_S
                Pct_Total_Count_24h_S = (Total_Count_24h_S / volume_data[ticker]["Start_Count_24h_S"]) * 100
                pct_New_Count_24h_S = (New_Count_24h_S / Count1) * 100
                alerts_24h_S = int(volume_data[ticker]["alerts_24h_S"] + 1)
                New_Volume_1h_S = Volume1 - volume_data[ticker]["Last_Volume_1h_S"]
                Total_Volume_1h_S = volume_data[ticker]["Total_Volume_1h_S"] + New_Volume_1h_S
                Pct_Total_Volume_1h_S = (Total_Volume_1h_S / volume_data[ticker]["Start_Volume_1h_S"]) * 100
                pct_New_Volume_1h_S = (New_Volume_1h_S / Volume1) * 100
                New_Quote_1h_S = QuoteVolume1 - volume_data[ticker]["Last_Quote_Volume_1h_S"]
                Total_Quote_Volume_1h_S = volume_data[ticker]["Total_Quote_Volume_1h_S"] + New_Quote_1h_S
                Pct_Total_Quote_Volume_1h_S = (Total_Quote_Volume_1h_S / volume_data[ticker]["Start_Quote_Volume_1h_S"]) * 100
                pct_New_Quote_1h_S = (New_Quote_1h_S / QuoteVolume1) * 100
                New_Count_1h_S = Count1 - volume_data[ticker]["Last_Count_1h_S"]
                Total_Count_1h_S = volume_data[ticker]["Total_Count_1h_S"] + New_Count_1h_S
                Pct_Total_Count_1h_S = (Total_Count_1h_S / volume_data[ticker]["Start_Count_1h_S"]) * 100
                pct_New_Count_1h_S = (New_Count_1h_S / Count1) * 100
                alerts_1h_S = int(volume_data[ticker]["alerts_1h_S"] + 1)
                time_stamp, time_del, duration, time_weekly, minutes, par_second = Eq.Calc_time(volume_data[ticker]["Event_time11"], Event_time)
                Volume_K_M_S, Quote_K_M_S, Count_K_M_S, Total_Quote_Volume_1h_K_M_S, Total_Quote_Volume_24h_K_M_S = Eq.K_M(New_Volume_1h_S, New_Quote_1h_S, New_Count_1h_S, Total_Quote_Volume_1h_S, Total_Quote_Volume_24h_S)
                Tps_S = New_Count_1h_S / par_second
                Tps_1h_S = Total_Count_1h_S / _minute
                if pct_New_Volume_1h_S > 0.5 and pct_New_Quote_1h_S > 0.5 and pct_New_Count_1h_S > 0.5:
                    message_type = "🔥" if par_second < 60 else "🔴"
                    print("hlwlekdj")
                    if par_second < 60:
                        message_type = f"🔴 `{ticker}` 🔥"
                        volume_display = f"{Quote_K_M_S} 🔥"
                    else:
                        message_type = f"🔴 `{ticker}`"
                        volume_display = f"{Quote_K_M_S}"
                    Tb.send_message_down(
                        f"┌ **scalping:** {message_type} | {round(Pct, 2)}% | {round(Price_change_percent, 2)}%\n"
                        f"├ **Price:** `{Last2_price}`\n"
                        f"├ [1h Vol](http://t.me/jj) : {Total_Quote_Volume_1h_K_M_S} | {round(Pct_Total_Quote_Volume_1h_S, 2)}%\n"
                        f"├ **Net Vol:** {volume_display} | {round(pct_New_Volume_1h_S, 2)}%\n"
                        f"┊ └ **in** :  {time_del}\n"
                        f"┊ └ **v** : {round(pct_New_Volume_1h_S, 2)}% | Q : {round(pct_New_Quote_1h_S, 2)}% | C: {round(pct_New_Count_1h_S, 2)}%\n"
                        f"┊ └ Tps : {round(Tps_S, 2)}% | 1h : {round(Tps_1h_S, 2)}%\n"
                        f"├ [24 Vol](http://t.me/jj) : {Total_Quote_Volume_24h_K_M_S} | **change:** {round(Pct_Quote_Volume_24h_S, 2)}%\n"
                        f"└ Alerts : ⏰ {alerts_24h_S} | **1h:**  {alerts_1h_S} | {round(Pct_Total_Quote_Volume_1h_S, 1)}% 📈\n"
                        f"\n"
                        f"🧑‍💻 Dev: @mohammedalgorafi"
                    )
                    volume_data[ticker]["Event_time11"] = Event_time
                    volume_data[ticker]["Volume"] = Volume1
                    volume_data[ticker]["QuoteVolume"] = QuoteVolume1
                    volume_data[ticker]["Count"] = Count1
                    volume_data[ticker]["Last_price"] = Last2_price
                    volume_data[ticker]["Price_change_percent"] = Price_change_percent
                    volume_data[ticker]["Total_Volume_24h_S"] = Total_Volume_24h_S
                    volume_data[ticker]["Total_Quote_Volume_24h_S"] = Total_Quote_Volume_24h_S
                    volume_data[ticker]["Total_Count_24h_S"] = Total_Count_24h_S
                    volume_data[ticker]["Last_Volume_24h_S"] = Volume1
                    volume_data[ticker]["Last_Quote_Volume_24h_S"] = QuoteVolume1
                    volume_data[ticker]["Last_Count_24h_S"] = Last2_price
                    volume_data[ticker]["Total_Volume_1h_S"] = Total_Volume_1h_S
                    volume_data[ticker]["Total_Quote_Volume_1h_S"] = Total_Quote_Volume_1h_S
                    volume_data[ticker]["Total_Count_1h_S"] = Total_Count_1h_S
                    volume_data[ticker]["Last_Volume_1h_S"] = Volume1
                    volume_data[ticker]["Last_Quote_Volume_1h_S"] = QuoteVolume1
                    volume_data[ticker]["Last_Count_1h_S"] = Count1
                    volume_data[ticker]["Pct_Total_Volume_1h_S"] = Pct_Total_Volume_1h_S
                    volume_data[ticker]["Pct_Total_Count_1h_S"] = Pct_Total_Count_1h_S
                    volume_data[ticker]["alerts_24h_S"] = alerts_24h_S
                    volume_data[ticker]["alerts_1h_S"] = alerts_1h_S
                    print(f"Hour: {_hour}")
                    updated = True

    if updated:
        save_volume_data()
