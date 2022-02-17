from asyncio import subprocess
import discord
import os
import subprocess

def dc(expression):
    dcFilepath = "C:\\Program Files (x86)\\GnuWin32\\bin"
    tempdcFilepath = os.getcwd()+"\\tempdc.txt"
    expression = '"'+expression+'"'
    dcFilepath = '"'+dcFilepath+"\\dc.exe"+'"'+" -e "
    command = '"'+dcFilepath+expression+" > "+'"'+tempdcFilepath+'"'+'"'
    command = os.path.normcase(command)
    print(command)
    os.system(command)
    f = open(tempdcFilepath, "r")
    output = f.read()
    f.close()
    os.remove(tempdcFilepath)
    return output
    #return subprocess.check_output([command])
    