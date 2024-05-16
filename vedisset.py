from vedis import Vedis

device_id = "123456"
wifi = "MyWifi"
wifipass = "MyPassword"
device_name = "MyDevice"
poll_period = "60"
chat_number = "12345"

with Vedis() as db:
    db.Set(f"wifi_{device_id}", wifi)
    db.Set(f"wifipass_{device_id}", wifipass)
    db.Set(f"device_name_{device_id}", device_name)
    db.Set(f"poll_period_{device_id}", poll_period)
    db.Set(f"chat_number_{device_id}", chat_number)
