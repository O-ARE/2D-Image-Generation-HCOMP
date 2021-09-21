import json

json_dir = "Input_JSON/"
img_dir = "Output_Images/"
group_name = "01_1"

backgroundA = [
    ((230,235,209,255), 1080, 1080)
]

scaleA = [
    ("T", .10, .25, .4),
    ("T", 0.25, 0.40, 0.55),
    ("T", 0.40, 0.55, 0.70),
    ("T", 0.55, 0.70, 0.85)
    ]

rotationA = [("U", 0, 365)]

colorA = [
("M",(
(31,28,28,200),
(20,92,163,200),
(20,92,163,150),
(20,92,163,100),
(89,135,28,200),
(89,135,28,150),
(89,135,28,100),
(196,130,23,200),
(196,130,23,150),
(196,130,23,100),
(0,0,0,255)))
]

centersA = [
    (100, 32),
    (120, 32),
    (140, 32),
    (160, 32)
    ]

find_image_name = "ray"
find_image_number = "-7"

find_images = [
    {"name":find_image_name + find_image_number + ".gif", "depth":0.5},
]

excluded_images = [
    {"name": find_image_name + "-1.gif"},
    {"name": find_image_name + "-2.gif"},
    {"name": find_image_name + "-3.gif"},
    {"name": find_image_name + "-4.gif"},
    {"name": find_image_name + "-5.gif"},
    {"name": find_image_name + "-6.gif"},
    {"name": find_image_name + "-7.gif"},
    {"name": find_image_name + "-8.gif"},
    {"name": find_image_name + "-9.gif"},
    {"name": find_image_name + "-10.gif"},
    {"name": find_image_name + "-11.gif"},
    {"name": find_image_name + "-12.gif"},
    {"name": find_image_name + "-13.gif"},
    {"name": find_image_name + "-14.gif"},
    {"name": find_image_name + "-15.gif"},
    {"name": find_image_name + "-16.gif"},
    {"name": find_image_name + "-17.gif"},
    {"name": find_image_name + "-18.gif"},
    {"name": find_image_name + "-19.gif"},
    {"name": find_image_name + "-20.gif"}
]

save_num = 0

for backItem in backgroundA:
    for scaleItem in scaleA:
        for rotationItem in rotationA:
            for colorItem in colorA:
                for centersItem in centersA:
                    # make a dictionary for each combination with some variable name?
                    # maybe just write the json file here?
                    save_num += 1
                    save_name = group_name + "_img" + str(save_num)
                    json_dict = {
                        "save_dir": img_dir,
                        "save_name": save_name,
                        "params": {
                            "background": {
                                "color": backItem[0],
                                "width": backItem[1],
                                "height": backItem[2]
                            },
                            "scale": {
                                "dist": scaleItem[0],
                                "params": scaleItem[1:]
                            },
                            "rotation": {
                                "dist": rotationItem[0],
                                "params": rotationItem[1:]
                            },
                            "color": {
                                "dist": colorItem[0],
                                "args": colorItem[1]
                            },
                            "centers": {
                                "r": centersItem[0],
                                "k": centersItem[1]
                            }
                        },
                        "find_images": find_images,
                        "excluded_images": excluded_images,
                    }
                    with open(json_dir + save_name + ".json", 'w') as json_file:
                        json.dump(json_dict, json_file, indent=4)
