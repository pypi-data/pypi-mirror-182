from pwn import shellcraft,context,log,sleep,make_elf,asm
import os
from colorama import Fore,Back,Style
from . import my_package
import string

chars = string.ascii_letters
'''
add 12.22 
mipsel_shell_cmd
mips_shell_cmd
armelv5_shell_cmd
'''

def mipsel_shell_cmd(cmd,cmd_whole_path ,filename=None):
	context.arch='mips'
	context.endian='little'
	context.bits="32"
	log.success("CMD is  "+ cmd)
	cmd = cmd.split(" ")
	for i in range(len(cmd)):
		cmd[i] = cmd[i] + "\x00"
	shellcode = shellcraft.execve(cmd_whole_path,cmd,0)
	shellcode = asm(shellcode)
	ELF_data=make_elf(shellcode)
	if filename==None:
		log.info("waiting 3s")
		sleep(1)
		filename=context.arch + "-cmd-" + my_package.random_string_generator(4,chars)
		f=open(filename,"wb")
		f.write(ELF_data)
		f.close()
		os.chmod(filename, 0o755)
		log.success("{} is ok in current path ./".format(filename))
		context.arch='i386'
		context.bits="32"
		context.endian="little"
		return 
	else:
		if(os.path.exists(filename) != True):
			log.info("waiting 3s")
			sleep(1)
			f=open(filename,"wb")
			f.write(ELF_data)
			f.close()
			os.chmod(filename, 0o755)
			log.success("{} generated successfully".format(filename))
			context.arch='i386'
			context.bits="32"
			context.endian="little"
			return 
		else:
			print(Fore.RED+"[+]"+" be careful File existence may overwrite the file (y/n) ",end='')
			choise = input()
			if choise == "y\n" or choise == "\n":
				log.info("waiting 3s")
				sleep(1)
				f=open(filename,"wb")
				f.write(ELF_data)
				f.close()
				os.chmod(filename, 0o755)
				log.success("{} generated successfully".format(filename))
				context.arch='i386'
				context.bits="32"
				context.endian="little"
				return 
			else:
				return 


def mips_shell_cmd(cmd, cmd_whole_path,filename=None):
	context.arch='mips'
	context.endian='big'
	context.bits="32"
	log.success("CMD is  "+ cmd)
	cmd = cmd.split(" ")
	for i in range(len(cmd)):
		cmd[i] = cmd[i] + "\x00"
	shellcode = shellcraft.execve(cmd_whole_path,cmd,0)
	shellcode = asm(shellcode)
	ELF_data=make_elf(shellcode)
	if filename==None:
		log.info("waiting 3s")
		sleep(1)
		filename=context.arch + "-cmd-" + my_package.random_string_generator(4,chars)
		f=open(filename,"wb")
		f.write(ELF_data)
		f.close()
		log.success("{} is ok in current path ./".format(filename))
		os.chmod(filename, 0o755)
		context.arch='i386'
		context.bits="32"
		context.endian="little"
		return 
	else:
		if(os.path.exists(filename) != True):
			log.info("waiting 3s")
			sleep(1)
			f=open(filename,"wb")
			f.write(ELF_data)
			f.close()
			os.chmod(filename, 0o755)
			log.success("{} generated successfully".format(filename))
			context.arch='i386'
			context.bits="32"
			context.endian="little"
			return 
		else:
			print(Fore.RED+"[+]"+" be careful File existence may overwrite the file (y/n) ",end='')
			choise = input()
			if choise == "y\n" or choise == "\n":
				log.info("waiting 3s")
				sleep(1)
				f=open(filename,"wb")
				f.write(ELF_data)
				f.close()
				os.chmod(filename, 0o755)
				log.success("{} generated successfully".format(filename))
				context.arch='i386'
				context.bits="32"
				context.endian="little"
				return 
			else:
				return 

