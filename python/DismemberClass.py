from os import fdopen, remove, listdir, chmod
from tempfile import mkstemp
from shutil import move

class DismemberClass:
    def __init__(self, path, substs ):
        self.path = path
        self.substs = substs
        #print(path)
        #print(type(substs))
        #print(substs)

    def replace(self, file_path, pattern, subst):
        #Create temp file
        fh, abs_path = mkstemp()
        with fdopen(fh,'w') as new_file:
            with open(file_path) as old_file:
                for line in old_file:
                     #print(line)
                     if line.__contains__(pattern):
                         line = subst+"\n"
                     new_file.write(line) #line.replace(pattern, subst)
        #Remove original file
        chmod(file_path, 0o777)
        remove(file_path)
        #Move new file
        move(abs_path, file_path)

    def replaceAll(self):
        #rmdir("D:\StarWars\JediAcademy\\npcs")
        #path="D:\StarWars\JediAcademy\\npcs"
        #path="D:\StarWars\GameData\\base\\assets0.pk3\\npcs"
        path = self.path
        path = path + "/" + "npcs"
        print(path)
        #print(self.substs[0])
        #print(type(self.substs[0]))
        #return
        files =listdir(path)
        print(len(files))

        for file in files:
            print(file)
            #replace(path+"\\"+file,"kura","kuraM")
            self.replace(path + "/" + file, "dismemberProbHead", "dismemberProbHead " + str(self.substs[0]))
            self.replace(path + "/" + file, "dismemberProbArms", "dismemberProbArms " + str(self.substs[1]))
            self.replace(path + "/" + file, "dismemberProbLegs", "dismemberProbLegs " + str(self.substs[2]))
            self.replace(path + "/" + file, "dismemberProbHands", "dismemberProbHands " + str(self.substs[3]))
            self.replace(path + "/" + file, "dismemberProbWaist", "dismemberProbWaist " + str(self.substs[4]))

            """
            try:
                fp = open(path+"\\"+file,'r')
                for line in fp:
                    if "dismemberProbWaist" in line:
                        print(line)
            finally:
                fp.close()
            """
        return

    def hello(self):
        print("hello class!")