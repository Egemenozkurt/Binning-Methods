#import required libraries
#pip install numpy
import numpy as np

def equi_depth_binning(data, num_bins):
    #Sort data
    sorted_data = np.sort(data)
    
    #Calculate number of data
    num_points = len(data)
    points_per_bin = int(num_points / num_bins)
    
    #Array to store the bin indices
    bin_indices = np.zeros_like(data, dtype=int)
    
    #Assign the bin indices to each data point
    for i, value in enumerate(data):
        bin_indices[i] = int(i / points_per_bin)
    
    #Dictionary to store the bin data
    bins = {}
    
    #Populate the bins with data points
    for i, value in enumerate(data):
        bin_index = bin_indices[i]
        if bin_index not in bins:
            bins[bin_index] = []
        bins[bin_index].append(value)
    
    #Print Partition into equal-frequency (equi-depth) bins
    print("Partition into equal-frequency (equi-depth) bins:")
    for bin_index, bin_data in bins.items():
        print(f"- Bin {bin_index+1}: {', '.join(map(str, bin_data))}")
    return bin_indices

def bin_means(data, bin_indices):
    #Dictionary to store the bin data
    bins = {}
    
    #Populate the bins with data points
    for i, value in enumerate(data):
        bin_index = bin_indices[i]
        if bin_index not in bins:
            bins[bin_index] = []
        bins[bin_index].append(value)
    
    #Calculate bin means
    bin_means = {}
    for bin_index, bin_data in bins.items():
        bin_means[bin_index] = np.mean(bin_data)
    return bin_means

def bin_boundaries(data, bin_indices):
    #Create a dictionary to store the bin data
    bins = {}
    
    #Populate the bins with data points
    for i, value in enumerate(data):
        bin_index = bin_indices[i]
        if bin_index not in bins:
            bins[bin_index] = []
        bins[bin_index].append(value)
    
    #Calculate the bin boundaries
    bin_boundaries = {}
    for bin_index, bin_data in bins.items():
        min_value = min(bin_data)
        max_value = max(bin_data)
        bin_boundaries[bin_index] = (min_value, max_value)
    return bin_boundaries

#example data
data = np.array([4, 8, 9, 15, 21, 21, 24, 25, 26, 28, 29, 34])
num_bins = 3

#Calculate bin indice,bin means
bin_indices = equi_depth_binning(data, num_bins)
bin_means = bin_means(data, bin_indices)

#Print bin means
print("Smoothing by bin means:")
for bin_index, mean_value in bin_means.items():
    smoothed_bin_data = [str(int(round(mean_value)))] * len(bin_indices[bin_indices == bin_index])
    print(f"- Bin {bin_index+1}: {', '.join(smoothed_bin_data)}")

bin_boundaries = bin_boundaries(data, bin_indices)

#Print bin boundaries
print("Smoothing by bin boundaries:")
for bin_index, boundaries in bin_boundaries.items():
    smoothed_bin_data = [str(boundaries[0])] * (len(bin_indices[bin_indices == bin_index]) - 1)
    smoothed_bin_data.append(str(boundaries[1]))
    print(f"- Bin {bin_index+1}: {', '.join(smoothed_bin_data)}")