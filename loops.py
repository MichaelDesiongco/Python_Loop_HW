# 1
import random


moods = ["Happy","Sad","Energetic","Calm"]

days_of_the_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

for day in days_of_the_week:
    mood = random.choice(moods)

print(f"On {day}, you were feeling {mood}")

# 2

import random

moods = ["Happy","Sad","Energetic","Calm","Tired"]

days_of_week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

times_of_day = ["Morning","Afternoon","Evening"]

for day in days_of_week:
    for time in times_of_day:
        mood = random.choice(moods)
print(f"On {day} {time} you were {mood}")