def armelv5_shell_cmd(cmd,cmd_whole_path ,filename=None):
	context.arch = 'arm'
	context.endian = 'little'
	context.bits = '32'
	log.success("CMD: "+cmd)
	data_shellcode = ''
	text_shellcode = ''
	cmd_list = cmd.split(" ")[::-1]
	#cmd_list = cmd_list.reverse()
	for i in range(len(cmd_list)):
		data_shellcode += "	cmd%d: .ascii \"%s\\x00\"\n"%(i, cmd_list[i])
		text_shellcode += "	ldr r2, =cmd%d\n		push {r2}\n"%(i)
	shellcode_data = """
.section .data
.section .text
.data
spawn: .ascii "%s\\x00"
	"""
	shellcode_data = shellcode_data%(cmd_whole_path)
	shellcode_data += data_shellcode
	shellcode_text = '''
.text
.global _start
_start:
	.ARM
		add	r3, pc, #1
		bx	r3
	.THUMB
		ldr r0, =spawn
		eor     r3, r3
		push  {r3}
	'''
	shellcode_text += text_shellcode
	shellcode_text += '''
		eor r2, r2
		mov r1, sp
		mov r7, #11
		svc #1
	'''
	shellcode = shellcode_data + shellcode_text
	#print(shellcode)
	#ith open("2.s",'w') as f:
	#	f.write(shellcode)
	if(filename == None ):
		log.info("waiting 3s")
		sleep(1)
		filename = my_package.my_make_elf(shellcode, filename)
		log.success("{} is ok in current path ./".format(filename))
		context.arch='i386'
		context.bits="32"
		context.endian="little"
	else:
		if(os.path.exists(filename) != True):
			log.info("waiting 3s")
			sleep(1)
			my_package.my_make_elf(shellcode, filename)
			log.success("{} generated successfully".format(filename))
			context.arch='i386'
			context.bits="32"
			context.endian="little"
			return 
		else:
			print(Fore.RED+"[+]"+" be careful File existence may overwrite the file (y/n) ",end='')
			choise = input()
			if choise == "y\n" or choise == "\n":
				log.info("waiting 3s")
				sleep(1)
				my_package.my_make_elf(shellcode, filename)
				log.success("{} generated successfully".format(filename))
				context.arch='i386'
				context.bits="32"
				context.endian="little"
				return 
			else:
				return

def armebv5_shell_cmd(cmd, cmd_whole_path, filename):
	context.arch = 'arm'
	context.endian = 'big'
	context.bits = '32'
	log.success("CMD: "+cmd)
	data_shellcode = ''
	text_shellcode = ''
	cmd_list = cmd.split(" ")[::-1]
	#cmd_list = cmd_list.reverse()
	for i in range(len(cmd_list)):
		data_shellcode += "	cmd%d: .ascii \"%s\\x00\"\n"%(i, cmd_list[i])
		text_shellcode += "	ldr r2, =cmd%d\n		push {r2}\n"%(i)
	shellcode_data = """
.section .data
.section .text
.data
spawn: .ascii "%s\\x00"
	"""
	shellcode_data = shellcode_data%(cmd_whole_path)
	shellcode_data += data_shellcode
	shellcode_text = '''
.text
.global _start
_start:
	.ARM
		add	r3, pc, #1
		bx	r3
	.THUMB
		ldr r0, =spawn
		eor     r3, r3
		push  {r3}
	'''
	shellcode_text += text_shellcode
	shellcode_text += '''
		eor r2, r2
		mov r1, sp
		mov r7, #11
		svc #1
	'''
	shellcode = shellcode_data + shellcode_text
	#print(shellcode)
	#ith open("2.s",'w') as f:
	#	f.write(shellcode)
	if(filename == None ):
		log.info("waiting 3s")
		sleep(1)
		filename = my_package.my_make_elf(shellcode, filename)
		log.success("{} is ok in current path ./".format(filename))
		context.arch='i386'
		context.bits="32"
		context.endian="little"
	else:
		if(os.path.exists(filename) != True):
			log.info("waiting 3s")
			sleep(1)
			my_package.my_make_elf(shellcode, filename)
			log.success("{} generated successfully".format(filename))
			context.arch='i386'
			context.bits="32"
			context.endian="little"
			return 
		else:
			print(Fore.RED+"[+]"+" be careful File existence may overwrite the file (y/n) ",end='')
			choise = input()
			if choise == "y\n" or choise == "\n":
				log.info("waiting 3s")
				sleep(1)
				my_package.my_make_elf(shellcode, filename)
				log.success("{} generated successfully".format(filename))
				context.arch='i386'
				context.bits="32"
				context.endian="little"
				return 
			else:
				return


