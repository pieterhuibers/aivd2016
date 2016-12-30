import numpy as np
import sys

r_nums = [1,4,7,10,13,16,19,22]
g_nums = [2,5,8,11,14,20,23,26]
b_nums = [6,9,12,15,18,21]
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

def create_word(c_red, c_green, c_blue, colors) :
	i_red = 0
	i_green = 0
	i_blue = 0
	word = ''
	numbers = '['
	for c in colors :
		if(c == 'r') :
			word = word + chr(c_red[i_red] + 96)
			numbers = numbers + str(c_red[i_red]) + ','
			i_red += 1
		if(c == 'g') :
			word = word + chr(c_green[i_green] + 96)
			numbers = numbers + str(c_green[i_green]) + ','
			i_green += 1
		if(c == 'b') :
			word = word + chr(c_blue[i_blue] + 96)
			numbers = numbers + str(c_blue[i_blue]) + ','
			i_blue += 1
	return word+','+numbers[0:-1] + ']'

def find_sums(total, parts, options) :
		if(parts==0) :
			return [[]]
		if(parts==1) :
			if(total > max_nr or not(total in options)) :
				return []
			else :
				return [[total]]
		sums = []
		for i in options :
			if(i < total) :
				results = find_sums(total-i, parts-1, options)
				for result in results :
					combination = [i]
					combination.extend(result)
					sums.append(combination)
		return sums

def check_colors(colors, sums) :
	parts = [0,0,0]
	for i in range(len(colors)) :
		if(colors[i] == 'r') :
			parts[0] += 1
		if(colors[i] == 'g') :
			parts[1] += 1
		if(colors[i] == 'b') :
			parts[2] += 1

	combinations_red = find_sums(sums[0],parts[0], r_nums)
	combinations_green = find_sums(sums[1],parts[1], g_nums)
	combinations_blue = find_sums(sums[2],parts[2], b_nums)
	total_combinations = len(combinations_red)*len(combinations_green) * len(combinations_blue)
	print total_combinations
	for c_red in combinations_red :
		for c_green in combinations_green :
			for c_blue in combinations_blue :
				print(create_word(c_red, c_green, c_blue, colors))

def main(args):
	i = 0
	colors = args[0:-3]
	sums = [0,0,0]
	sums[0] = int(args[-3])
	sums[1] = int(args[-2])
	sums[2] = int(args[-1])
	check_colors(colors, sums)

if __name__ == "__main__":
	if len(sys.argv) > 1 :
		main(sys.argv[1:])
