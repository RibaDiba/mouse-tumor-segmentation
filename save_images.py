import os, random, cv2
import matplotlib.pyplot as plt
import tqdm

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

MedSAM_greyscale = read_images_to_array('./images_MedSAM_greyscale')
MedSAM_rgb = read_images_to_array('./images_MedSAM_rgb')
SAM_greyscale = read_images_to_array('./images_SAM_greyscale')
SAM_rgb = read_images_to_array('./images_SAM_rgb')

for i in tqdm(range(len(SAM_rgb))):

     M_greyscale = MedSAM_greyscale[i]
     M_rgb = MedSAM_rgb[i]
     S_greyscale = SAM_greyscale[i]
     S_rgb = SAM_rgb[i]

     fig, ax = plt.subplots(nrows=4, figsize=[7,7])

     ax[0].imshow(M_greyscale)
     ax[0].set_title("MedSAM Greyscale")

     ax[1].imshow(S_greyscale)
     ax[1].set_title("SAM Greyscale")

     ax[2].imshow(M_rgb)
     ax[2].set_title("MedSAM RGB")

     ax[3].imshow(S_rgb)
     ax[3].set_title("SAM RGB")

     for a in ax: 
        a.axis("off")

     fig.savefig(os.path.join("./final_images", f"image_{i}.png"))
     plt.close(fig)