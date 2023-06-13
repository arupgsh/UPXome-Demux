# UPXome Demux

## Dependencies

 - idemux Python package


## Usage

``` sh
python3 qiaseq_upxome_demux.py sample_wells.txt R1.fastq.gz R2.fastq.gz 
```

##TODO

 - Trim the linker sequence from R2. (Trim first 6 bases)
 - Implement the C++ version of the tool to reduce runtime.
 - Clean up Undetermined files.
