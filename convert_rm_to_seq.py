import argparse
verboseprint = lambda *a, **k: None

def seq_cons(head,tail):
	return (2**head) * (2 * tail + 1)


def main(args):
	global verboseprint
	verboseprint = print if args.v else lambda *a, **k: None
	command_file = open(args.input,'r')

	seq_number = 0
	file_list = []
	one_command = command_file.readline()
	while(one_command != ''):
		file_list += [one_command]
		one_command = command_file.readline()

	file_list.reverse()
	print(file_list)
	for one_command in file_list:
		if(one_command[-1] == '\n'):
			one_command = one_command[:-1]
		command_list = one_command.split(' ')
		if(command_list[0] == 'inc'):
			seq_number = seq_cons(seq_cons(int(command_list[1]), seq_cons(int(command_list[2]),0)),seq_number)
		elif(command_list[0] == 'dec'):
			seq_number = seq_cons(seq_cons(int(command_list[1]), seq_cons(int(command_list[2]),seq_cons(int(command_list[3]),0))),seq_number)
		else:
			seq_number = seq_cons(0,seq_number)
		verboseprint(one_command)
		verboseprint(seq_number)




	return seq_number





def parse_args():
	parser = argparse.ArgumentParser(description='Splitting video transcripts')
	parser.add_argument('-i', required = True, dest = 'input', action='store',
	help='transcript file large')
	parser.add_argument('-v', action='store_true', required = False,
        help='enable verbose')

	args = parser.parse_args()
	print(main(args))

parse_args()

