#usr/bin/env python3

if __name__ == "__main__":
	score = 0
	with open("input.txt", encoding="utf-8") as f:
		for line in f:
			opponent_move = line[0]
			your_move = line[2]
			if (your_move == "X"):
				if (opponent_move == "A"):
					score += 3
				elif (opponent_move == "B"):
					score += 1
				else:
					score += 2
			elif (your_move == "Y"):
				score += 3
				if (opponent_move == "A"):
					score += 1
				elif (opponent_move == "B"):
					score += 2
				else:
					score += 3
			elif (your_move == "Z"):
				score += 6
				if (opponent_move == "A"):
					score += 2
				elif (opponent_move == "B"):
					score += 3
				else:
					score += 1
			else:
				print("Invalid input")
				break
		print("Your score: ", str(score))
