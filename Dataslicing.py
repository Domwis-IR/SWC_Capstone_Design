import os
import matplotlib.pyplot as plt
import nibabel as nib
from time import sleep
def DataSlicing (source, save, slice):
    files = os.listdir(source)
    files.sort()
    count = 0
    for file in files:
        img = nib.load(f"{source}/{file}")
        data = img.get_fdata()
        for i in range(slice):
            plt.imsave(f"{save}/axial/{file}_{i+1}.png",data[:, :, i+13],cmap='gray', origin='lower')
            print(count, f"{save}/axial/{file}_{i+1}.png")
        sleep(1)
        count += 1

    count = 0
    for file in files:
        img = nib.load(f"{source}/{file}")
        data = img.get_fdata()
        for i in range(slice):
            plt.imsave(f"{save}/coronal/{file}_{i+1}.png",data[:, i+27, :],cmap='gray', origin='lower')
            print(count, f"{save}/coronal/{file}_{i+1}.png")
        sleep(1)
        count += 1

    count = 0
    for file in files:
        img = nib.load(f"{source}/{file}")
        data = img.get_fdata()
        for i in range(slice):
            plt.imsave(f"{save}/sagittal/{file}_{i+1}.png",data[i+20, :, :],cmap='gray', origin='lower')
            print(count, f"{save}/sagittal/{file}_{i+1}.png")
        sleep(1)
        count += 1

if __name__ == '__main__':
    source = r'/root/default/capstone/HCP_YA_2mm/data'
    save = r'/root/default/capstone/HCP_YA_2mm/40'
    DataSlicing(source,save,40)
