# Author: Zhaoyan
# Description: build a document website
# 
import sys,os,shutil
baseDir=os.path.dirname(os.path.realpath(__file__))
templateDir   = baseDir+os.sep+"template"
sourcesDir    = baseDir+os.sep+"source"
outputDir     = baseDir+os.sep+"output"
resourcesDirs = ["css","img","js"]
def clean ():
    print "[info]execute clean"
    if (os.path.exists(outputDir)) :
        print "[info]output dir exists"
        shutil.rmtree(outputDir)
        print "[info]deleting output dir"

def copyDir(src, dest):
    shutil.copytree(src, dest)

def complie(file):
    print file

def walkDir(path):
    for file in os.listdir(path):
        if (os.path.isdir(file)):
            walkDir(file)
        else if (os.path.isfile(file)):
            complie(file)

#remove output dir
clean()

#create output dir
os.mkdir(outputDir)

for resouceDir in resourcesDirs:
    copyDir(baseDir+os.sep+resouceDir, outputDir+os.sep+resouceDir)

walkDir(sourcesDir)


print "[info]end of building"
