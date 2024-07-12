#讀取檔案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding ='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	new = []
	person = None
	allen_word_count = 0
	viki_word_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':

		elif name == 'Viki':

		print(s)
	return new

def write_file(filename, lines):
	with open(filename,'w') as f:
		for line in lines:
			f.write(line + '\n')
			
def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt', lines)

main() #進入點