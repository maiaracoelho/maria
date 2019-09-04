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
DSVERIFY_PATH = "/home/maria/dsverifier/./dsverifier"
options = "--property STABILITY_CLOSED_LOOP --bmc ESBMC --realization DFI --connection-mode FEEDBACK --x-size 10 --timeout 518400"
results_output_directory = "newresultados_stability"
home = "/home/maria/"
#DSN = "cruise"


 
def write_results(outfile_path, params):
    
    

def menu():

        os.system("clear")
        print ("===================================")
        print ("======= Extract Results ========")
        print ("===================================")

        config_path = "config.json"
        
        with open(config_path, "r") as arq_config:
                videoset_config = json.load(arq_config)
        arq_config.close()

        plans_path = videoset_config.get("path_plans") 
        home_path = videoset_config.get("path_home") 
        bits = videoset_config.get("bits")
        uncert = videoset_config.get("uncert")
        cases = videoset_config.get("cases")
        output_directory = videoset_config.get("output")

        for case in cases:       
                for bit in bits:
                        for one_uncert in uncert:
                                path_unc = os.path.join(home_path+"/"+str(bit)+"-bits", one_uncert)
                                bits2_list = os.listdir(path_unc)
                        
                                for bit2 in bits2_list:
                                        path_bit2 = os.path.join(home_path+"/"+str(bit)+"-bits/"+one_uncert, bit2)
                    
                                        if os.path.isdir(path_bit2):
                                                one_unc2_list = os.listdir(path_bit2)
                                                print(one_unc2_list)

                                                for one_unc2 in one_unc2_list:
                                                        path_one_unc2 = path_bit2+"/"+ one_unc2
                            
                                                        if os.path.isdir(path_one_unc2):
                                                                arq_input =  path_one_unc2 + "/test-case-"+str(case)+"/"+"input.c"
                                                                arq_output_name = "test-case-"+str(case)+"_SCL_"+bit+"Bits-"+bit2+"-U00_ESBMC_"+directory+"_resultado_21_08.txt
                                                                print(arq_input)
                                                                comand = DSVERIFY_PATH+" "+os.path.join(home, arq_input+" "+options+" > "+   os.path.join(home+"/"+output_directory, arq_output_name)

                               
    
        for directory in directories_list:
            if(directory != ".DS_Store"):
                print("Diretorio: ", directory)           











                directory_path = os.path.join(path+"/"+results_directory, directory)
                
                
                params.append((linha1))
                params.append((linha2))
                

        print("Finish")
            
            
if __name__ == '__main__':
    menu()

try:
        #Execute FFMPEG command SEGMENTER
        probe = subprocess.Popen((ffmpegcmd_segm).split(), stdout=subprocess.PIPE)
        output, err = probe.communicate()
        if not err:
            return True
        print (err)
    except:
        return False
    else:
        return True
    