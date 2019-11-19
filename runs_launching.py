import os


f_sum = open("README", "w")

os.mkdir("runs")

i = 0
while i<18:

    if int(i/6) == 0:

        if not os.path.exists("runs/h2o"):
            os.mkdir("runs/h2o")

        job_str = """#!/bin/bash
        #SBATCH -t 5:00:00
        #SBATCH -o out.txt
        cd $WORK/gaussian/runs/h2o/"""+str(i%6)

        with open("coords/h2o.coords", "r") as myfile:
            h2o_coords = myfile.read()

        if i%6 == 0:
            job_str += """\n #p HF/6-31G opt \n \nh2o_HF \n\n0 1\n""" + h2o_coords + "\n! RW"
        if i%6 == 1:
            job_str += """\n #p MP2/6-31G opt \n\nh2o_MP2 \n\n0 1\n""" + h2o_coords + "\n! RW"
        if i%6 == 2:
            job_str += """\n #p CCSD/6-31G opt \n\nh2o_CCSD \n\n0 1\n""" + h2o_coords + "\n! RW"
        if i%6 == 3:
            job_str += """\n #p B3LYP/6-31G opt \n\nh2o_B3LYP \n\n0 1\n""" + h2o_coords + "\n! RW"
        if i%6 == 4:
            job_str += """\n #p AM1/6-31G opt \n\nh2o_AM1 \n\n0 1\n""" + h2o_coords + "\n! RW"
        if i%6 == 5:
            job_str += """\n #p MNDO/6-31G opt \n\nh2o_MNDO \n\n0 1\n""" + h2o_coords + "\n! RW"

        os.mkdir("runs/h2o/" + str(i%6))

        job_path = "runs/h2o/" + str(i%6) + "/" + str(i%6) + ".sh"

        f = open(job_path, "w")
        f.write(job_str)
        f.close()

        f_sum.write("sbatch " + job_path + "\n")

    if int(i/6) == 1:

        if not os.path.exists("runs/ethane"):
            os.mkdir("runs/ethane")

        job_str = """#!/bin/bash
                #SBATCH -t 5:00:00
                #SBATCH -o out.txt
                cd $WORK/gaussian/runs/ethane/""" + str(i%6)

        with open("coords/ethane.coords", "r") as myfile:
            ethane_coords = myfile.read()

        if i%6 == 0:
            job_str += """\n #p HF/6-31G opt \n\nethane_HF \n\n0 1\n""" + ethane_coords + "\n! RW"
        if i%6 == 1:
            job_str += """\n #p MP2/6-31G opt \n\nethane_MP2 \n\n0 1\n""" + ethane_coords + "\n! RW"
        if i%6 == 2:
            job_str += """\n #p CCSD/6-31G opt \n\nethane_CCSD \n\n0 1\n""" + ethane_coords + "\n! RW"
        if i%6 == 3:
            job_str += """\n #p B3LYP/6-31G opt \n\nethane_B3LYP \n\n0 1\n""" + ethane_coords + "\n! RW"
        if i%6 == 4:
            job_str += """\n #p AM1/6-31G opt \n\nethane_AM1 \n\n0 1\n""" + ethane_coords + "\n! RW"
        if i%6 == 5:
            job_str += """\n #p MNDO/6-31G opt \n\nethane_MNDO \n\n0 1\n""" + ethane_coords + "\n! RW"

        os.mkdir("runs/ethane/" + str(i%6))

        job_path = "runs/ethane/" + str(i%6) + "/" + str(i%6) + ".sh"

        f = open(job_path, "w")
        f.write(job_str)
        f.close()

        f_sum.write("sbatch " + job_path + "\n")

    if int(i/6) == 2:

        if not os.path.exists("runs/NiCO4"):
            os.mkdir("runs/NiCO4")

        job_str = """#!/bin/bash
                        #SBATCH -t 5:00:00
                        #SBATCH -o out.txt
                        cd $WORK/gaussian/runs/NiCO4/""" + str(i%6)

        with open("coords/NiCO4.coords", "r") as myfile:
            NiCO4_coords = myfile.read()

        if i%6 == 0:
            job_str += """\n #p HF/6-31G opt \n\nNiCO4_HF \n\n0 1\n""" + NiCO4_coords + "\n! RW"
        if i%6 == 1:
            job_str += """\n #p MP2/6-31G opt \n\nNiCO4_MP2 \n\n 0 1\n""" + NiCO4_coords + "\n! RW"
        if i%6 == 2:
            job_str += """\n #p CCSD/6-31G opt \n\nNiCO4_CCSD \n\n0 1\n""" + NiCO4_coords + "\n! RW"
        if i%6 == 3:
            job_str += """\n #p B3LYP/6-31G opt \n\nNiCO4_B3LYP \n\n0 1\n""" + NiCO4_coords + "\n! RW"
        if i%6 == 4:
            job_str += """\n #p AM1/6-31G opt \n\nNiCO4_AM1 \n\n0 1\n""" + NiCO4_coords + "\n! RW"
        if i%6 == 5:
            job_str += """\n #p MNDO/6-31G opt \n\nNiCO4_MNDO \n\n0 1\n""" + NiCO4_coords + "\n! RW"

        os.mkdir("runs/NiCO4/" + str(i%6))

        job_path = "runs/NiCO4/" + str(i%6) + "/" + str(i%6) + ".sh"

        f = open(job_path, "w")
        f.write(job_str)
        f.close()

        f_sum.write("sbatch " + job_path + "\n")

    i +=1

f_sum.close()







