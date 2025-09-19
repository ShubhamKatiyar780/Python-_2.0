from datetime import datetime
import playsound
import time
import os
class AlarmClock:
    def __init__(self):
        while True:
            self.set_day = input("set your day: ").strip().capitalize()
            if self.set_day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
                break
            print("Invalid day. Please enter a valid day.")
        while True:
            self.set_time = input("Set your time(HH:MM:SS): ")
            try:
                datetime.strptime(self.set_time, "%H:%M:%S")
                break
            except ValueError:
                print("Invalid time format. Please enter time in HH:MM:SS format.")
        self.song = "C:/Users/katiy/Music/Humnava Mere Music Ringtone Download - MobCup.Com.Co.mp3"
        if not os.path.exists(self.song):
            print(f"Error: The file {self.song} does not exist.")
            return
        self.checkTime()

    def checkTime(self):
        print("Alarm set successfully!")
        while True:
            # self.current_date = datetime.now().strftime("%d-%m-%Y")
            self.current_time = datetime.now().strftime("%H:%M:%S")
            self.current_day = datetime.now().strftime("%A")
            print(f"Today is: {self.current_day}")
            print(f"Current time is: {self.current_time}")
            if (self.current_day == self.set_day):
                if (self.current_time == self.set_time):
                    print("Alarm is on!")
                    playsound.playsound(self.song)
                    break
            time.sleep(1)

obj = AlarmClock()