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
results_directory = "resultados/results_todaslexicais/knn"
outfile_name = "results_todaslexicais_knn.csv"
#DSN = "cruise"

def check(string, file_path):
    inputfileArq=open(file_path,"r")
    lines = inputfileArq.readlines()
    if (string in lines[-1]) or (string in lines[-2]):
            return True
    return False    

def extract_params(file_path):
    inputfileArq=open(file_path,"r")
    lines = inputfileArq.readlines()
    #list_params = lines[0].split("/")
    
    n_neighbors = lines[0].split(":")[1]
    scores_KNN = lines[1].split(":")[1]
    precisao = lines[2].split(":")[1]
    tempo = lines[3].split(":")[1]
    recall = lines[15].split(":")[1]
         
    
    
   
    
    return (n_neighbors, scores_KNN, recall, precisao, tempo)

 
def write_results(outfile_path, params):
    
    with open(outfile_path, mode='a') as out_file:
        file_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        print("n_neighbors, scores_KNN, recall, precisao, tempo")
        file_writer.writerow(["n_neighbors", "scores_KNN", "recall", "precision", "temp"])
        for param in params:
                file_writer.writerow([param[0],param[1],param[2],param[3],param[4]])
                print(param[0],param[1],param[2],param[3],param[4])

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

                #file_list = os.listdir(directory_path)

                #for file_name in file_list:
                #   file_path = os.path.join(path+"/"+results_directory+"/"+directory, file_name)
                #  print("Filename: ", file_name)
                
                n_neighbors, scores_KNN, recall, precisao, tempo  =  extract_params(directory_path)
              

                params.append((n_neighbors, scores_KNN, recall, precisao, tempo))

        outfile_path = os.path.join(path, outfile_name)
        write_results(outfile_path, params)

        print("Finish")
            
            
if __name__ == '__main__':
    menu()
