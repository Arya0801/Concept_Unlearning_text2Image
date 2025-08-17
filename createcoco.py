# import os
# import pandas as pd

# # Path to images
# img_dir = "exp"
# prompts = ["Eiffel Tower", "Taj Mahal"]  # Your text descriptions
# image_ids = [os.path.splitext(img)[0] for img in os.listdir(img_dir) if img.endswith(('.png', '.jpg', '.jpeg'))]

# # Create a DataFrame
# data = {"prompt": prompts[:len(image_ids)], "image_id": image_ids}
# df = pd.DataFrame(data)

# # Save as CSV
# df.to_csv("coco_30k.csv", index=False)
# print("coco_30k.csv created!")

import os
import csv

# Define the folder containing the images and output CSV file
image_folder = "ds"  # Path to your image folder
output_csv = "coco_original.csv"

# Create the CSV file
with open(output_csv, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["prompt", "image_id"])  # Write header

    # Traverse through all subfolders and files
    for root, dirs, files in os.walk(image_folder):
        for file in files:
            if file.endswith(('.jpeg', '.jpg', '.png')):
                prompt = os.path.basename(root)  # Use folder name as prompt
                image_id = os.path.splitext(file)[0]  # Remove file extension
                writer.writerow([prompt, image_id])  # Write prompt and image_id to CSV

print(f"CSV file '{output_csv}' created successfully.")
