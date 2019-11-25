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
cd $WORK/gaussian/runs/h2o/"""+str(i%6) +"\n"

        with open("h2o.coords", "r") as myfile:
            h2o_coords = myfile.read()

        os.mkdir("runs/h2o/" + str(i % 6))

        job_path = "runs/h2o/" + str(i%6) + "/" + str(i%6) + ".sh"

        if i%6 == 0:
            HF_h2o = """#p HF/6-31G opt \n \nh2o_HF \n\n0 1\n""" + h2o_coords + "\n! RW"
            job_str += """g16 < h2o_HF.gj > h2o_HF.out"""
            job_path_2 = "runs/h2o/" + str(i % 6) + "/" + "h2o_HF.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(HF_h2o)
            f_gj.close()
        if i%6 == 1:
            MP2_h2o = """#p MP2/6-31G opt \n\nh2o_MP2 \n\n0 1\n""" + h2o_coords + "\n! RW"
            job_str += """g16 < h2o_MP2.gj > h2o_MP2.out"""
            job_path_2 = "runs/h2o/" + str(i % 6) + "/" + "h2o_MP2.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(MP2_h2o)
            f_gj.close()
        if i%6 == 2:
            CCSD_h2o= """#p CCSD/6-31G opt \n\nh2o_CCSD \n\n0 1\n""" + h2o_coords + "\n! RW"
            job_str += """g16 < h2o_CCSD.gj > h2o_CCSD.out"""
            job_path_2 = "runs/h2o/" + str(i % 6) + "/" + "h2o_CCSD.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(CCSD_h2o)
            f_gj.close()
        if i%6 == 3:
            B3LYP_h2o= """#p B3LYP/6-31G opt \n\nh2o_B3LYP \n\n0 1\n""" + h2o_coords + "\n! RW"
            job_str += """g16 < h2o_B3LYP.gj > h2o_B3LYP.out"""
            job_path_2 = "runs/h2o/" + str(i % 6) + "/" + "h2o_B3LYP.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(B3LYP_h2o)
            f_gj.close()
        if i%6 == 4:
            AM1_h2o = """#p AM1/6-31G opt \n\nh2o_AM1 \n\n0 1\n""" + h2o_coords + "\n! RW"
            job_str += """g16 < h2o_AM1.gj > h2o_AM1.out"""
            job_path_2 = "runs/h2o/" + str(i % 6) + "/" + "h2o_AM1.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(AM1_h2o)
            f_gj.close()
        if i%6 == 5:
            MNDO_h2o = """#p MNDO/6-31G opt \n\nh2o_MNDO \n\n0 1\n""" + h2o_coords + "\n! RW"
            job_str += """g16 < h2o_MNDO.gj > h2o_MNDO.out"""
            job_path_2 = "runs/h2o/" + str(i % 6) + "/" + "h2o_MNDO.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(MNDO_h2o)
            f_gj.close()


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
cd $WORK/gaussian/runs/ethane/""" + str(i%6) + "\n"

        with open("ethane.coords", "r") as myfile:
            ethane_coords = myfile.read()

        os.mkdir("runs/ethane/" + str(i % 6))

        if i%6 == 0:
            HF_ethane = """#p HF/6-31G opt \n\nethane_HF \n\n0 1\n""" + ethane_coords + "\n! RW"
            job_str += """g16 < ethane_HF.gj > ethane_HF.out"""
            job_path_2 = "runs/ethane/" + str(i % 6) + "/" + "ethane_HF.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(HF_ethane)
            f_gj.close()
        if i%6 == 1:
            MP2_ethane = """#p MP2/6-31G opt \n\nethane_MP2 \n\n0 1\n""" + ethane_coords + "\n! RW"
            job_str += """g16 < ethane_MP2.gj > ethane_MP2.out"""
            job_path_2 = "runs/ethane/" + str(i % 6) + "/" + "ethane_MP2.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(MP2_ethane)
            f_gj.close()
        if i%6 == 2:
            CCSD_ethane = """#p CCSD/6-31G opt \n\nethane_CCSD \n\n0 1\n""" + ethane_coords + "\n! RW"
            job_str += """g16 < ethane_CCSD.gj > ethane_CCSD.out"""
            job_path_2 = "runs/ethane/" + str(i % 6) + "/" + "ethane_CCSD.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(CCSD_ethane)
            f_gj.close()
        if i%6 == 3:
            B3LYP_ethane = """#p B3LYP/6-31G opt \n\nethane_B3LYP \n\n0 1\n""" + ethane_coords + "\n! RW"
            job_str += """g16 < ethane_B3LYP.gj > ethane_B3LYP.out"""
            job_path_2 = "runs/ethane/" + str(i % 6) + "/" + "ethane_B3LYP.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(B3LYP_ethane)
            f_gj.close()
        if i%6 == 4:
            AM1_ethane = """#p AM1/6-31G opt \n\nethane_AM1 \n\n0 1\n""" + ethane_coords + "\n! RW"
            job_str += """g16 < ethane_AM1.gj > ethane_AM1.out"""
            job_path_2 = "runs/ethane/" + str(i % 6) + "/" + "ethane_AM1.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(AM1_ethane)
            f_gj.close()
        if i%6 == 5:
            MNDO_ethane = """#p MNDO/6-31G opt \n\nethane_MNDO \n\n0 1\n""" + ethane_coords + "\n! RW"
            job_str += """g16 < ethane_MNDO.gj > ethane_MNDO.out"""
            job_path_2 = "runs/ethane/" + str(i % 6) + "/" + "ethane_MNDO.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(MNDO_ethane)
            f_gj.close()

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
cd $WORK/gaussian/runs/NiCO4/""" + str(i%6) + "\n"

        with open("NiCO4.coords", "r") as myfile:
            NiCO4_coords = myfile.read()

        os.mkdir("runs/NiCO4/" + str(i%6))

        if i%6 == 0:
            HF_NiCO4 = """#p HF/6-31G opt \n\nNiCO4_HF \n\n0 1\n""" + NiCO4_coords + "\n! RW"
            job_str += """\ng16 < NiCO4_HF.gj> NiCO4_HF.out"""
            job_path_2 = "runs/NiCO4/" + str(i % 6) + "/" + "NiCO4_HF.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(HF_NiCO4)
            f_gj.close()
        if i%6 == 1:
            MP2_NiCO4 = """#p MP2/6-31G opt \n\nNiCO4_MP2 \n\n 0 1\n""" + NiCO4_coords + "\n! RW"
            job_str += """g16 < NiCO4_MP2.gj > NiCO4_MP2.out"""
            job_path_2 = "runs/NiCO4/" + str(i % 6) + "/" + "NiCO4_MP2.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(MP2_NiCO4)
            f_gj.close()
        if i%6 == 2:
            CCSD_NiCO4 = """#p CCSD/6-31G opt \n\nNiCO4_CCSD \n\n0 1\n""" + NiCO4_coords + "\n! RW"
            job_str += """g16 < NiCO4_CCSD.gj > NiCO4_CCSD.out"""
            job_path_2 = "runs/NiCO4/" + str(i % 6) + "/" + "NiCO4_CCSD.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(CCSD_NiCO4)
            f_gj.close()
        if i%6 == 3:
            B3LYP_NiCO4 = """#p B3LYP/6-31G opt \n\nNiCO4_B3LYP \n\n0 1\n""" + NiCO4_coords + "\n! RW"
            job_str += """g16 < NiCO4_B3LYP.gj > NiCO4_B3LYP.out"""
            job_path_2 = "runs/NiCO4/" + str(i % 6) + "/" + "NiCO4_B3LYP.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(B3LYP_NiCO4)
            f_gj.close()
        if i%6 == 4:
            AM1_NiCO4 = """#p AM1/6-31G opt \n\nNiCO4_AM1 \n\n0 1\n""" + NiCO4_coords + "\n! RW"
            job_str += """g16 < NiCO4_AM1.gj > NiCO4_AM1.out"""
            job_path_2 = "runs/NiCO4/" + str(i % 6) + "/" + "NiCO4_AM1.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(AM1_NiCO4)
            f_gj.close()
        if i%6 == 5:
            MNDO_NiCO4 = """#p MNDO/6-31G opt \n\nNiCO4_MNDO \n\n0 1\n""" + NiCO4_coords + "\n! RW"
            job_str += """g16 < NiCO4_MNDO.gj > NiCO4_MNDO.out"""
            job_path_2 = "runs/NiCO4/" + str(i % 6) + "/" + "NiCO4_MNDO.gj"
            f_gj = open(job_path_2, "w")
            f_gj.write(MNDO_NiCO4)
            f_gj.close()

        job_path = "runs/NiCO4/" + str(i%6) + "/" + str(i%6) + ".sh"

        f = open(job_path, "w")
        f.write(job_str)
        f.close()

        f_sum.write("sbatch " + job_path + "\n")

    i +=1

f_sum.close()







