#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 23:31:15 2019

@author: sturkars
"""
import glob
import sys
import os
import re

# data and results directories
run_dir = "/proj/omics4tb2/Global_Search"
data_dir = "%s/Pilot_Pass/X204SC21081158-Z01-F003/raw_data" %run_dir
data_folders = glob.glob('%s/*' %(data_dir))
data_folders = [element for element in data_folders if element not in ('%s/*/trimmed,%s/*/fastqc_results,%s/*/results_kallisto_Symbiodinium,%s/*/results_kallisto_Stylophora, %s/*/results_kallisto_Spis_Smic')%(data_dir,data_dir,data_dir,data_dir,data_dir)]

jobscripts_dir = "%s/Global_Search_Scripts/Kallisto/jobscripts_Acerv_Smic-reefGenomics_v1" %run_dir
jobscripts_logs = "%s/logs" %jobscripts_dir
# create sample spepcific results directory
if not os.path.exists('%s' %(jobscripts_dir)):
    os.makedirs('%s' %(jobscripts_dir))

if not os.path.exists('%s' %(jobscripts_logs)):
    os.makedirs('%s' %(jobscripts_logs))

folderCount = 1
for data_folder in data_folders:
    folder_name = data_folder.split('/')[-1]
    job_name = folder_name
    jobscript = '%s/%s_Acerv_Smic_reefGenomics_Kallisto_v1.csh' %(jobscripts_dir,folder_name)
    # write to job file
    with open(jobscript,'w') as g:
      g.write('#!/bin/bash\n\n')
      g.write('#$ -N %s\n'%(job_name))
      g.write('#$ -o %s/%s_outlog.txt\n' %(jobscripts_logs,job_name))
      g.write('#$ -e %s/%s_errorlog.txt\n' %(jobscripts_logs,job_name))
      g.write('#$ -pe smp 16\n')
      g.write('#$ -S /bin/bash\n\n')

      g.write('#Sample: %s\n' %(data_folder))

      # changing terminal to bash
      g.write('bash\n\n')
      g.write('source /users/sturkars/.bashrc \n\n')

      # change directory
      g.write('cd %s/Global_Search_Scripts/Kallisto\n\n' %(run_dir))

      job_cmd = 'python run_kallisto_Acerv_Smic-reefGenomics.py %s' %(folder_name)
      print(job_cmd)
      # spades command
      g.write('%s' %(job_cmd))

    g.close()
    folderCount = folderCount + 1

    # submit each job with qsub
    cmd = 'qsub %s' %jobscript
    print(cmd)
    print
    #os.system(cmd)
    #sys.exit()

