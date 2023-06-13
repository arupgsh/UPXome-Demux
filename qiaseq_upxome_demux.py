import sys
import subprocess

# this is a test comment to check if sftp edit working

barcode_dict = {}

#read the positional options
plate_l = sys.argv[1]
r1 = sys.argv[2]
r2 = sys.argv[3]


print(f'Staring run with Plate layout: {plate_l}, Read names: {r1}, {r2}')

with open('data/qiagen_upx_sids.txt','r') as barcodes:
	for barcode in barcodes:
		barcode = barcode.strip('\n').split(',')
		barcode_dict[barcode[1]] = barcode[0]

demux_barcodes = ['sample_name,i7,i5,i1']
with open(plate_l,'r') as sws:
	for sw in sws:
		sw = sw.strip('\n')
		#demux_barcodes.append(f'{barcode_dict.get(sw)}\t{sw}_R1.fastq.gz\t{sw}_R2.fastq.gz')
		demux_barcodes.append(f'{sw},,,{barcode_dict.get(sw)}')

with open('idemux_formatted.csv','w') as t:
	t.write('\n'.join(demux_barcodes))


print('==Format for idemux\n==')
print('\n'.join(demux_barcodes))
print('Starting idemux run')


subprocess.call(['idemux','--r1', r1,'--r2', r2,' --sample-sheet idemux_formatted.csv',' --out demuxed',' --i1-start 1'])


#TODO

print("Trim linker from R2")

print("Running cleanup")

print("Done!")
