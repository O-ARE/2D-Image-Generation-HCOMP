# 2D-Image-Generation-HCOMP

# Generating an Image
To generate an image using this code 4 steps are required:

    I. Seting up the environment
    II. Making a json image parameters file
    III. Running the "json_image_gen.py" code


### I. Environment setup
Run `bash setup.sh` to setup the virtual environment, install the python dependencies and download MPEG7 dataset.


### II. Making a json image parameters file
The code generates an image based on the parameters set in the JSON files.
In the home folder of this project there is a "template.json" that is an example of a working set of parameters used to generate an image.

The following sections will be used to explain how to change the parameters used in a JSON file.

1. `save_dir`
    This is input will direct where the generated image will be saved. This can be either an absolute or relative path. See two examples below. The first is the default.
    ```json
    "save_dir": "Image_Ouput/"
    ```
    ```json
    "save_dir": "C:/Users/Joshua/Documents/Project/Image_Output/"
    ```
2. `save_name`
    This input will be the text that is used to name the output files.
    When run three files will be generated.

    1. The image using the input parameters named *"<save_name>.png"*
    2. Another version of the image that makes the specified find image white named *"<save_name>-find.png"*
    3. A .json file that contains the input parameters and additional metadata named *"<save_name>.json"*

3. `background` This section includes 3 inputs. The color, width, and height of the background image. A valid entry will be formatted as follows:
    ```json
    "background": {
        "color": "beige",
        "width": 1080,
        "height": 1080
    }
    ```
    Currently the color is stated by name. In the future this will be updated to an RGB input. The color can currently be set to any of the colors show on the following website: https://www.w3schools.com/colors/colors_names.asp

4. `scale` The scale determines the size that the shapes will generated. The measure is a proportion of the height dimension of the background. For example, if the background is 500x1000 (WxH) and the scale of a shape is 0.25, then the shape will be generated at a 250x250 size. This parameter has two parts. The first is the distribution that will guide the random sampling and the second is the distribution parameters. Currently the triangular and uniform distributions are supported. See two examples below:

    ```json
    "scale": {
            "dist": "T",
            "params": [0.15, 0.2, 0.25]
    }
    ```
    The triangular distribution has parameters set up as [Lower Bound, Peak, Upper Bound].

    ```json
    "scale": {
            "dist": "U", 
            "params": [0.2, 0.3]
    }
    ```
    The uniform distribution has the parameters set as [Lower Bound, Upper Bound]

5. `rotation` The rotation determines what angle of rotation, in degrees, a shape has from the original image. This parameter has the same inputs as the scale. See two examples below:

    ```json
    "rotation": {
            "dist": "U",
            "params": [0, 360]
    }
    ```
    ```json
    "rotation": {
            "dist": "T",
            "params": [-15, 0, 15]
    }
    ```

6. `color` The color input determines the color each shape will be generated as. There are 3 distributions available for this parameter. Uniform, triangular, and mode. Each will be explained below.

    #### Uniform
    Using the uniform distribution, each channel of red, green, blue, and alpha will be independently distributed using their own upper and lower bounds. See example below:
    ```json
    "color": {
        "dist": "U",
        "args": [
            [10,255],
            [10,255],
            [10,255],
            [140,170]
        ]
    }
    ```

    #### Triangular
    This distribution is input very similar to the uniform one. Each channel is given the lower bounds, peak, and upper bounds. See example:
    ```json
    "color": {
        "dist": "T",
        "args": [
            [50, 70, 90],
            [200, 210, 255],
            [0, 50, 60],
            [140, 155, 170]
        ]
    }
    ```

    #### Mode
    This is a distributed made to allow for specific colors to be chosen. The inputs are each a "mode" that could be randomly selected. This supports 1 or more mode inputs. See example that will generate shapes that are all the same color:
    ```json
    "color": {
        "dist": "M",
        "args": [
            [160, 195, 93, 155]
        ]
    }
    ```
    Below is code that will generate images with 2 colors:
    ```json
    "color": {
        "dist": "M",
        "args": [
            [160, 195, 93, 155],
            [30, 150, 38, 140]
        ]
    }
    ```
    This mode will likely be updated in the near future.

