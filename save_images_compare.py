import os, random, cv2
import tqdm

def save_images(image_array, folder_path, base_filename='image'):
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    for idx, img in enumerate(image_array):
        filename = f"{base_filename}_{idx+1}.png"
        file_path = os.path.join(folder_path, filename)
        
        cv2.imwrite(file_path, img)

    print(f"Images have been saved to {folder_path}")

def save_images(image_array1, image_array2, folder_path, filename='image'):
    
    for i in tqdm(range(len(image_array1))):
        
        if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        
        img1 = image_array1[i]
        img2 = image_array2[i]

        fig, ax = plt.subplots(1,2, figsize=[7,7])

        ax[0].imshow(img1)
        ax[0].set_title("RGB")

        ax[1].imshow(img2)
        ax.[1].set_title("Greyscale")

        for a in ax:
            a.axis('off')

        fig.saveFig(os.path.join(folder_path, f"image_{i}.png"))