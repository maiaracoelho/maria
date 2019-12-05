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
#import sh

path = os.getcwd()
results_directory = "./newStability/8/DFI/bits-1-7/Uncertainty-0.0/test-case-1"
outfile_name = "script_SCL_caso01_8bits_bits-1-7.sh"
#DSN = "cruise"


 
def write_results(outfile_path, params):
    
    with open(outfile_path, mode='a') as out_file:
        file_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        #print("n_estimators, learning_rate, scores_AB, recall, precisao, tempo")
        #file_writer.writerow(["n_estimators", "learning_rate", "scores_AB", "recall", "precision", "temp"])
        for param in params:
                file_writer.writerow([param[0]])
                print(param[0])

    out_file.close()


def menu():

        os.system("clear")
        print ("===================================")
        print ("======= Extract Results ========")
        print ("===================================")

        directories_list = os.listdir(results_directory)
        params = []
        for directory in directories_list:
	        if(directory != ".DS_Store"):	
                print("Diretorio: ", directory)           
                directory_path = os.path.join(path+"/"+results_directory, directory)
                linha1 = "echo \"Result: Bits 8 Real DFI caso 1 bits-1-7 Uncer 0.0 "+directory+"\""
                linha2 = "/home/maria/dsverifier/./dsverifier /home/maria/test-case-1/esbcm/newStability/8/DFI/bits-1-7/Uncertainty-0.0/test-case-1/"+directory+" --property STABILITY_CLOSED_LOOP --bmc ESBMC --realization DFI --connection-mode FEEDBACK --x-size 10 --timeout 518400 > /home/maria/newresultados_stability/case-1_SCL_8Bits-bits-1-7-U00_ESBMC_"+directory+"_resultado_21_08.txt"
                linha3 = ""

                params.append((linha1))
                params.append((linha2))
                params.append((linha3))

        outfile_path = os.path.join(path, outfile_name)
        write_results(outfile_path, params)

        print("Finish")
            
            
if __name__ == '__main__':
    menu()
