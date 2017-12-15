
import argparse
import re
verboseprint = lambda *a, **k: None

def main(args):
	global verboseprint
	verboseprint = print if args.v else lambda *a, **k: None
	
	macro_files = ["copy.txt","zero.txt","pop.txt","dest_copy.txt","read.txt","mult_2.txt","push.txt","write.txt", "universal_register_machine.txt"]

	command_file = open(args.input,'r')
	output_file = open(args.output,'w+')
	one_command = command_file.readline()

	macros = {}
	macro_lens = {}


	# create macros dictionary 
	# keys: macros
	# values: [[variable list],macro string]
	for macro in macro_files:
		macro_file = open('macros' + '/' + macro,'r')
		#title consists of name, and inputs
		macro_title = macro_file.readline()
		macro_title_list = (macro_title[:-1]).split()
		macro_name = macro_title_list[0]
		macros[macro_name] = [macro_title_list[1:],'']
		macro_line = macro_file.readline()
		macro_len = 0
		while(macro_line != ''):
			macro_len += 1
			macros[macro_name][1] += macro_line
			macro_line = macro_file.readline()
		macro_lens[macro_name] = macro_len

	registers = {}
	commands = []

	# count number of commands 
	len_count = 0
	while(one_command != ''):
		len_count +=1
		one_command = command_file.readline()

	# get the length of each macro and put it in commands
	commands = [0] * len_count
	command_file = open(args.input,'r')
	one_command = command_file.readline()
	i = 0
	ouput_index = 0
	while(one_command != ''):
		command_inputs = one_command[:-1].split()
		commands[i] = ouput_index

		# this try/except block skips non-macros
		try:
			macros[command_inputs[0]]
		except:
			ouput_index += 1
			i += 1
			one_command = command_file.readline()
			continue

		ouput_index += macro_lens[command_inputs[0]]
		print(ouput_index)
		i += 1
		one_command = command_file.readline()




	# write new no macro file
	print(commands)
	command_file = open(args.input,'r')
	command_index = 0
	one_command = command_file.readline()
	while(one_command != ''):
		if(one_command[-1] == '\n'):
			one_command = one_command[:-1]
		command_inputs = one_command.split()
		print(command_inputs)
		cur_macro = command_inputs[0]
		index_offset = commands[command_index]


		# try involves macro
		try:
			macros[cur_macro]
			cur_macro_string = macros[cur_macro][1]
			#handles integers in macro
			cur_macro_list = re.split(" ",cur_macro_string)
			for word_ind in range(len(cur_macro_list)):
				word = cur_macro_list[word_ind]
				try:
					word = str(int(word) + index_offset)
				except:
					pass
				cur_macro_list[word_ind] = word
			cur_macro_string = ' '.join(cur_macro_list)

			# handles macro variables
			for var_ind in range(len(macros[cur_macro][0])):
				# plus one due to the first value in command_inputs being the macro name rather than a variable
				replaced_word = command_inputs[var_ind + 1]
				try:
					replaced_word = str(commands[int(replaced_word)])
				except:
					pass
				replaced_word = ' ' + replaced_word + ' '
				cur_macro_string = cur_macro_string.replace(' ' + macros[cur_macro][0][var_ind] + ' ', replaced_word)
		

			output_file.write(cur_macro_string + '\n')
		except:
			for command_ind in range(len(command_inputs)):
				try:
					command_inputs[command_ind] = str(commands[int(command_inputs[command_ind])])
				except:
					pass
			print(' '.join(command_inputs))
			output_file.write(' '.join(command_inputs) + '\n')

		one_command = command_file.readline()

		command_index += 1


	# write new no macro file
	# print(commands)
	# command_file = open(args.input,'r')
	# command_index = 0
	# one_command = command_file.readline()
	# while(one_command != ''):
	# 	if(one_command[-1] == '\n'):
	# 		one_command = one_command[:-1]
	# 	command_inputs = one_command.split()
	# 	print(command_inputs)
	# 	cur_macro = command_inputs[0]

	# 	#handles non-macro lines
	# 	try:
	# 		macros[cur_macro]
	# 	except:
	# 		for word_ind in range(len(command_inputs)):
	# 			replaced_word = command_inputs[word_ind]
	# 			try:
	# 				replaced_word = str(commands[int(replaced_word)])
	# 			except:
	# 				pass
	# 			command_inputs[word_ind] = replaced_word
	# 		output_file.write(' '.join(command_inputs) + '\n')
	# 		one_command = command_file.readline()
	# 		command_index += 1
	# 		continue
	# 	cur_macro_string = macros[cur_macro][1]
	# 	index_offset = commands[command_index]

	# 	#handles integers in macro
	# 	cur_macro_list = cur_macro_string.split(' ')
	# 	for word_ind in range(len(cur_macro_list)):
	# 		word = cur_macro_list[word_ind]
	# 		try:
	# 			int(word)
	# 			print("This word IS an int: " + word)
	# 			word = str(int(word) + index_offset)
	# 		except:
	# 			print("This word is not an int: " + word)
	# 		cur_macro_list[word_ind] = word
	# 	cur_macro_string = ' '.join(cur_macro_list)

	# 	# handles macro variables
	# 	for var_ind in range(len(macros[cur_macro][0])):
	# 		# plus one due to the first value in command_inputs being the macro name rather than a variable
	# 		replaced_word = command_inputs[var_ind + 1]
	# 		try:
	# 			replaced_word = str(commands[int(replaced_word)])
	# 		except:
	# 			pass
	# 		replaced_word = ' ' + replaced_word
	# 		cur_macro_string = cur_macro_string.replace(' ' + macros[cur_macro][0][var_ind], replaced_word)
		
	# 	print(cur_macro_string)
	# 	print(index_offset)

	# 	print("new macro")
	# 	output_file.write(cur_macro_string + '\n')
	# 	one_command = command_file.readline()

	# 	command_index += 1

	output_file.close()

		






def parse_args():
	parser = argparse.ArgumentParser(description='Splitting video transcripts')
	parser.add_argument('-i', required = True, dest = 'input', action='store',
	help='transcript file large')
	parser.add_argument('-o', required = True, dest = 'output', action='store',
	help='transcript file large')
	parser.add_argument('-v', action='store_true', required = False,
        help='enable verbose')

	args = parser.parse_args()
	print(main(args))

parse_args()

