seconds = int(input("Vvedite kol-vo sekund (0 <= n < 8640000): "))

day_sec = 24 * 60 * 60
hour_sec = 60 * 60
minute_sec = 60


days = seconds // day_sec
seconds = seconds % day_sec

hours = seconds // hour_sec
seconds = seconds % hour_sec

minutes = seconds // minute_sec
secs = seconds % minute_sec

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif days % 10 in [2, 3, 4] and not (12 <= days % 100 <= 14):
    day_word = "дні"
else:
    day_word = "днів"


hours = str(hours).zfill(2)
minutes = str(minutes).zfill(2)
secs = str(secs).zfill(2)


print(f"{days} {day_word}, {hours}:{minutes}:{secs}")
