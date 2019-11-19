#!/bin/bash
        #SBATCH -t 5:00:00
        #SBATCH -o out.txt
        cd $WORK/gaussian/runs/h2o/0
 #p HF/6-31G opt 
 
h2o_HF 

0 1
O       -0.464  0.177   0.0                                                          
H       -0.464  1.137   0.0                                                          
H        0.441 -0.143   0.0  

! RW