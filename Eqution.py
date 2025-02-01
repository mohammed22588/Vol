from datetime import datetime as dt
import datetime

def time_date():
    """
    دالة لإرجاع الوقت الحالي والتوقيت الزمني.
    """
    date_time = datetime.datetime.now()
    t_stamp = dt.timestamp(date_time)
    _hour = date_time.hour
    _minute = date_time.minute
    _secand = date_time.second
    _day = date_time.day
    _month = date_time.month
    _year = date_time.year
    return date_time, t_stamp , _year, _month, _day, _hour, _minute, _secand

def Calc_time(event_time_last, event_time2):
    last_time = dt.utcfromtimestamp(event_time_last / 1000)  # تحويل من ميلي ثانية إلى ثانية
    b = last_time.strftime('%Y-%m-%d %H:%M:%S')
    now_time = dt.utcfromtimestamp(event_time2 / 1000)  # تحويل من ميلي ثانية إلى ثانية
    time_stamp = now_time.strftime('%Y-%m-%d %H:%M:%S')
    time_difference = now_time - last_time
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    total_minutes = days * 24 * 60 + hours * 60 + minutes
    total_weeks = days // 7
    total_seconds = time_difference.total_seconds()

    # إعداد قيمة difference_details بناءً على الشروط
    if hours == 0 and minutes == 0:
        difference_details = f"{seconds} s"
    elif hours == 0:
        difference_details = f"{minutes} m and {seconds} s"
    else:
        difference_details = f"{hours} h and {minutes} m and  {seconds} s"

    return time_stamp, difference_details, total_seconds, total_weeks , total_minutes, total_seconds

def K_M(New_Volume_1h, New_Quote_1h, New_Count_1h, Total_Quote_Volume_1h, Total_Quote_Volume_24h):
        Volume_K_M = f"{New_Volume_1h/1000:.2f}K" if New_Volume_1h < 1_000_000 else f"{New_Volume_1h/1_000_000:.2f}M"
        Quote_K_M = f"{New_Quote_1h/1000:.2f}K" if New_Quote_1h < 1_000_000 else f"{New_Quote_1h/1_000_000:.2f}M"
        Count_K_M = f"{New_Count_1h/1000:.2f}K" if New_Count_1h < 1_000_000 else f"{New_Count_1h/1_000_000:.2f}M"
        Total_Quote_Volume_1h_K_M = f"{Total_Quote_Volume_1h/1000:.2f}K" if Total_Quote_Volume_1h < 1_000_000 else f"{Total_Quote_Volume_1h/1_000_000:.2f}M"
        Total_Quote_Volume_24h_K_M = f"{Total_Quote_Volume_24h/1000:.2f}K" if Total_Quote_Volume_24h < 1_000_000 else f"{Total_Quote_Volume_24h/1_000_000:.2f}M"
        return Volume_K_M, Quote_K_M, Count_K_M, Total_Quote_Volume_1h_K_M, Total_Quote_Volume_24h_K_M
 