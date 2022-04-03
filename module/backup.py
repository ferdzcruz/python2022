from turtle import end_fill
from mainfile import types_of_backup
backup_choice = ["dbexport","daexport","cdexport"]
env = "source"
prodlines = "lmghr"
backup_choice = 1

if backup_choice == 1:
    print(f"{backup_choice[1]}{types_of_backup(env,backup_choice,prodlines)}")
else:
    print("EOF")

