#!/usr/bin/env python3

import argparse
import shutil
import sys
import os

class CONST(object):
	VERSION = "0.3"

#  ---  ---  ---  ---  ---  #

def POSIX_Backup(arg):
	Src  = arg.s
	Dest = arg.d
	
	if not arg.l: 
		BACKUPn = 0
	
		while True:
			BACKUP_DIR = "BACKUP_" + str(BACKUPn)
			FULL_BACKUP_PATH = Dest + "/BACKUP_" + str(BACKUPn)

			if os.path.exists(FULL_BACKUP_PATH):
				BACKUPn += 1
			
			else:
				print("Backup-Tool: Info: Backup into " + str(BACKUP_DIR))
				shutil.copytree(Src, FULL_BACKUP_PATH)
				
				break;
			
		print("Backup-Tool: Info: Backuping complete... ")

	else:		
		BACKUP_DIR = arg.l
		BACKUP_FULL_PATH = Dest + "/" + BACKUP_DIR

		if os.path.exists(BACKUP_FULL_PATH):
			print("Backup-Tool: Error: Dest path is exists")
			
		else:
			print("Backup-Tool: Info: Backup into " + str(BACKUP_DIR))
			shutil.copytree(Src, BACKUP_FULL_PATH)
				
#def NT_BACKUP(arg):
	
#  ---  ---  ---  ---  ---  #

def Backup(arg):
	OS_NAME = os.name

	if OS_NAME == 'posix':
		POSIX_Backup(arg)
	
	elif OS_NAME == 'nt':
		NT_Backup(arg)
	
	else:
		print("Backup-Tool not supported your OS")

#  ---  ---  ---  ---  ---  #

def Main(arg):
	if os.path.exists(arg.s) and os.path.exists(arg.d):
		Backup(arg)
	
	else:
		print("Backup-tool: Error: Src or Dest directories not found")

#  ---  ---  ---  ---  ---  #

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Backup-Tool " + CONST.VERSION)
	
	parser.add_argument("-s", default=None, type=str, help="Source path")
	parser.add_argument("-d", default=None, type=str, help="Dest path")
	parser.add_argument("-l", default=None, type=str, help="Label")

	arg = parser.parse_args()

	if not arg.s or not arg.d:
		print("Backup-tool: Error: Src or Dest directories not found")
		sys.exit()

	else:
		Main(arg)
