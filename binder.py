#!/usr/bin/pyhton3

import sys
from subprocess import call

def c_output(f1_bin, f2_bin):
	f1_str = ''
	f2_str = ''
	for i in range(0, len(f1_bin)):
		f1_str = f1_str + "\\x" + f1_bin[i:i + 1].hex()
	for i in range(0, len(f2_bin)):
		f2_str = f2_str + "\\x" + f2_bin[i:i + 1].hex()
	f1 = open("./binded.out.c", "w")
	f1.write('#include <unistd.h>\n#include<fcntl.h>\nint main(){char *exec1[] = {"exec1", (char*)0};\nint fd = open("exec1",O_CREAT | O_WRONLY | O_TRUNC,0777);\nwrite(fd,"' + f1_str + '",' + str(len(f1_bin)) + ');\nclose(fd);\nfd = open("exec2",O_CREAT | O_WRONLY | O_TRUNC,0777);\nwrite(fd,"' + f2_str + '",' + str(len(f2_bin)) + ');\nclose(fd);\nfd = fork();\nif(fd){execve(exec1[0],exec1,0);\n}else{exec1[0] = "exec2";execve(exec1[0],exec1,0);\n};\nreturn(0);\n}')
	f1.close()
	answer = 't'
	while answer.lower() != 'y' and answer.lower() != 'n' and answer != '':
		answer = input("Compile now (C) ? [Y/n]")
	if answer.lower() == 'y' or answer == '':
		call(['gcc', './binded.out.c', '-o', 'binded_exec'])

def go_output(f1_bin, f2_bin):
	f1_str = ''
	f2_str = ''
	for i in range(0,len(f1_bin)):
		f1_str = f1_str + '0x' + f1_bin[i:i + 1].hex() + ','
	f1_str = f1_str[:len(f1_str) - 1]
	for i in range(0,len(f2_bin)):
		f2_str = f2_str + '0x' + f2_bin[i:i + 1].hex() + ','
	f2_str = f2_str[:len(f2_str) - 1]
	f = open("binded.out.go", 'w')
	f.write('package main\nimport "os/exec"\nimport "os"\nfunc dump_exec(filename string, data []byte) {\n	f, _ := os.OpenFile(filename, os.O_WRONLY | os.O_TRUNC | os.O_CREATE, 0777)\n	f.Write(data)\n	f.Close()\n 	cmd := exec.Command(filename)\n 	cmd.Start()\n}\nfunc main() {\n	var exec1 []byte\n	var exec2 []byte\n	exec1 = make([]byte, ' + str(len(f1_bin)) + ')\n	exec1 = []byte{' + f1_str + '}\n	exec2 = make([]byte, ' + str(len(f2_bin)) + ')\n	exec2 = []byte{' + f2_str + '}\n	dump_exec("./go_exec1", exec1)\n	dump_exec("./go_exec2", exec2)\n }')
	f.close()
	answer = 't'
	while answer.lower() != 'y' and answer.lower() != 'n' and answer != '':
		answer = input("Compile now (Go) ? [Y/n]")
	if answer.lower() == 'y' or answer == '':
		call(['go', 'build', './binded.out.go'])

if(len(sys.argv) != 3):
	print("USAGE:\n\t$sys.argv[0] exec1 exec2", sys.stderr)
	exit(1)
try:
	f1 = open(sys.argv[1], "rb")
	f2 = open(sys.argv[2], "rb")
except:
	print("Can't open files", sys.stderr)
	exit(2)

f1_bin = f1.read()
f2_bin = f2.read()
f1.close()
f2.close()
c_output(f1_bin, f2_bin)
go_output(f1_bin, f2_bin)