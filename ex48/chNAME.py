import os
import shutil

def indt(indent):
    return " " * 4 * indent


def changeName(path, oldName, newName, indent):
    
    print indt(indent) + "Looking into " + path
    indent += 1
    
    for fn in os.listdir(path):
        print indt(indent) + "Found " + fn 
        if fn == __file__:
            continue
        elif fn.endswith('.old') or fn.endswith('.pyc'):
            os.remove(os.path.join(path, fn))
            print indt(indent) + "removed useless file " + fn
        else:
            
            # change file name
            if os.path.isdir(fn):
                print indt(indent) + fn + " is a folder!"
                changeName(fn, oldName,newName, indent + 1)
            else:
                #print os.path.join(path, fn)
                #print os.path.join(path, fn + '.old')
                shutil.copyfile(os.path.join(path, fn), os.path.join(path, fn + '.old'))
                with open(os.path.join(path,fn + '.old')) as fold:
                    with open(os.path.join(path, fn), 'w+') as fnew:
                        for line in fold:
                            fnew.write(line.replace(oldName, newName))
                        print indt(indent) + "replaced words in " + fn
                os.remove(os.path.join(path, fn + '.old'))
                
                
            if oldName in fn:
                print indt(indent) + "changing the name of " + fn
                os.rename(os.path.join(path, fn), os.path.join(path, fn.replace(oldName, newName)))
            
ans = raw_input("This script changes names of all the relevant files for a new project. \nHave you preserved your original template? (yes/no): ")
if ans == "yes":
    newName = raw_input("The new name is: ")
    changeName('./', 'NAME',newName,0)
else:
    print "Phew. Close call."