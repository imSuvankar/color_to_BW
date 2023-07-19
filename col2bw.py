
from PIL import Image
# from tqdm import tqdm
import os

imgs = os.listdir(os.getcwd()+'/samples/')
print("Total files in folder:", len(imgs))

print("\nSelecet range to convert images:(1-30)")
start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))

if 1 > start or len(imgs) < end: print(f"Error: Invalid indexing (Range: 1-{len(imgs)})")
else:
    # if you want a progress bar, uncomment lines 16 and 17, and comment out lines 18 and 19.
    # for i, j in enumerate(tqdm(imgs[start-1 : end])):
        # Image.open(os.getcwd() + '/samples/' + imgs[i-1]).convert('L').save(os.getcwd() + '/converted/' + imgs[i-1][:imgs[i-1].find('.')] + '.png')
    for i in range(len(imgs[start-1 : end])):
        Image.open(os.getcwd() + '/samples/' + imgs[i-1]).convert('L').save(os.getcwd() + '/converted/' + imgs[i-1])
    print("\n-> Result:"+ str(end - (start-1)) + " images converted successfully !\nHit ENTER to exit...", end='')
    input()
