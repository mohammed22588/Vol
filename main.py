from flask import Flask
import threading
import json
import websocket
import time
import Eqution as Eq
import Volu1 as Vol

app = Flask(__name__)

@app.route('/')
def home():
    return "WebSocket is running!"

def on_open(ws):
    try:
        print("Opened connection WebSocket Start...")
        SUBSCRIBE = {"method": "SUBSCRIBE", "params": ["!ticker@arr"], "id": 1}
        ws.send(json.dumps(SUBSCRIBE))
    except Exception as massgge:
        print(massgge)

def on_message(ws, message):
    data = json.loads(message)
    date_time, time_stamp, _year, _month, _day, _hour, _minute, _secand = Eq.time_date()
    threads = []
    for ticker in data:
        if ((ticker['s'].endswith('USDT'))):
            t = threading.Thread(target=Vol.volume_24, args=(
                ticker['s'], int(ticker['E']), float(ticker['p']), float(ticker['P']), float(ticker['w']),
                float(ticker['c']), float(ticker['o']), float(ticker['h']), float(ticker['l']), float(ticker['v']),
                float(ticker['q']), float(ticker['n']), float(ticker['Q']), float(ticker['b']), float(ticker['B']),
                float(ticker['a']), float(ticker['A']), date_time, time_stamp, _year, _month, _day, _hour, _minute, _secand
            ))
            threads.append(t)
            t.start()

    # الانتظار حتى تنتهي جميع الثريدات
    for t in threads:
        t.join()

def start_websocket():
    url = "wss://stream.binance.com:9443/ws"
    ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message)
    while True:
        try:
            ws.run_forever()
        except KeyboardInterrupt:
            print("Interrupted by user.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    # بدء WebSocket في ثريد منفصل
    websocket_thread = threading.Thread(target=start_websocket)
    websocket_thread.start()

    # بدء Flask على المنفذ 8000
    app.run(host="0.0.0.0", port=8000)
