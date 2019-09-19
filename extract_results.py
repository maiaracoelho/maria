# -*- coding: utf-8 -*-
import time
import os
import sys
import string
import math
from datetime import datetime, timedelta
from operator import itemgetter
import json
import csv

path = os.getcwd()
results_directory = "newresultados_stability01"
outfile_name = "newresultados_stability.csv"
DSN = "cruise"

def check(string, file_path):
    inputfileArq=open(file_path,"r")
    lines = inputfileArq.readlines()
    if (string in lines[-1]) or (string in lines[-2]):
            return True
    return False    

def extract_params(file_path):
    inputfileArq=open(file_path,"r")
    lines = inputfileArq.readlines()
    list_params = lines[3].split("/")
    
    bit = list_params[6]
    int_fact = list_params[8].split("-")[1]
    frac_fact = list_params[8].split("-")[2]
    realization = list_params[7]
    unc = list_params[9].split("-")[1]
    input = (list_params[11].split(".")[0]).split("-")[1]


    
    return (int_fact, frac_fact, bit, realization, unc, input)

 
def write_results(outfile_path, params):
    
    with open(outfile_path, mode='a') as out_file:
        file_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        print("int_fact,frac_fact,bit,realization,unc,classify","input")
        file_writer.writerow(["Digital_System_Name_(original_name)","Implementation_Integer_bits(i)","Implementation_fractional_bits(j)","Bit","Realization","Uncertainty", "Class", "Input"])
        for param in params:
                file_writer.writerow([DSN,param[0],param[1],param[2],param[3],param[4],param[5],param[6]])
                print(param[0],param[1],param[2],param[3],param[4],param[5],param[6])

    out_file.close()


def menu():
	
	os.system("clear")
	print ("===================================")
	print ("======= Extract Results ========")
	print ("===================================")

	directories_list = os.listdir(results_directory)
	params = []
	for directory in directories_list:
		file_list=[]
		
		if (directory != ".DS_Store"):
			print("Diretorio1: ", directory)
			directory_path = os.path.join(path+"/"+results_directory, directory)

			file_list = os.listdir(directory_path)

			for file_name in file_list:
				if (file_name != ".DS_Store"):
					file_path = os.path.join(path+"/"+results_directory+"/"+directory, file_name)
					print("Filename: ", file_name)
					int_fact, frac_fact, bit, realization, unc, input  =  extract_params(file_path)
					classify = "" 

					if check("SUCCESSFUL", file_path):
						classify = "Success"
					elif check("FAILED", file_path):
						classify = "Fail"
					elif check("Timed out", file_path):
						classify = "Timeout" 
			
					params.append((int_fact,frac_fact,bit,realization,unc,classify,input))
			outfile_path = os.path.join(path+"/"+results_directory+"/"+directory, outfile_name)
			write_results(outfile_path, params)

	print("Finish")
            
            
if __name__ == '__main__':
    menu()
