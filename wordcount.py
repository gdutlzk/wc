wordcount
import sys
import os
import os.path
import re
def wordcount(file_name):
#	with open('file_name') as file
	f = file_name.readlines()
	chars = 0
	word = [] #单词列表
	lines = 0
	for line in f:
		chars += len(line)
#		lines += 1
		line = line.replace("[0-9a-zA-Z\u4e00-\u9fff]", " ") #正则表达式替代非英文、汉字、非数字
		line = line.strip() #消除左右空格
		lb = line.split(" ") #以空格分割
		word.extend(lb)
		words = len(word)
		lines = s.count('\n')
	return chars , words , lines

def search(path, ci):
	for filename in os.listdir(path):
		fp = os.path.join(path, filename)
		if os.path.isfile(fp) and ci in filename: #如果路径fp是一个存在的文件，返回True。
			print (fp)
		elif os.path.isdir(fp): #如果fp是一个存在的目录，则返回True
			search(fp, ci) #递归处理
search(sys.argv[3])

def linecount(path):
	blank， comments, codelines, totalines, count ,temp = 0, 0, 0, 0, 0, 0
	f_list = os.listdir(dirpath)
	for i in f_list:
		if os.path.splitext(i)[1] == '.py':
		#分离文件名与扩展名；确认是否为py文件
			print(i)
			with open(i, 'r', encoding='utf-8') as ff
				while True:
					line = fp.readline()
					totalines += 1
					if not line:
						break
					elif line.strip().startswith('#'): #于检查字符串是否是以#开头,是返回TRUE
						comments += 1
					elif line.strip().startswith("'''") or line.strip().startswith('"""'):
						comments += 1
						if line.count('"""') == 1 or line.count("'''") == 1: #注释行下面
							while True:
								line = ff.readline()
								totalines += 1
								comments +=1
								if ("'''" in line) or ('"""' in line):
									break
					elif line.strip():
						codelines += 1
					else:
						blank +=1
				print('the nuber of totalines is : ' + str(totalines-1))
				print('the nuber of comments is : ' + str(comments))
				print('the nuber of codelines is : ' + str(codelines))
				print('the nuber of blanklines is : ' + str(blank))
				blank, comments, codelines, totalines = 0, 0, 0, 0

print("请输入你的功能和文件路径")
skr, name = input().split()
def command(skr， name):
	file_name = open(name, "r")
#	path = name 
	chars, words, lines = wordcount(file_name)
	totalines, comments, codelines, blank = linecount(name)
	if str == '-c':
		print('字符数',chars)
	elif str == '-w':
		print('单词数',words)
	elif str == '-l':
		print('行数',lines)
	elif str == '-s':
		search(sys.argv[3])
	elif str == '-a':
		print('空格行',blank)
		print('代码行',codelines)
		print('注释行',comments)
	elif str == '-q':#读取全部信息
		print('字符数', chars)
		print('单词数', words)
		print('行数', totalines)
		print('空格行', blank)
		print('代码行', codelines)
		print('注释行', comments)















