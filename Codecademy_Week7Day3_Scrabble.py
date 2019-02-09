letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]  # List
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]  # List

# Step 15 - handle lowercase inputs
letters += [letter.lower() for letter in letters]
points *= 2

# Step 1 - Create new dictionary from zip lists
letter_to_points = {letter:point for [letter, point] in zip(letters, points)}

print(letter_to_points)  # Results in {'A': 1, 'h': 4, 't': 1, 'U': 1, 'H': 4, 'P': 3, 'j': 8, 'o': 1, 'c': 3, 'g': 2, 'G': 2, 'D': 2, 'Q': 10, 'N': 4, 'B': 3, 'n': 4, 'i': 1, 'e': 1, 'x': 8, 'v': 4, 'L': 1, 'p': 3, 'Y': 4, 'b': 3, 'E': 1, 'q': 10, 'K': 5, 'd': 2, 'k': 5, 'r': 1, 'X': 8, 'I': 1, 'O': 1, 'S': 1, 'Z': 10, 'W': 4, 'z': 10, 'F': 4, 'w': 4, 'C': 3, 'y': 4, 'V': 4, 'M': 3, 'u': 1, 'T': 1, 'f': 4, 'a': 1, 's': 1, 'J': 8, 'm': 3, 'l': 1, 'R': 1}

# Step 2 - Add blank " " letter key with a value of "0"
letter_to_points[" "] = 0

print(letter_to_points)  # Results in {'A': 1, 'h': 4, 't': 1, 'U': 1, 'H': 4, 'P': 3, 'j': 8, 'o': 1, 'c': 3, 'g': 2, 'G': 2, 'D': 2, 'Q': 10, 'N': 4, 'B': 3, 'n': 4, 'i': 1, 'e': 1, 'x': 8, 'v': 4, 'L': 1, 'p': 3, 'Y': 4, 'b': 3, 'E': 1, 'q': 10, 'K': 5, 'd': 2, 'k': 5, 'r': 1, 'X': 8, ' ': 0, 'I': 1, 'O': 1, 'S': 1, 'Z': 10, 'W': 4, 'z': 10, 'F': 4, 'w': 4, 'C': 3, 'y': 4, 'V': 4, 'M': 3, 'u': 1, 'T': 1, 'f': 4, 'a': 1, 's': 1, 'J': 8, 'm': 3, 'l': 1, 'R': 1}

# Step 3, 4, 5, and 6  - Create "score_word" function
def score_word(word):  # Create function "score_word"
  point_total = 0  # Set "point_total" variable to an initial value of 0
  for letters in word:  # For the index "letters" in the function parameter "word"
    point_total += letter_to_points.get(letters, 0)  # "point_total" variable equals "point_value" plus the index "letters" using the get() method from the "letter_to_points" dictionary
  return point_total

# Steps 7 and 8
brownie_points = score_word("BROWNIE")  # Set "brownie_points" variable to the "score_word()" function passing "BROWNIE" as the "word" parameter
print(brownie_points)  # Results in 15

# Step 9 - Create new dictionary "player_to_words"
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"], "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# Step 10 - Create empty dictionary "player_to_points"
player_to_points = {}

# Steps 11, 12, 13 - Iterate and create loop
for player, words in player_to_words.items():  # For indexes "player" and "words" in the "player_to_words" dictionary using the items() method.
  player_points = 0  # Create the "player_points" variable and set it equal to "0"
  for word in words:  # For the index "word" in the index "words"
    player_points += score_word(word)  # The variable "player_points" is equal to "player_points" plus the score_word() function passing the index "word" as the "word" parameter
  player_to_points[player] = player_points  # Set the current player (index) value to be a key of player_to_points, with a value of player_points.
  
print(player_to_points)  # Results in {'wordNerd': 32, 'player1': 29, 'Lexi Con': 31, 'Prof Reader': 31}

# Adding optional enhancements

print(player_to_words)  # Results in {'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD'], 'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE']}

  
play_word("player1", "COOKIE")  # Tests the "play_word" function
print(player_to_words)  # Results in (player1 list is updated): {'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD'], 'player1': ['BLUE', 'TENNIS', 'EXIT', 'COOKIE'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE']}

# Step 15 - update_point_totals()
def update_point_totals():
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

# Step 15 - "play_word()"
def play_word(player, word):  # Function that takes two parameters, "player" and "word"
  player_to_words[player].append(word)  # Appends the parameter "word" to the value of the key/parameter "player" for the "player_to_words" dictionary
  update_point_totals()  # Calls the update_point_totals() function
  

play_word("player1", "COOKIE")  # Tests the "play_word" function
print(player_to_words)  # Results in (player1 list is updated): {'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD'], 'player1': ['BLUE', 'TENNIS', 'EXIT', 'COOKIE'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE']}  
print(player_to_points)  # Results in {'wordNerd': 32, 'player1': 41, 'Lexi Con': 31, 'Prof Reader': 31}  **Compare to line 41**













