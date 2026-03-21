import os
import time 

import pygetwindow as gw


distraction_keyword = ["YouTube", "Instagram", "TikTok", "Facebook"]
Time_Limit = 15 


def is_distraction(app_name):
    for keyword in distraction_keyword:
        if keyword.lower() in app_name.lower():
            return True
    return False

def get_active_window():
    try:
       window = gw.getActiveWindow()  
       if window:
            return window.title
       return "No active window"
    except:
       return "Error getting window"   

app_time = {}

last_window = ""

while True:
    active_window = get_active_window()

    if active_window not in app_time:
        app_time[active_window] = 0

    app_time[active_window] += 1

    os.system('cls' if os.name == 'nt' else 'clear') 

    print("=== App Usage (Live) ===\n")

    for app , seconds in app_time.items():
        if is_distraction(app):
            if seconds >= Time_Limit:
              print(f"{app} → {seconds} sec ❌ LIMIT EXCEEDED 🚨")
            else:
                print(f"{app} → {seconds} sec ❌ DISTRACTION")
        else :
            print(f"{app} → {seconds} sec ✅")
    time.sleep(1)        