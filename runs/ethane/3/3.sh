#!/bin/bash
                #SBATCH -t 5:00:00
                #SBATCH -o out.txt
                cd $WORK/gaussian/runs/ethane/3
 #p B3LYP/6-31G opt 

ethane_B3LYP 

0 1
C1  0.00   0.00   0.00
C2  0.00   0.00   1.52
H   1.02   0.00  -0.39
H  -0.51  -0.88  -0.39
H  -0.51   0.88  -0.39
H  -1.02   0.00   1.92
H   0.51  -0.88   1.92
H   0.51   0.88   1.92

! RW