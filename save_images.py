import os, random, cv2
import matplotlib.pyplot as plt
from tqdm import tqdm

def read_images_to_array(folder_path):

  image_array = []
  # Get a sorted list of filenames
  filenames = sorted(os.listdir(folder_path))
  for filename in filenames:
    if filename.endswith(".jpg") or filename.endswith(".png"):
      img_path = os.path.join(folder_path, filename)
      img = cv2.imread(img_path)

      if img is not None:
        image_array.append(img)

  return image_array

MedSAM_infused = read_images_to_array('./MedSAM_infused')
MedSAM_rgb = read_images_to_array('./MedSAM_rgb')
MedSAM_depth = read_images_to_array('./MedSAM_depth')

for i in tqdm(range(len(MedSAM_rgb)), desc="Saving Images"):

     M_infused = MedSAM_infused[i]
     M_rgb = MedSAM_rgb[i]
     M_depth = MedSAM_depth[i]

     fig, ax = plt.subplots(nrows=3, figsize=[7,7])

     ax[0].imshow(M_infused)
     ax[0].set_title("MedSAM rgb + depth info")

     ax[1].imshow(M_depth)
     ax[1].set_title("MedSAM Greyscale")

     ax[2].imshow(M_rgb)
     ax[2].set_title("MedSAM RGB")

     for a in ax: 
        a.axis("off")

     fig.savefig(os.path.join("./final_images", f"image_{i}.png"))
     plt.close(fig)