# from typing import Mapping
# from numpy.core.fromnumeric import repeat
from image_generator_fun import allFiles
from image_generator_fun import imageGen
import multiprocessing as mp
# from p_tqdm import p_map
# from functools import partial
from itertools import repeat

if __name__ == '__main__':
    # Location of the JSON file(s) that you wish to use to generate image(s) from
    # JSON files should be formatted as the "template.json" file
    jsonDir = "Input_JSON/"

    # Location of the unedited MPEG7 images
    # The MPEG7 dataset can be found at the following link: http://www.timeseriesclassification.com/description.php?Dataset=ShapesAll
    mpeg7Dir = "MPEG7/"

    jsonFiles = allFiles(jsonDir)  # Gets all the JSON files in the provided folder

    # Generates an number of images for each JSON file provided
    image_count = 1250
    for jsonFile in jsonFiles:
        args = {
            'json_dir': jsonDir + jsonFile,
            'mpeg7_dir': mpeg7Dir,
        }
        
        pool = mp.Pool(mp.cpu_count())
        pool.starmap(imageGen, zip(repeat(args), range(image_count)))
        # p_map(partial(imageGen, jsonDir + jsonFiles[0], mpeg7Dir), range(image_count))
        pool.close()
    
    print("Complete")

