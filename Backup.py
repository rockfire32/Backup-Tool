#!/usr/bin/env python3

import argparse
import shutil
import os

class CONST(object):
	VERSION = "0.1"

#  ---  ---  ---  ---  ---  #

def POSIX_Backup(Src, Dest):
	BACKUP_N = 0
	
	BACKUP_DIR = "/BACKUP_" + str(BACKUP_N)
	FULL_BACKUP_DIR = Dest + "/BACKUP_" + str(BACKUP_N)
	
	while True:
		FULL_BACKUP_DIR = Dest + "/BACKUP_" + str(BACKUP_N)
				
		if os.path.exists(FULL_BACKUP_DIR):
			BACKUP_N = BACKUP_N + 1
					
		else:
			print("Backup into: " + FULL_BACKUP_DIR)
			shutil.copytree(Src, FULL_BACKUP_DIR)
					
			break
	
	else:
		print("Backup into: " + FULL_BACKUP_DIR)
		shutil.copytree(Src, FULL_BACKUP_DIR)
	
	print("Backuping complete... ")
				
	return 0;


def NT_BACKUP():
	BACKUP_N = 0
	
	BACKUP_DIR = "\BACKUP_" + str(BACKUP_N)
	FULL_BACKUP_DIR = Dest + "\BACKUP_" + str(BACKUP_N)
	
	while True:
		FULL_BACKUP_DIR = Dest + "\BACKUP_" + str(BACKUP_N)
				
		if os.path.exists(FULL_BACKUP_DIR):
			BACKUP_N = BACKUP_N + 1
					
		else:
			print("Backup into: " + FULL_BACKUP_DIR)
			shutil.copytree(Src, FULL_BACKUP_DIR)
					
			break
	
	else:
		print("Backup into: " + FULL_BACKUP_DIR)
		shutil.copytree(Src, FULL_BACKUP_DIR)
	
	print("Backuping complete... ")
				
	return 0;
	
	
#  ---  ---  ---  ---  ---  #

def Backup(Src, Dest):
	OS_NAME = os.name

	if OS_NAME == 'posix':
		POSIX_Backup(Src, Dest)
	
	elif OS_NAME == 'nt':
		NT_Backup(Src, Dest)
	
	else:
		print("Backup-Tool not supported your OS")

#  ---  ---  ---  ---  ---  #

def Interactive_Main():
	print(" --- Backup Tool " + CONST.VERSION + " --- ")
	
	Path      = input("Enter the full path of the directory to backup: ")
	BackupDir = input("Enter the full path of the dest directory: ")
	
	if os.path.exists(Path) and os.path.exists(BackupDir) == True:
		
		Answer = input("Backup files? [y/n]: ")
		if Answer.lower() == "y":
			Backup(Path, BackupDir)
			
	else:
		print("Error: Directory not found")
	
	return 0


def Main(Src, Dest):
	if os.path.exists(Src) and os.path.exists(Dest) == True:
		Backup(Src, Dest)
	else:
		print("Path not found")
	
	return 0

#  ---  ---  ---  ---  ---  #

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Backup-Tool" + CONST.VERSION)
	
	parser.add_argument("-s", default="None", type=str, help="Source path")
	parser.add_argument("-d", default="None", type=str, help="Dest path")
	
	arg = parser.parse_args()
	
	if arg.s == "None" or arg.d == "None":
		Interactive_Main()
	else:
		Main(arg.s, arg.d)