def armelv7_shell_cmd(cmd, cmd_whole_path, filename):
	context.arch = 'arm'
	context.endian = 'little'
	context.bits = '32'
	log.success("CMD: "+cmd)
	data_shellcode = ''
	text_shellcode = ''
	cmd_list = cmd.split(" ")
	#cmd_list = cmd_list.reverse()
	shellcode = shellcraft.execve(cmd_whole_path, cmd_list, 0)
	shellcode = asm(shellcode)
	ELF_data=make_elf(shellcode)
	if filename==None:
		log.info("waiting 3s")
		sleep(1)
		filename=context.arch + "-cmd-" + my_package.random_string_generator(4,chars)
		f.write(ELF_data)
		f.close()
		os.chmod(filename, 0o755)
		log.success("{} is ok in current path ./".format(filename))
		context.arch='i386'
		context.bits="32"
		context.endian="little"
		return 
	else:
		if(os.path.exists(filename) != True):
			log.info("waiting 3s")
			sleep(1)
			f=open(filename,"wb")
			f.write(ELF_data)
			f.close()
			os.chmod(filename, 0o755)
			log.success("{} generated successfully".format(filename))
			context.arch='i386'
			context.bits="32"
			context.endian="little"
			return 
		else:
			print(Fore.RED+"[+]"+" be careful File existence may overwrite the file (y/n) ",end='')
			choise = input()
			if choise == "y\n" or choise == "\n":
				log.info("waiting 3s")
				sleep(1)
				f=open(filename,"wb")
				f.write(ELF_data)
				f.close()
				os.chmod(filename, 0o755)
				log.success("{} generated successfully".format(filename))
				context.arch='i386'
				context.bits="32"
				context.endian="little"
				return 
			else:
				return 

def armebv7_cmd_file(cmd, cmd_whole_path, filename):
	context.arch = 'arm'
	context.endian = 'big'
	context.bits = '32'
	log.success("CMD: "+cmd)
	data_shellcode = ''
	text_shellcode = ''
	cmd_list = cmd.split(" ")
	shellcode = shellcraft.execve(cmd_whole_path, cmd_list, 0)
	shellcode = asm(shellcode)
	ELF_data=make_elf(shellcode)
	if filename==None:
		log.info("waiting 3s")
		sleep(1)
		filename=context.arch + "-cmd-" + my_package.random_string_generator(4,chars)
		f=open(filename,"wb")
		f.write(ELF_data)
		f.close()
		os.chmod(filename, 0o755)
		log.success("{} is ok in current path ./".format(filename))
		context.arch='i386'
		context.bits="32"
		context.endian="little"
		return 
	else:
		if(os.path.exists(filename) != True):
			log.info("waiting 3s")
			sleep(1)
			f=open(filename,"wb")
			f.write(ELF_data)
			f.close()
			os.chmod(filename, 0o755)
			log.success("{} generated successfully".format(filename))
			context.arch='i386'
			context.bits="32"
			context.endian="little"
			return 
		else:
			print(Fore.RED+"[+]"+" be careful File existence may overwrite the file (y/n) ",end='')
			choise = input()
			if choise == "y\n" or choise == "\n":
				log.info("waiting 3s")
				sleep(1)
				f=open(filename,"wb")
				f.write(ELF_data)
				f.close()
				os.chmod(filename, 0o755)
				log.success("{} generated successfully".format(filename))
				context.arch='i386'
				context.bits="32"
				context.endian="little"
				return 
			else:
				return 
'''
mips64,mips64el,cmdfile 2022.12.23 add by doudoudedi
'''



