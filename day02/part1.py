#usr/bin/env python3

if __name__ == "__main__":
	score = 0
	with open("input.txt", encoding="utf-8") as f:
		for line in f:
			opponent_move = line[0]
			your_move = line[2]
			if (your_move == "X"):
				score += 1
				if (opponent_move == "C"):
					score += 6
				elif (opponent_move == "A"):
					score += 3
				else:
					score += 0
			elif (your_move == "Y"):
				score += 2
				if (opponent_move == "A"):
					score += 6
				elif (opponent_move == "B"):
					score += 3
				else:
					score += 0
			elif (your_move == "Z"):
				score += 3
				if (opponent_move == "B"):
					score += 6
				elif (opponent_move == "C"):
					score += 3
				else:
					score += 0
			else:
				print("Invalid input")
				break
		print("Your score: ", str(score))
