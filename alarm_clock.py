from playsound import playsound
import time

def alarm(seconds):
    time_elapsed = 0
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"Time left: {minutes_left} minutes and {seconds_left} seconds", end='\r')


alarm(10)   
     