def mips64_cmd_file(cmd, cmd_whole_path, filename):
	context.arch = 'mips64'
	context.endian = 'big'
	context.bits = '64'
	log.success("CMD: "+cmd)
	data_shellcode = ''
	text_shellcode = ''
	cmd_list = cmd.split(" ")
	#cmd_list = cmd_list.reverse()
	num = 1
	for i in range(len(cmd_list)):
		data_shellcode += "cmd%d: .ascii \"%s\\x00\"\n"%(i, cmd_list[i])
		text_shellcode += "dla $t3, cmd%d\nsd $t3,+%d($sp)\n"%(i, num*8)
		num = num+1
	shellcode_data = """
.section .data
.section .text
.data
spawn: .ascii "%s\\x00"
	"""
	shellcode_data = shellcode_data%(cmd_whole_path)
	shellcode_data += data_shellcode
	shellcode_text = '''
.text
.global __start
__start:
dla $a0, spawn
'''
	shellcode_text += text_shellcode
	shellcode_text += '''
xor $t3, $t3, $t3
sd  $t3, +%d($sp)
daddiu $a1,$sp,8
xor $a2, $a2, $a2
li $v0, 0x13c1
syscall 0x40404
	'''%(num*8)
	#print(shellcode_text)
	shellcode = shellcode_data + shellcode_text
	if(filename == None ):
		log.info("waiting 3s")
		sleep(1)
		filename = my_package.my_make_elf(shellcode, filename)
		log.success("{} is ok in current path ./".format(filename))
		context.arch='i386'
		context.bits="32"
		context.endian="little"
	else:
		if(os.path.exists(filename) != True):
			log.info("waiting 3s")
			sleep(1)
			my_package.my_make_elf(shellcode, filename)
			log.success("{} generated successfully".format(filename))
			context.arch='i386'
			context.bits="32"
			context.endian="little"
			return 
		else:
			print(Fore.RED+"[+]"+" be careful File existence may overwrite the file (y/n) ",end='')
			choise = input()
			if choise == "y\n" or choise == "\n":
				log.info("waiting 3s")
				sleep(1)
				my_package.my_make_elf(shellcode, filename)
				log.success("{} generated successfully".format(filename))
				context.arch='i386'
				context.bits="32"
				context.endian="little"
				return 
			else:
				return


def mips64el_cmd_file(cmd, cmd_whole_path, filename):
	context.arch = 'mips64'
	context.endian = 'little'
	context.bits = '64'
	log.success("CMD: "+cmd)
	data_shellcode = ''
	text_shellcode = ''
	cmd_list = cmd.split(" ")
	#cmd_list = cmd_list.reverse()
	num = 1
	for i in range(len(cmd_list)):
		data_shellcode += "cmd%d: .ascii \"%s\\x00\"\n"%(i, cmd_list[i])
		text_shellcode += "dla $t3, cmd%d\nsd $t3,+%d($sp)\n"%(i, num*8)
		num = num+1
	shellcode_data = """
.section .data
.section .text
.data
spawn: .ascii "%s\\x00"
	"""
	shellcode_data = shellcode_data%(cmd_whole_path)
	shellcode_data += data_shellcode
	shellcode_text = '''
.text
.global __start
__start:
dla $a0, spawn
'''
	shellcode_text += text_shellcode
	shellcode_text += '''
xor $t3, $t3, $t3
sd  $t3, +%d($sp)
daddiu $a1,$sp,8
xor $a2, $a2, $a2
li $v0, 0x13c1
syscall 0x40404
	'''%(num*8)
	#print(shellcode_text)
	shellcode = shellcode_data + shellcode_text
	if(filename == None ):
		log.info("waiting 3s")
		sleep(1)
		filename = my_package.my_make_elf(shellcode, filename)
		log.success("{} is ok in current path ./".format())
		context.arch='i386'
		context.bits="32"
		context.endian="little"
	else:
		if(os.path.exists(filename) != True):
			log.info("waiting 3s")
			sleep(1)
			filename = my_package.my_make_elf(shellcode, filename)
			log.success("{} generated successfully".format(filename))
			context.arch='i386'
			context.bits="32"
			context.endian="little"
			return 
		else:
			print(Fore.RED+"[+]"+" be careful File existence may overwrite the file (y/n) ",end='')
			choise = input()
			if choise == "y\n" or choise == "\n":
				log.info("waiting 3s")
				sleep(1)
				filename = my_package.my_make_elf(shellcode, filename)
				log.success("{} generated successfully".format(filename))
				context.arch='i386'
				context.bits="32"
				context.endian="little"
				return 
			else:
				return