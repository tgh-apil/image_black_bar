import os
from PIL import Image, ImageDraw
from pathlib import Path

# create a data and output folder to work with imagaes
Path('Data').mkdir(parents=True, exist_ok=True)
Path('Output').mkdir(parents=True, exist_ok=True)

images = os.listdir('Data')

def black_bar_images():
    
    # check whether data folder has data
    if len(images) == 0:
        print('please load data into the Data folder and run script again')
    else:
        for i in range(0, len(images)):
            image_name = images[i]
            
            print(f'Attaching black bar to file: image_name...')
            
            file_path = os.path.join('Data', image_name)
            im = Image.open(file_path)
            
            width, height = im.size
            
            draw = ImageDraw.Draw(im)
            
            # adds a black rectangle with coordinates (0, 0) to the width of the image and a height of 75.
            draw.rectangle([(0, 0), (width, 75)], fill=(0, 0, 0, 255), outline=None)
            del draw
            
            print(f'Saving {image_name} with black bar...')
            
            output_path = os.path.join('Output', 'anon_' + image_name)
            im.save(output_path, "JPEG")
            
            # just for watching output
            current_image_num = i + 1
            num_images = len(images)
            
            if current_image_num == num_images:
                print(f'\n\nAll images in Data folder has a black bar')
            else:
                print(f'Saved {current_image_num} / {num_images}')
                
black_bar_images()
