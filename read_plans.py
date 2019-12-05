import numpy as np
import pandas as pd
import os
import json

def main():


    config_path = "config.json"

    with open(config_path, "r") as arq_config:
        videoset_config = json.load(arq_config)
    arq_config.close()

    plans_path = videoset_config.get("path_plans") 
    home_path = videoset_config.get("path_home") 
    bits = videoset_config.get("bits")
    uncert = videoset_config.get("uncert")
    cases = videoset_config.get("cases")
    output = videoset_config.get("output")
    
    if not os.path.exists(output):
        os.mkdir(output)

    for case in cases:       
        
        for bit in bits:
            path_new_bit = os.path.join(output,str(bit))
            if not os.path.exists(path_new_bit):
                os.mkdir(path_new_bit)

            for one_uncert in uncert:
                path_unc = os.path.join(home_path+"/"+str(bit), one_uncert)
                bits2_list = os.listdir(path_unc)
                path_new_unc = os.path.join(path_new_bit, one_uncert)
                if not os.path.exists(path_new_unc):
                    os.mkdir(path_new_unc)
                
                print(bits2_list)
                
                for bit2 in bits2_list:

                    path_bit2 = os.path.join(path_unc, bit2)
                    path_new_bit2 = os.path.join(path_new_unc, bit2)
                    if not os.path.exists(path_new_bit2):
                        os.mkdir(path_new_bit2)
                    
                    if os.path.isdir(path_bit2):
                        one_unc2_list = os.listdir(path_bit2)
                        print(one_unc2_list)

                        for one_unc2 in one_unc2_list:
                        
                            path_one_unc2 = path_bit2+"/"+ one_unc2
                            path_new_unc2 = os.path.join(path_new_bit2, one_unc2)
                            if not os.path.exists(path_new_unc2):
                                os.mkdir(path_new_unc2)

                            if os.path.isdir(path_one_unc2):
                                arq_input =  path_one_unc2 + "/test-case-"+str(case)+"/"+"input.c"
                                arq_plans = plans_path+"/"+ "case_"+str(case)+".csv"
                                print(arq_plans)
                                print(arq_input)

                                with open(arq_plans, "r") as arq_p:
                                    lines_plan = arq_p.readlines()

                                with open(arq_input, "r") as arq_c:
                                    lines_arq = arq_c.readlines()

                                path_new_test = os.path.join(path_new_unc2, "test-case-"+str(case))
                                if not os.path.exists(path_new_test):
                                    os.mkdir(path_new_test)

                                '''a = lines_arq[23]
                                b = lines_arq[20]

                                n_ele_a = a.count(",")
                                n_ele_b = a.count(",")
                                print(n_ele_a, n_ele_b)
                                '''
                                
                                for i in range(1, len(lines_plan)):
                                    arq_output =  path_new_test + "/input-"+str(i)+".c"
                                    arq_o =  open(arq_output, 'w+')

                                    elems = lines_plan[i].split(",")
                                    half = len(elems)/2

                                    for j in range(1, len(lines_arq)):
                                        
                                        line = lines_arq[j]

                                        if(j==20):
                                            #print(lines_arq[j])
                                            line = "\t.b = { "
                                            for elem in range(half, len(elems)):
                                                line += elems[elem]
                                                if(elem != len(elems)-1):
                                                    line += ", "
                                                else:
                                                    line = line.replace("\n", "")
                                            line += " },\n" 

                                        elif(j==23):
                                            #print(lines_arq[j])
                                            line = "\t.a = { "
                                            for elem in range(0, half):
                                                line += elems[elem]
                                                if(elem != half-1):
                                                    line += ", "
                                            line += " },\n"
                                        
                                        print(line)
                                        arq_o.write(line)
                                    
                                    arq_o.close()



    
            
            


if __name__ == '__main__':
	main()
