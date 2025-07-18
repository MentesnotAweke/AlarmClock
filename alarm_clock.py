from playsound import playsound
import time
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR + CLEAR_AND_RETURN, end='')
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        print(f"Time left: {minutes_left} minutes and {seconds_left} seconds", end='\r')
    playsound('alarm_sound.mp3')

minutes = int(input("Enter the number of minutes for the alarm: "))
seconds = int(input("Enter the number of seconds for the alarm: "))
total_seconds = minutes * 60 + seconds

alarm(total_seconds)   
     
