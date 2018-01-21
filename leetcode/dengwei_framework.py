#!/usr/bin/python
"""
Generate file for any leetcode question
Fetch the content from leetcode
"""
import sys
import re
import os

class LeetCode:
    # using __init__ for future function updates
    def __init__(self, f):
        self.f = f
    def title(self, num):
        fileList = open(self.f)
        ques_num_dict = {}
        for l in fileList:
            l = l.strip().split("\t")
            par = l[0].split(" ")
            id = par[0]
            title = ""
            tag = 0
            for pars in range(1, len(par)):
                if par[pars] != "" and not re.match(r'(.*)[%\(\)](.*)', par[pars]):
                    title += "_" + par[pars]
                    tag = 1
                if tag == 1 and par[pars] == "":
                    break
            ques_num_dict[id] = id.zfill(4) + title   # add padding 0s
        return ques_num_dict[num]

# check if file exists, do nothing if it does, avoid overwrite
class Framework:
    def __init__(self, name):
        self.name = name
    def cp(self):
        if not os.path.isfile(self.name + ".py"):
            os.system('cp ./.tmp/template.py ' + self.name + '.py')
            print(self.name + ".py generated successfully!")
        else:
            print(self.name + ".py already existed!")

        # if not os.path.isfile("./c++/" + self.name + ".cpp"):
        #     os.system('cp ./.tmp/framework.cpp ./c++/' + self.name + '.cpp')
        #     print self.name + ".cpp generated successfully!"
        # else:
        #     print self.name + ".cpp already existed!"
        

def main():
    if len(sys.argv) < 2:
        print("Usage: python dengwei_framework.py <question_num>")
        exit()
    # Get the name of this question
    L = LeetCode("./.tmp/list")
    # input question number, return fileName
    fileName = L.title(sys.argv[1])
    print("Let's deal with " + fileName)
    # Generate the framework file
    new = Framework(fileName)
    new.cp()


if __name__ == "__main__":
    main()
