file = open("data.txt", "r")
lines = file.readlines()

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
numbers_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

suma = 0

string = "one9eight"

for line in lines:
		print("="*20)
		first = ""
		last = ""

		firstIdx = -1
		lastIdx = -1

		# Searching numbers forward
		for i in range(len(line)):
				if line[i] in numbers:
						first = line[i]
						firstIdx = i
						print(f"Found {first} on index {firstIdx}")
						break

				# Searching numbers backwards
		for i in range(len(line) - 1, -1, -1):
				if line[i] in numbers:
						last = line[i]
						lastIdx = i
						print(f"Found {last} on index {lastIdx}")
						break
						
		lastIdxCopy = lastIdx
		for ns in numbers_str:
			index = line.rfind(ns,lastIdxCopy,-1)
			if index != -1 and index > lastIdx:
				lastIdx = index
				last = str(numbers_str.index(ns)+1)
				print(f"Found {last} word on index {lastIdx}")

		firstIdxCopy = firstIdx
		for ns in numbers_str:
			index = line.find(ns,0, firstIdxCopy)
			if index != -1 and index < firstIdx:
				firstIdx = index
				first = str(numbers_str.index(ns)+1)
				print(f"Found {first} word on index {firstIdx}")
				
		word = first + last
		suma += int(word)

		print(f"Whole number: {word}")
		print(f"Partial sum: {suma}")