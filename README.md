<p align="center">
  <img src="GraphBin2_Logo.png" width="450" title="GraphBin2 Logo" alt="GraphBin2 Logo">
</p>

# GraphBin2: Refined and Overlapped Binning of Metagenomic Contigs Using Assembly Graphs

![GitHub](https://img.shields.io/github/license/Vini2/GraphBin2) 
![GitHub top language](https://img.shields.io/github/languages/top/Vini2/GraphBin2)

GraphBin2 is an extension of [GraphBin](https://github.com/Vini2/GraphBin) which refines the binning results obtained from existing tools and, more importantly, is able to assign contigs to multiple bins. GraphBin2 uses the connectivity and coverage information from assembly graphs to adjust existing binning results on contigs and to infer contigs shared by multiple species.

## Getting Started

### Downloading GraphBin2
You can download the latest release of GraphBin from [Releases](https://github.com/Vini2/GraphBin/releases) or clone the GraphBin repository to your machine.

```
git clone https://github.com/Vini2/GraphBin2.git
```

If you have downloaded a release, you will have to extract the files using the following command.

```
unzip [file_name].zip
```

Now go in to the GraphBin folder using the command

```
cd GraphBin/src/
```

## Using GraphBin2
You can see the usage options of GraphBin by typing ```python graphbin2_SPAdes.py -h``` or ```python graphbin2_SGA.py -h``` on the command line. For example,

```
python graphbin2_SPAdes.py -h
usage: graphbin2_SPAdes.py [-h] --contigs CONTIGS --graph GRAPH --paths PATHS
                           --binned BINNED --output OUTPUT [--prefix PREFIX]
                           [--depth DEPTH] [--threshold THRESHOLD]
                           [--nthreads NTHREADS]

GraphBin2 Help. GraphBin2 is a tool which refines the binning results obtained
from existing tools and, more importantly, is able to assign contigs to
multiple bins. GraphBin2 uses the connectivity and coverage information from
assembly graphs to adjust existing binning results on contigs and to infer
contigs shared by multiple species.

optional arguments:
  -h, --help            show this help message and exit
  --contigs CONTIGS     path to the contigs file
  --graph GRAPH         path to the assembly graph file
  --paths PATHS         path to the contigs.paths file
  --binned BINNED       path to the .csv file with the initial binning output
                        from an existing tool
  --output OUTPUT       path to the output folder
  --prefix PREFIX       prefix for the output file
  --depth DEPTH         maximum depth for the breadth-first-search. [default: 5]
  --threshold THRESHOLD
                        threshold for determining inconsistent vertices.
                        [default: 1.5]
  --nthreads NTHREADS   number of threads to use. [default: 8]
```
```
python graphbin2_SGA.py -h
usage: graphbin2_SGA.py [-h] --contigs CONTIGS --abundance ABUNDANCE --graph
                        GRAPH --binned BINNED --output OUTPUT
                        [--prefix PREFIX] [--depth DEPTH]
                        [--threshold THRESHOLD] [--nthreads NTHREADS]

GraphBin2 Help. GraphBin2 is a tool which refines the binning results obtained
from existing tools and, more importantly, is able to assign contigs to
multiple bins. GraphBin2 uses the connectivity and coverage information from
assembly graphs to adjust existing binning results on contigs and to infer
contigs shared by multiple species.

optional arguments:
  -h, --help            show this help message and exit
  --contigs CONTIGS     path to the contigs file
  --abundance ABUNDANCE
                        path to the abundance file
  --graph GRAPH         path to the assembly graph file
  --binned BINNED       path to the .csv file with the initial binning output
                        from an existing tool
  --output OUTPUT       path to the output folder
  --prefix PREFIX       prefix for the output file
  --depth DEPTH         maximum depth for the breadth-first-search. [default: 5]
  --threshold THRESHOLD
                        threshold for determining inconsistent vertices.
                        [default: 1.5]
  --nthreads NTHREADS   number of threads to use. [default: 8]
```

## Input Format

For the SPAdes version, `graphbin_SPAdes.py` takes in 4 files as inputs (required).
* Contigs file (in `.fasta` format)
* Assembly graph file (in `.gfa` format)
* Paths of contigs (in `.paths` format)
* Binning output from an existing tool (in `.csv` format)

For the SGA version, `graphbin_SGA.py` takes in 4 files as inputs (required).
* Contigs file (in `.fasta` format)
* Abundance file (tab separated file with contig number and coverage in each line)
* Assembly graph file (in `.asqg` format)
* Binning output from an existing tool (in `.csv` format)

**Note:** The binning output file should have comma separated values ```(contig_number, bin_number)``` for each contig. The contents of the binning output file should look similar to the example given below. Contigs are named according to their number starting from 0 and the numbering of bins starts from 1.

Example binned input
```
0,1
1,2
2,1
3,1
4,2
...
```

## Example Usage

```
python graphbin_SPAdes.py --contigs /path/to/contigs.fasta --graph /path/to/graph_file.gfa --paths /path/to/paths_file.paths --binned /path/to/binning_result.csv --output /path/to/output_folder
```
```
python graphbin_SGA.py --contigs /path/to/contigs.fa --abundance /path/to/abundance.tsv --graph /path/to/graph_file.asqg --binned /path/to/binning_result.csv --output /path/to/output_folder
```

## References

[1] Barnum, T.P., _et al._: Genome-resolved metagenomics identifies genetic mobility, metabolic interactions, and unexpected diversity in perchlorate-reducing communities. The ISME Journal 12, 1568-1581 (2018)

[2] Nurk, S., _et al._: metaSPAdes: a new versatile metagenomic assembler. Genome Researcg 5, 824-834 (2017)

[3] Simpson, J. T. and Durbin, R.: Efficient de novo assembly of large genomes using compressed data structures. Genome Research, 22(3), 549–556 (2012).

[4] Wang, Z., _et al._:  SolidBin: improving metagenome binning withsemi-supervised normalized cut. Bioinformatics 35(21), 4229–4238 (2019).

[5] Wu, Y.W., _et al._: MaxBin: an automated binning method to recover individual genomes from metagenomes using an expectation-maximization algorithm. Microbiome 2(1), 26 (2014)

[6] Wu, Y.W., _et al._: MaxBin 2.0: an automated binning algorithm to recover genomes from multiple metagenomic datasets. Bioinformatics 32(4), 605–607 (2016)
