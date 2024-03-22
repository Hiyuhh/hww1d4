import random
# 1. The Range Riddle
    # Task 1: Your Mood Today
moods = ["happy" , "sad", "energetic", "calm", "hopeful", "depressed", "angry"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in range(len(days)):
    random.choice(moods) 
    print(f"On {days[i]}, you were feeling {random.choice(moods)}." )

# 2. Double Scoop with Nested Loops
    # Task 1: Your Mood Tracker
time_days = ["morning", "afternoon", "evening", "night"]
for x in range(len(days)):
    for y in range(len(time_days)):
        print(f"On {days[x]} {time_days[y]} you were {random.choice(moods)}")

# 3. Loop Condition Logic
    # Task 1: Loop Condition Exploration
loopy = 100
while True:
    print("in a loop")
    loopy -= 20
    if loopy == 0:
        break

# Task 2: Conditional Exit
loopy = 0
while loopy < 10:
    loopy += 1
    print("in a loop that will end ;)")
    loopy >= 10

# 4. Python's Random Game Night
inventory = ["sword", "shield", "armor", "staff", "wand", "potion", "poison"]
npc_choice = random.choice(inventory)
while True:
    user_input = input("What item was selected? Pick sword, shield, armor, staff, wand, potion or poison:")
    if npc_choice == user_input:
        print("Congrats you got it right!")
        break
    else:
        print("Oops, you are wrong!")

# 5. Looping Lists - The Rhythm of Repetition
# Our playlist of genres
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
message = ["nice", "good taste", "dope", "exciting"]
for i in range(len(genres)):
    track = i + 1
    print(f"You're on track .{track} in {genres[i]}, that's {message[i]}!")

# Task 2: The Remix Artist with while
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
message = ["nice", "good taste", "dope", "exciting"]

track = 1
while track <= len(genres):
    song = random.choice(genres)
    print(f"Track {track}: in {song}, that's {random.choice(message)}!")
    if  song == 'Hip-hop':
        print("Playlist stopped because Hiphop was playing next and we hate Hiphop so much!!!!!!!")
        break
    track += 1

# Task 3: Light Show Technician Loop
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']

for i in range(len(genres)):
    track = i + 1
    if genres[i] == 'Classical':
        print(f"{genres[i]} is not suitable for a light show... ;-;") # not sure if the task was to add a message before it skips or not 
        continue
    print(f"Track {track}: for {genres[i]}, the light show is ready!")


# 6. Advanced Looping Techniques
    # Task 1: The Selective DJ
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
sublist = genres[1:4]
print(sublist)

# Task 2: The One-Liner Band with List Comprehensions
genres = ['Jazz', 'Rock', 'Hip-hop', 'Classical']
music_list = [music + " Music"  for music in genres]
print(music_list)

# Task 3: Numerical Beats with range
beat = 10
while beat >= 1:
    if beat ==1:
        print(f"{beat} The beat drops now!")
    else:
        print(beat)
    beat -= 1

# Task 3: Numerical Beats with range
for beat in range(10, 0, -1):
    if beat ==1:
        print(f"{beat} The beat drops now!")
    else:
        print(beat)