# UPXome Demux

This is a script to demultiplex the [QIAseq 3' UPxome RNA Library](https://www.qiagen.com/us/products/discovery-and-translational-research/next-generation-sequencing/rna-sequencing/ultraplex/qiaseq-upxome-rna-library-kits) fastq files without using the QIAGEN online server. Contributions are welcome.

## Dependencies

 - idemux,cutadapt Python package


## Usage

``` sh
python3 qiaseq_upxome_demux.py sample_wells.txt R1.fastq.gz R2.fastq.gz output_folder 
```

## TODO

 - Trim the linker sequence from R2. (Trim first 6 bases)
 - Implement the C++ version of the tool to reduce runtime.
 - Clean up Undetermined files.

## Limitations
Currently only supports paired-end fastq files.
