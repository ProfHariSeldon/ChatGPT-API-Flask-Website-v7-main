# https://chat.openai.com/g/g-b2dsUQrfB-transcriptome-classifier/c/d770e3a5-f565-4b7b-a234-6a75e81aec0a
import os

print(os.getcwd())

# pip install pandas
# python3 -m pip install pandas
import pandas as pd
from pandas import DataFrame as df
import numpy as np
import matplotlib.pyplot as plt

# Loading all the additional BED files
files_paths = {
    'genes': './static/hg38_genes.bed',
    'introns': './static/hg38_introns.bed',
    'CDS': './static/hg38_CDS.bed',
    '5p': './static/hg38_5p.bed',
    '3p': './static/hg38_3p.bed',
    'circRNA': './static/hsa_hg38_circRNA.bed',
    'exons' : './static/hg38_exons.bed'
}
bed_dfs = {}

for key, path in files_paths.items():
    bed_dfs[key] = pd.read_csv(path, sep='\t', header=None)

def adjust_frequency_for_chromosome(df, chromosome, bins):
    # Filter the dataframe for the specified chromosome
    df_chr = df[df[0] == chromosome]

    # Combine start and end positions
    # positions = df_chr[1].append(df_chr[2])
    positions = df_chr[1]._append(df_chr[2])
    # positions = pd.concat(df_chr[1], df_chr[2])

    # Calculate frequency within bins
    freq, bin_edges = np.histogram(positions, bins=bins)

    return freq, bin_edges

# Define chromosome and number of bins
chromosome = 'chr1'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 1')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 1')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr1.png')
# plt.show()
plt.close()

print("chr1 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr2'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 2')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 2')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr2.png')
# plt.show()
plt.close()
print("chr2 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr3'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 3')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 3')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr3.png')
# plt.show()
plt.close()
print("chr3 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr4'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 4')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 4')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr4.png')
# plt.show()
plt.close()
print("chr4 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr5'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 5')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 5')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr5.png')
# plt.show()
plt.close()
print("chr5 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr6'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 6')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 6')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr6.png')
# plt.show()
plt.close()
print("chr6 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr7'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 7')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 7')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr7.png')
# plt.show()
plt.close()
print("chr7 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr8'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 8')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 8')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr8.png')
# plt.show()
plt.close()
print("chr8 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr9'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 9')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 9')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr9.png')
# plt.show()
plt.close()
print("chr9 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr10'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 10')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 10')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr10.png')
# plt.show()
plt.close()
print("chr10 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr11'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 11')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 11')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr11.png')
# plt.show()
plt.close()
print("chr11 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr12'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 12')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 12')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr12.png')
# plt.show()
plt.close()
print("chr12 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr13'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 13')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 13')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr13.png')
# plt.show()
plt.close()
print("chr13 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr14'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 14')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 14')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr14.png')
# plt.show()
plt.close()
print("chr14 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr15'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 15')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 15')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr15.png')
# plt.show()
plt.close()
print("chr15 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr16'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 16')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 16')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr16.png')
# plt.show()
plt.close()
print("chr16 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr17'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 17')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 17')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr17.png')
# plt.show()
plt.close()
print("chr17 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr18'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 18')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 18')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr18.png')
# plt.show()
plt.close()
print("chr18 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr19'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 19')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 19')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr19.png')
# plt.show()
plt.close()
print("chr19 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr20'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 20')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 20')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr20.png')
# plt.show()
plt.close()
print("chr20 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr21'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 21')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 21')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr21.png')
# plt.show()
plt.close()
print("chr21 done")
######################################
# Define chromosome and number of bins
chromosome = 'chr22'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome 22')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome 22')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chr22.png')
# plt.show()
plt.close()
print("chr22 done")
######################################
# Define chromosome and number of bins
chromosome = 'chrX'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome X')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome X')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chrX.png')
# plt.show()
plt.close()
print("chrX done")
######################################
# Define chromosome and number of bins
chromosome = 'chrY'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Chromosome Y')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Chromosome Y')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chrY.png')
# plt.show()
plt.close()
print("chrY done")
######################################
# Define chromosome and number of bins
chromosome = 'chrMT'
bins = 100

# Calculate frequencies for all datasets for chromosome 1
frequencies = {}
bin_edges_dict = {}
for key, df in bed_dfs.items():
    frequencies[key], bin_edges_dict[key] = adjust_frequency_for_chromosome(df, chromosome, bins)

# Creating line graphs for each dataset
plt.figure(figsize=(15, 10))
for key, freq in frequencies.items():
    plt.plot(bin_edges_dict[key][:-1], freq, label=f'{key} Frequency')

plt.xlabel('Genomic Position on Mitochondrial Chromosome')
plt.ylabel('Frequency')
plt.title('Frequency of Genomic Features on Mitochondrial Chromosome')
plt.legend()
# plt.show()

# save a image using extension 
plt.savefig('./static/images/chrMT.png')
# plt.show()
plt.close()
print("chrMT done")