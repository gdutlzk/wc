
#[root@js python]# cat wc2.py
#!/usr/bin/python
#coding:utf-8
import sys
def wordCount(s):
    chars = len(s)
    words = len(s.split())
    lines = s.count('\n')
    print (chars, words, lines)
    print ("你好!")

s = open('外星人').read()
wordCount(s)

#file_name = input("Enter the file_name: ")
#try:
#	with open('file_name') as file_object:
#		s = file_object.read()#字符串变量s
#except FileNotFoundError 
#	msg = 'Sorry,the file' + file_name + 'does not exist'
#	print(msg)
	num_chars = len(s)
	num_words = len(s.split())
	num_lines = s.count('\n')
