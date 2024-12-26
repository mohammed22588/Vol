from datetime import datetime as dt
import datetime
from datetime import datetime

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


def Calc_time(stored_event_time):
    """
    حساب الفروقات الزمنية بناءً على الوقت المخزن (stored_event_time) في MongoDB.
    """
    try:
        # التحقق من أن stored_event_time ليس فارغًا أو غير معرف
        if stored_event_time is None:
            print("No stored event time found, skipping the time calculation step.")
            return None, None, None, None, None, None

        # تحويل الطابع الزمني إلى datetime
        stored_time = datetime.fromtimestamp(stored_event_time / 1000)  # الوقت المخزن
        current_time = datetime.now()  # وقت الجهاز الحالي

        # حساب الفرق بين الوقت المخزن ووقت الجهاز الحالي
        time_difference = current_time - stored_time

        # استخراج تفاصيل الفرق الزمني
        days = time_difference.days
        total_seconds = time_difference.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)

        # نص وصفي للمدة الزمنية
        duration = f"{days}d {hours}h {minutes}m {seconds}s" if days > 0 else f"{hours}h {minutes}m {seconds}s"

        # اليوم في الأسبوع
        time_weekly = stored_time.weekday()

        # إرجاع القيم المطلوبة
        return stored_event_time, time_difference, duration, time_weekly, minutes, seconds

    except Exception as e:
        print(f"Error occurred in Calc_time: {e}")
        # إذا حدث خطأ، يمكن ببساطة تجاوز أو إرجاع قيمة افتراضية
        return None, None, None, None, None, None


def K_M(New_Volume_1h, New_Quote_1h, New_Count_1h, Last_price, Weighted_average_price):
    """
    إجراء حسابات على حجم التداول، القيمة السوقية، وعدد العمليات خلال الساعة، 
    مع تحديد اتجاه السعر (Up/Down).
    """
    try:
        # التحقق من وجود البيانات
        if New_Volume_1h is None or New_Quote_1h is None or New_Count_1h is None:
            print("Incomplete data, skipping the K_M calculation.")
            return None, None, None, None

        # حسابات مهيئة للحجم والقيمة وعدد العمليات (تحويل إلى ألف أو مليون)
        Volume_K_M = f"{New_Volume_1h/1000:.2f}K" if New_Volume_1h < 1_000_000 else f"{New_Volume_1h/1_000_000:.2f}M"
        Quote_K_M = f"{New_Quote_1h/1000:.2f}K" if New_Quote_1h < 1_000_000 else f"{New_Quote_1h/1_000_000:.2f}M"
        Count_K_M = f"{New_Count_1h/1000:.2f}K" if New_Count_1h < 1_000_000 else f"{New_Count_1h/1_000_000:.2f}M"

        # تحديد الاتجاه (صعود أو هبوط)
        if Last_price > Weighted_average_price:
            Up_down = "Up"
        elif Last_price < Weighted_average_price:
            Up_down = "Down"
        else:
            Up_down = "Stable"

        # إرجاع النتائج
        return Volume_K_M, Quote_K_M, Count_K_M, Up_down

    except Exception as e:
        print(f"Error occurred in K_M: {e}")
        # إذا حدث خطأ، يمكن ببساطة تجاوز أو إرجاع قيمة افتراضية
        return None, None, None, None
