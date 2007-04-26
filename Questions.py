# -*- coding: utf8 -*-

import os,sys
import random
import codecs

class Questions:
  """self.question
     A questions collection
     You can get a random question, answers, and right answers
  """
  def __init__(self,dir):
     self.questionfiles=os.listdir(dir)
     self.dir=dir 

  def get_one(self):
    questionfile=""
    while questionfile[0:1] != "q":
      questionfile=random.choice(self.questionfiles)
    try:
      qfile=codecs.open(os.path.join(self.dir,questionfile),"r","utf8")
    except:
      sys.exit("ERROR: can't open question file "+questionfile)
    line=qfile.readline()
    self.question=line.rstrip("\r\n")
    line=qfile.readline()
    self.answer1=line.rstrip("\r\n")
    line=qfile.readline()
    self.answer2=line.rstrip("\r\n")
    line=qfile.readline()
    self.answer3=line.rstrip("\r\n")
    line=qfile.readline()
    self.rightanswer=int(line.rstrip("\r\n"))
    qfile.close
