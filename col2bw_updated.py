from PIL import Image  # to convert images 
from tqdm import tqdm  # to show progress bar
import os  # to fetch path directory


# selecting path/directory
imgs = os.listdir(os.getcwd()+'\samples')


# print total files count in that path
print("Total files in folder:", len(imgs))


# taking range to convert 
print("\nSelecet range to convert images:(1-30)")
start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))


# if range is invalid, show error message and exit program
if 1 > start or len(imgs) < end: print(f"Error: Invalid indexing (Range: 1-{len(imgs)})")


# else convert selected images 
else:

    print("\nProgress: ")
    for i, j in enumerate(tqdm(imgs[start-1 : end])):
        Image.open(os.getcwd() + '/samples/' + imgs[i-1]).convert('L').save(os.getcwd() + '/converted/' + imgs[i-1])


    # print confirmation message and hit enter before terminating
    print("\n-> Result:"+ str(end - (start-1)) + " images converted successfully !\nHit ENTER to exit...", end='')
    input() 