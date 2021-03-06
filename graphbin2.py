#!/usr/bin/env python3

"""graphbin2.py: Refined and overlapped binning of metagenomic contigs using assembly graphs."""

import argparse
import os
import sys
import subprocess

__author__ = "Vijini Mallawaarachchi, Anuradha Wickramarachchi, and Yu Lin"
__copyright__ = "Copyright 2020, GraphBin2 Project"
__license__ = "GPL"
__version__ = "0.2"
__maintainer__ = "Vijini Mallawaarachchi"
__email__ = "vijini.mallawaarachchi@anu.edu.au"
__status__ = "Prototype"

parser = argparse.ArgumentParser(description="""GraphBin2 Help. GraphBin2 is a tool which refines the binning results obtained from existing tools and, 
more importantly, is able to assign contigs to multiple bins. GraphBin2 uses the connectivity and coverage information from assembly graphs to 
adjust existing binning results on contigs and to infer contigs shared by multiple species.""")

parser.add_argument("--assembler", 
                    required=True, 
                    type=str,
                    help="name of the assembler used (SPAdes or SGA)")

parser.add_argument("--graph", 
                    required=True,
                    type=str,
                    help="path to the assembly graph file")

parser.add_argument("--contigs", 
                    required=True,
                    type=str,
                    help="path to the contigs file")

parser.add_argument("--paths", 
                    required=False,
                    type=str,
                    help="path to the contigs.paths file")

parser.add_argument("--abundance", 
                    required=False,
                    type=str,
                    help="path to the abundance file")

parser.add_argument("--binned", 
                    required=True,
                    type=str,
                    help="path to the .csv file with the initial binning output from an existing tool")

parser.add_argument("--output", 
                    required=True,
                    type=str,
                    help="path to the output folder")

parser.add_argument("--prefix", 
                    required=False,
                    type=str,
                    default='',
                    help="prefix for the output file")

parser.add_argument("--depth", 
                    required=False, 
                    type=int, 
                    default=5, 
                    help="maximum depth for the breadth-first-search. [default: 5]")

parser.add_argument("--threshold", 
                    required=False, 
                    type=float, 
                    default=1.5, 
                    help="threshold for determining inconsistent vertices. [default: 1.5]")

parser.add_argument("--nthreads", 
                    required=False, 
                    type=int, 
                    default=8, 
                    help="number of threads to use. [default: 8]")

args = vars(parser.parse_args())


assembler = args["assembler"]
assembly_graph_file = args["graph"]
contigs = args["contigs"]
contig_paths = args["paths"]
abundance = args["abundance"]
contig_bins_file = args["binned"]
output_path = args["output"]
prefix = args["prefix"]
depth = args["depth"]
threshold = args["threshold"]
nthreads = args["nthreads"]


# Validation of inputs
#---------------------------------------------------

# Check assembler type
if not (assembler.lower() == "spades" or assembler.lower() == "sga"):
    print("\nPlease make sure to provide the correct assembler type (SPAdes or SGA).")
    print("Exiting GraphBin2...\nBye...!\n")
    sys.exit(1)

# Check assembly graph file
if not os.path.isfile(assembly_graph_file):
    print("\nFailed to open the assembly graph file.")
    print("Exiting GraphBin2...\nBye...!\n")
    sys.exit(1)

# Check contigs file
if not os.path.isfile(contigs):
    print("\nFailed to open the contigs file.")
    print("Exiting GraphBin2...\nBye...!\n")
    sys.exit(1)

# Check if paths file is provided when the assembler type is SPAdes
if assembler.lower() == "spades" and contig_paths is None:
    print("\nPlease make sure to provide the path to the contigs.paths file.")
    print("Exiting GraphBin2...\nBye...!\n")
    sys.exit(1)

# Check contigs.paths file for SPAdes
if assembler.lower() == "spades" and not os.path.isfile(contig_paths):
    print("\nFailed to open the contigs.paths file.")
    print("Exiting GraphBin2...\nBye...!\n")
    sys.exit(1)

# Check if abundance file is provided when the assembler type is SGA
if assembler.lower() == "sga" and abundance is None:
    print("\nPlease make sure to provide the path to the abundance file.")
    print("Exiting GraphBin2...\nBye...!\n")
    sys.exit(1)

# Check contigs.paths file for sga
if assembler.lower() == "sga" and not os.path.isfile(abundance):
    print("\nFailed to open the abundance file.")
    print("Exiting GraphBin2...\nBye...!\n")
    sys.exit(1)

# Check the file with the initial binning output
if not os.path.isfile(contig_bins_file):
    print("\nFailed to open the file with the initial binning output.")
    print("Exiting GraphBin2...\nBye...!\n")
    sys.exit(1)

# Handle for missing trailing forwardslash in output folder path
if output_path[-1:] != "/":
    output_path = output_path + "/"

# Create output folder if it does not exist
if not os.path.isdir(output_path):
    subprocess.run("mkdir -p "+output_path, shell=True)

# Validate prefix
if args["prefix"] != '':
    if args["prefix"].endswith("_"):
        prefix = args["prefix"]
    else:
        prefix = args["prefix"]+"_"
else:
    prefix = ''

# Validate depth
if depth < 1:
    print("\nPlease enter a valid number for depth")
    print("Exiting GraphBin2...\nBye...!\n")
    sys.exit(1)

# Validate threshold
if threshold < 1.0:
    print("\nPlease enter a valid number for threshold")
    print("Exiting GraphBin2...\nBye...!\n")
    sys.exit(1)

# Validate number of threads
if nthreads <= 0:
    print("\nPlease enter a valid number for the number of threads")
    print("Exiting GraphBin2...\nBye...!\n")
    sys.exit(1)


# Run GraphBin2
#---------------------------------------------------
if assembler.lower() == "spades":
    cmdGraphBin2 = """python "{0}/src/graphbin2_SPAdes.py" --graph "{1}" --contigs "{2}" --paths "{3}" --binned "{4}" --output "{5}" --prefix "{6}" --depth "{7}" --threshold "{8}" --nthreads "{9}" """.format(
        os.path.dirname(__file__), 
        assembly_graph_file,
        contigs,
        contig_paths, 
        contig_bins_file, 
        output_path,
        prefix,
        depth,
        threshold,
        nthreads)

elif assembler.lower() == "sga":
    cmdGraphBin2 = """python "{0}/src/graphbin2_SGA.py" --graph "{1}" --contigs "{2}" --binned "{3}" --abundance "{4}" --output "{5}" --prefix "{6}" --depth "{7}" --threshold "{8}"  --nthreads "{9}" """.format(
        os.path.dirname(__file__), 
        assembly_graph_file,
        contigs,
        contig_bins_file, 
        abundance,
        output_path,
        prefix,
        depth,
        threshold,
        nthreads)


os.system(cmdGraphBin2)
