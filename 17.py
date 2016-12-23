import numpy as np

characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','z']
min_nr = 1
max_nr = 26

def is_valid(word, colors, sums) :
	sum_red = 0
	sum_green = 0
	sum_blue = 0

	for i in range(len(word)) :
		character = word[i]
		color = colors[i]
		if(color == 'r') :
			sum_red += character
		if(color == 'g') :
			sum_green += character
		if(color == 'b') :
			sum_blue += character
	return sum_red == sums[0] and sum_green == sums[1] and sum_blue == sums[2]

def to_word(word) :
	result = ''
	for c in word : 
		result = result + chr(c+96)
	return result


def complete(word, char_index, colors, sums) :
	for c in range(1,26) :
		word[char_index] = c
		if(char_index == len(word)-1) :
			if(is_valid(word,colors,sums)) :
					print(to_word(word))
		else :
			complete(word, char_index+1, colors, sums)


def combinations(colors, sums) :
	characters = len(colors)
	word = np.repeat(0,characters)
	complete(word, 0, colors, sums)

def create_word(c_red, c_green, c_blue, colors) :
	i_red = 0
	i_green = 0
	i_blue = 0
	word = ''
	for c in colors :
		if(c == 'r') :
			word = word + chr(c_red[i_red] + 96)
			i_red += 1
		if(c == 'g') :
			word = word + chr(c_green[i_green] + 96)
			i_green += 1
		if(c == 'b') :
			word = word + chr(c_blue[i_blue] + 96)
			i_blue += 1
	return word

def main():
	colors = ['r','g','g','b','r','g','r','b','b','b','r','r']
	sums = [56,30,60]
	parts = [0,0,0]
	for i in range(len(colors)) :
		if(colors[i] == 'r') :
			parts[0] += 1
		if(colors[i] == 'g') :
			parts[1] += 1
		if(colors[i] == 'b') :
			parts[2] += 1

	combinations_red = find_sums(sums[0],parts[0])
	combinations_green = find_sums(sums[1],parts[1])
	combinations_blue = find_sums(sums[2],parts[2])
	print(len(combinations_red))
	print(len(combinations_green))
	print(len(combinations_blue))
	for c_red in combinations_red :
		for c_green in combinations_green :
			for c_blue in combinations_blue :
				print(create_word(c_red, c_green, c_blue, colors))
				# print(c_red, c_green, c_blue)

def find_sums(total, parts) :
		if(parts==0) :
			return [[]]
		if(parts==1) :
			if(total > max_nr) :
				return []
			else :
				return [[total]]
		sums = []
		for i in range(min_nr, min(total,max_nr+1)) :
			results = find_sums(total-i, parts-1)
			for result in results :
				combination = [i]
				combination.extend(result)
				sums.append(combination)
		return sums

if __name__ == "__main__":
	main()
