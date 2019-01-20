from django.shortcuts import render
import os
from django.conf import settings
from re import *
import json

def home(request):
	AnthList = []
	with open("Anthfa18", "r") as f:
		for line in f:
			CourseName = search("(\w*[A-Z])\s(\d*[0-9])\s-\s\D*\t", line)
			CourseNum = search("(\w*[A-Z])\s(\d*[0-9])",line)
			Year = search("(\w*[A-Z]\d*[0-9])", line)
			Prof = search("((\D*)([,])\D*\t)", line)
			AGE = search("([A-F][(+)-]{0,1}\s\()", line)
			Perc = search("\s\d*\s\d*\s", line)
			agelist = []
			proflist = []
			perclist = []
			courselist = []
			ageStr = ""
			profStr = ""

			courseStr = ""
			try:
				courselist = list(CourseName.group(0))
				agelist = list(AGE.group(0))
				if(agelist[1] == '+' or agelist[1] == '-'):
					ageStr = agelist[0]+agelist[1]
				else:
					ageStr = agelist[0]
				proflist = list(Prof.group(0))
				perclist = list(Perc.group(0))
			except:
				print("Cannot find AGE")
			count = 0
			for aName in courselist:
				if (count >= 0 and count < len(courselist) - 1):
					courseStr = courseStr + aName
				count = count + 1
				profC = 0

			for aChar in proflist:
				if (profC >= 0 and profC < len(proflist) - 1):
					profStr = profStr + aChar
				profC = profC + 1

			num1s = ""
			num2s = ""
			isFirst = 0
			for aChar in perclist:
				if (aChar == "\t"):
					isFirst = isFirst + 1
					continue
				elif (isFirst == 1):
					num1s = num1s + aChar
				elif (isFirst == 2):
					num2s = num2s + aChar
				else:
					break

			num1 = ""
			num2 = ""
			num3 = ""
			if(len(num1s) != 0):
				num1 = int(num1s)
			if(len(num2s) != 0):
				num2 = int(num2s)
			if(len(num1s) != 0 and len(num2s) != 0):
				num3 = round((float(num2/num1)*100),2)
			try:
				AnthList.append({"CourseName":courseStr,"CN":CourseNum.group(0), "Professor":profStr, "Year":Year.group(0), "AGE":ageStr, "PE":str(num3)+"%"})
			except:
				print("Error appending! for: " + line)
	return render(request,"home.html", {'list':AnthList})


def page1(request):
	AnthList = []
	with open("Anthfa18", "r") as f:
		for line in f:
			CourseNum = search("(\w*[A-Z])\s(\d*[0-9])",line)
			Year = search("(\w*[A-Z]\d*[0-9])", line)
			Prof = search("((\D*)([,])\D*\t)", line)
			AGE = search("([A-F][(+)-]{0,1}\s\()", line)
			Perc = search("\s\d*\s\d*\s", line)
			agelist = []
			proflist = []
			perclist = []

			ageStr = ""
			profStr = ""
			try:
				agelist = list(AGE.group(0))
				if(agelist[1] == '+' or agelist[1] == '-'):
					ageStr = agelist[0]+agelist[1]
				else:
					ageStr = agelist[0]
				proflist = list(Prof.group(0))
				perclist = list(Perc.group(0))
			except:
				print("Cannot find AGE")

			profC = 0

			for aChar in proflist:
				if (profC >= 0 and profC < len(proflist) - 1):
					profStr = profStr + aChar
				profC = profC + 1

			num1s = ""
			num2s = ""
			isFirst = 0
			for aChar in perclist:
				if (aChar == "\t"):
					isFirst = isFirst + 1
					continue
				elif (isFirst == 1):
					num1s = num1s + aChar
				elif (isFirst == 2):
					num2s = num2s + aChar
				else:
					break

			num1 = ""
			num2 = ""
			num3 = ""
			if(len(num1s) != 0):
				num1 = int(num1s)
			if(len(num2s) != 0):
				num2 = int(num2s)
			if(len(num1s) != 0 and len(num2s) != 0):
				num3 = round((float(num2/num1)*100),2)
			try:
				AnthList.append({"Professor":profStr, "Year":Year.group(0), "AGE":ageStr, "PE":str(num3)+"%"})
			except:
				print("Error appending! for: " + line)

	return render(request,"page1.html", {'key':AnthList})