7. `centers` The centers section are the input parameters for the poisson disc distribution that will make all the center points for the shapes.

    The "r" value is the minimum pixels between the center points generated. 

    The "k" value is how many times the program will try to generate a new point before giving up. The value 32 seems to be a good number to ensure there are no large blank spaces, but not be too inefficient.

    To learn more about the poisson disc distribution, and the code used in this program visit the following website: https://scipython.com/blog/poisson-disc-sampling-in-python/

    ```json
    "centers": {
        "r": 150,
        "k": 32
    }
    ```

8. `find_images` This section sets the shapes that will be required to be placed when the image is generated. The inputs required are the name of the MPEG7 shape, and the depth. The depth will determine when the shape is placed. Depth can be a value from 0 to 1. For example, if 1000 shapes are going to be placed and the depth is set to 0.2, the specified image will be placed as the 200th image. See example below:
    ```json
    "find_images": [
        {"name": "bat-1.gif", "depth": 0.4}
    ],
    ```
    The find images can also be left empty:
    ```json
    "find_images": [
    ],
    ```
    More than one image can be included as well:
    ```json
    "find_images": [
        {"name": "bat-1.gif", "depth": 0.40},
        {"name": "bat-1.gif", "depth": 0.41},
        {"name": "bat-3.gif", "depth": 0.42},
        {"name": "butterfly-1.gif", "depth": 0.43}
    ],
    ```
    When there are multiple find images all will be shown in the produced "<save_name>-find.png" image.

9. `excluded_images` This section will stop these specified shapes from being randomly selected. This does not apply to the "find_images" section. The following example is used to remove all the bats, so that no bats will be confused for the bat that is being searched for.
    ```json
    "excluded_images": [
        {"name": "bat-1.gif"},
        {"name": "bat-2.gif"},
        {"name": "bat-3.gif"},
        {"name": "bat-4.gif"},
        {"name": "bat-5.gif"},
        {"name": "bat-6.gif"},
        {"name": "bat-7.gif"},
        {"name": "bat-8.gif"},
        {"name": "bat-9.gif"},
        {"name": "bat-10.gif"},
        {"name": "bat-11.gif"},
        {"name": "bat-12.gif"},
        {"name": "bat-13.gif"},
        {"name": "bat-14.gif"},
        {"name": "bat-15.gif"},
        {"name": "bat-16.gif"},
        {"name": "bat-17.gif"},
        {"name": "bat-18.gif"},
        {"name": "bat-19.gif"},
        {"name": "bat-20.gif"}
    ]
    ```
### IV. Running the "json_image_gen.py" code
To finally generate one or more images, run

```bash
source .venv/bin/activate
python json_image_gen.py
``` 

The python script cycles through all the .json files in the JSON input folder (Default "Input_JSON/") and generates images using those parameters and outputs to the output folder (Default "Output_Images/"). Both of these directories, as well as the MPEG7 directories can be changed from the "json_image_gen.py" code. 

To quickly try generating a new image, copy and paste the "template.json" file from the home folder into the JSON input folder and run the "json_image_gen.py" code. After completion, you will find two images and an additional .json file in the "Output_Images" folder. 

Some things to note:
1. A newly generated file (.png or .json) that has the same name as another file in the output folder will be overwritten with no warning. 
2. Since the random sampling is done during the execution of this code, you can rerun the same code with the same .json files and it will output new images. This is helpful when by chance the image that you are looking for is placed so close to the edge that it is not possible to find.
3. The JSON input folder can contain as many .json files as you want. The code will simply cycle through them all. The code will print out a status as the images are generated to track progress. Images with especially low "r" values, or especially large background sizes will take long to generate. 
