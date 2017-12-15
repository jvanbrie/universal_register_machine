import argparse
verboseprint = lambda *a, **k: None

def main(args):
	global verboseprint
	verboseprint = print if args.v else lambda *a, **k: None
	command_file = open(args.input,'r')
	one_command = command_file.readline()

	# macro registers
	A = 0
	B = 0
	C = 0

	registers = {}
	commands = []

	len_count = 0
	while(one_command != ''):
		len_count +=1
		one_command = command_file.readline()

	commands = [''] * len_count
	command_file = open(args.input,'r')
	one_command = command_file.readline()
	i = 0
	while(one_command != ''):
		commands[i] = one_command[:-1]
		i += 1
		one_command = command_file.readline()

	def print_state(line):
		print ("State after line %d:" % line)
		print (registers)

	line = 0
	print_count = 0

	while(True):
		command = commands[line]
		if command == 'halt':
			break
		command_inputs = command.split()
		# verboseprint(command_inputs)
		if(len(command_inputs) == 3):
			try:
				registers[command_inputs[1]] += 1
			except:
				registers[command_inputs[1]] = 1
			line = (int(command_inputs[2]))
		else:
			try:
				registers[command_inputs[1]]
			except:
				registers[command_inputs[1]] = 0
			if registers[command_inputs[1]] == 0:
				line = (int(command_inputs[3]))
			else:
				registers[command_inputs[1]] -= 1
				line = (int(command_inputs[2]))
		print_count += 1
		if(print_count >= 100000):
			verboseprint(command_inputs)
			print_state(line)
			# print_count = 0
	print("Final state:")
	print_state(0)



def parse_args():
	parser = argparse.ArgumentParser(description='Splitting video transcripts')
	parser.add_argument('-i', required = True, dest = 'input', action='store',
	help='transcript file large')
	parser.add_argument('-v', action='store_true', required = False,
        help='enable verbose')

	args = parser.parse_args()
	print(main(args))

parse_args()

