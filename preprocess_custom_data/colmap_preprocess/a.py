# import os

# folder_path = "../../data/custom-data/data-duc/lego/images"  # Replace with the path to your folder

# # Get a list of files in the folder
# files = os.listdir(folder_path)

# # Sort the files in alphanumeric order
# files.sort()

# # Iterate over the files and rename them
# for i, file_name in enumerate(files):
#     # Get the file extension
#     file_ext = os.path.splitext(file_name)[1]
    
#     # Create the new file name with zero-padding
#     new_file_name = "{:03d}{}".format(i+1, file_ext)
    
#     # Build the full paths to the old and new file names
#     old_file_path = os.path.join(folder_path, file_name)
#     new_file_path = os.path.join(folder_path, new_file_name)
    
#     # Rename the file
#     os.rename(old_file_path, new_file_path)

import numpy as np
from PIL import Image
img = np.zeros([800,800,3],dtype=np.uint8)
img.fill(255) # numpy array!
im = Image.fromarray(img) #convert numpy array to image
for i in range(0,100):
    im.save("../../data/custom-data/data-duc/lego/mask/"+f"{i:03}"+".jpg")

