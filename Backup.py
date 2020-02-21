#!/usr/bin/env python3

import shutil
import os

def Backup(Tree, Dest):
	print("Backuping... ")
	
	for Branch in Tree:
			for File in Branch[2]:
				shutil.copy(str(Branch[0]) + "/" + str(File), Dest)
	
	print("Backuping complete... ")
				
	return 0;

#  ---  ---  ---  ---  ---  #

def Main():
	print(" --- Backup Tool --- ")
	print(" --- Warning: Doesn't save files path --- ")
	
	Path      = input("Enter the full path of the directory to backup: ")
	BackupDir = input("Enter the full path of the dest directory: ")
	
	if os.path.exists(Path) and os.path.exists(BackupDir) == True:
		Tree = os.walk(Path)
		
		Answer = input("Backup files? [y/n]: ")
		if Answer.lower() == "y":
			Backup(Tree, BackupDir)
			
	else:
		print("Error: Directory not found")
	
	return 0

#  ---  ---  ---  ---  ---  #

if __name__ == "__main__":
	if os.name == "posix":
		Main()
	else:
		print("Script supported only POSIX OS")
