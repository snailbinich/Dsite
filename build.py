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
#calculate how many char in string
def calculateNums(string, char):
    num = 0;
    for c in string :
       if char == c :
           num = num +1
    return num

def getBaseUrlByNums(num):
    result = ""
    if (num == 1) :
        return "./" 
    for i in range(1, num):
        result += "../"
    return result

def copyDir(src, dest):
    shutil.copytree(src, dest)

def complie(file, templatename):
    print "[info] compiling file :"+file
    targetFile = file.replace(sourcesDir, outputDir).replace(".md",".html")
    targetFileParentDir = os.path.dirname(targetFile)
    baseUrl = getBaseUrlByNums(calculateNums(file.replace(sourcesDir,""), os.sep))
    if not os.path.exists(os.path.dirname(targetFile)):
        os.mkdir(targetFileParentDir)
    cmd = "pandoc -s --template="+templateDir+os.sep + templatename
    cmd += " -V baseUrl="+baseUrl
    cmd += " -o "+targetFile+" "+file
    print "[info] calling command : "+cmd
    os.system(cmd)

def walkDir(path):
    print "[info] walking dir "+path
    defaultTemplate = "template.html"
    if (os.path.exists(path+os.sep+"template")):
        f = open(path+os.sep+"template", 'r')
        #defaultTemplate = 
        defaultTemplate =  f.readline()
        f.close()
    for file in os.listdir(path):
        fullPath = path+os.sep+file
        if (os.path.isdir(fullPath)):
            walkDir(fullPath)
        elif (os.path.isfile(fullPath)):
            complie(fullPath, defaultTemplate)

#remove output dir
clean()

#create output dir
os.mkdir(outputDir)

for resouceDir in resourcesDirs:
    copyDir(baseDir+os.sep+resouceDir, outputDir+os.sep+resouceDir)

walkDir(sourcesDir)


print "[info]end of building"
