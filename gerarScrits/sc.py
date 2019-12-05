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
import subprocess

DSVERIFY_PATH = "/home/maria/dsverifier/./dsverifier"
options = "--property STABILITY_CLOSED_LOOP --bmc ESBMC --realization DFI --connection-mode FEEDBACK --x-size 10 --timeout 518400"
home = "/home/maria/test-case-nov/esbcm"


def menu():

        os.system("clear")
        print ("===================================")
        print ("======= Generating Results ========")
        print ("===================================")

        config_path = "config_scripts.json"
        
        with open(config_path, "r") as arq_config:
                videoset_config = json.load(arq_config)
        arq_config.close()

        home_path = videoset_config.get("path_home") 
        bits = videoset_config.get("bits")
        uncert = videoset_config.get("uncert")
        cases = videoset_config.get("cases")
        results_output_directory = videoset_config.get("output")

        for case in cases:       
                for bit in bits:
                        for one_uncert in uncert:
                                path_unc = os.path.join(home,home_path+"/"+str(bit)+"/"+str(one_uncert))
                                bits2_list = os.listdir(path_unc)
                        
                                for bit2 in bits2_list:
                                    if bit2 != ".DS-Store":
                                        path_bit2 = os.path.join(path_unc, str(bit2))
                                        # print(path_bit2)
                                    
                                        if os.path.isdir(path_bit2):
                                                one_unc2_list = os.listdir(path_bit2)

                                                for one_unc2 in one_unc2_list:
                                                    
                                                    if one_unc2 != ".DS_Store":
                                                        print(one_unc2)
                                                        path_one_unc2 = path_bit2+"/"+ one_unc2
                                                        input_files_dir =  path_one_unc2 + "/test-case-"+str(case)
                                                        inputs_file_list = os.listdir(input_files_dir)
                                                
                                                        for inputs_file in inputs_file_list:
                                                                print(inputs_file)
                                                                if inputs_file != ".DS_Store":
                                                                        arq_input =  path_one_unc2 + "/test-case-"+str(case)+"/"+inputs_file
                                                                        
                                                                        arq_output_name = "test-case-"+str(case)+"_SCL_"+str(bit)+"Bits-"+str(bit2)+"-"+one_uncert+"_"+inputs_file.split('.')[0]+".txt"
                                                                        print(arq_input)
                                                                        print(arq_output_name)
                                                                        comand = DSVERIFY_PATH+" "+os.path.join(home, arq_input)+" "+options #+" > "+   os.path.join(home+"/"+ results_output_directory, arq_output_name) 
                                                                        print(comand)
                                                                        file = os.path.join(home+"/"+ results_output_directory, arq_output_name)
                                                                        probe = subprocess.Popen((comand).split(), stdout=open(file, 'w', 1))
                                                                        #output = probe.wait()
                                                                        #exitCode = probe.returncode
                                                                        #print(probe.stdout)
                                                                                
                                                                        #if (exitCode == 0):
                                                                        #        print(output)
                                                                        #else:
                                                                        #        print("Process Initiate!")
									


        print("Finish")
            
            
if __name__ == '__main__':
    menu()    