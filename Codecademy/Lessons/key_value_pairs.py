songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", \
"What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

playlist = zip(songs, playcounts)

plays = {key:value for key, value in playlist}
print(plays)

plays["Purple Haze"] = 1
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)