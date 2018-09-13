#wordcount
import os
import os.path
import sys
def wordcount(file):
	chars = 0
	word = [] #单词列表
	lines = 0
	for line in file:
		chars += len(line)
		line = line.replace("[^0-9a-zA-Z\\u4e00-\\u9fff]", " ") #正则表达式替代非英文、汉字、非数字
		line = line.strip() #消除左右空格
		lb = line.split(" ") #以空格分割
		word.extend(lb)
		words = len(word)
		lines += 1
	return chars , words , lines

def linecount(path):
	blank, comments, codelines, totalines, begin_comment, long_comment= 0, 0, 0, 0, 0, 0
	f_list = open(path).readlines()
	for line in f_list:
				totalines += 1
				if line.strip().startswith('#'): #于检查字符串是否是以#开头,是返回TRUE
					comments += 1
				elif line.strip().startswith("'''") or line.strip().startswith('"""'):
					if begin_comment == 0:
						long_comment += 1
						begin_comment = 1
					else :
						begin_comment = 0
						comments += long_comment
				elif len(line) <= 1:
					blank += 1
				else:
					codelines += 1
	return totalines, comments, codelines, blank

def command(skr, path):
	file = open(path, "r")
	chars, words, lines = wordcount(file)
	totalines, comments, codelines, blank = linecount(path)
	if skr == '-c':
		print('字符数', chars)
	elif skr == '-w':
		print('单词数', words)
	elif skr == '-l':
		print('行数', lines)
	elif skr == '-s':
		search(sys.argv[1])  
	elif skr == '-a':
		print('空格行', blank)
		print('代码行', codelines)
		print('注释行', comments)

def search(path, ci):
	for filename in os.listdir(path):
		fp = os.path.join(path, filename)
		if os.path.isfile(fp) and ci in filename: #如果路径fp是一个存在的文件，返回True。
			command(-q, fp)
		elif os.path.isdir(fp): #如果fp是一个存在的目录，则返回True
			search(fp, ci) #递归处理
#search(sys.argv[1], sys.argv[2])

print("please input:")

if len(sys.argv) < 4:
#print(sys.argv)
	"""if sys.argv[1] != "-c" and sys.argv[1] != "-w" and sys.argv[1] != "-l":
		print("参数出现错误")
	else:
		skr = sys.argv[1]
		path = sys.argv[2]
elif len(sys.argv) == 4:
	if sys.argv[2] != "-c" and sys.argv[2] != "-w" and sys.argv[2] != "-l" and sys.argv[2] != "-a":
		print("参数出现错误")
	elif sys.argv[1] != "-s":
		print("参数出现错误")
	else:
		skr = sys.argv[2]
		path = sys.argv[3]"""
skr,path = input().split()
command(skr, path)
#/Users/lzk/Desktop/python/wc/qaq.java






















