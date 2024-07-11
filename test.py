from pathlib import Path as P

test = r'C:\Users\Kulilits\Documents\Maco\Test Fol 1\Health Q1 PT pics\F\New folder'

for i in  P(test).iterdir():
    print(i.name)