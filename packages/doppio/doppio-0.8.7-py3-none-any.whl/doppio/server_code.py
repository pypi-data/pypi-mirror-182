import json
import os

def check_json_from_server(dataset=None, split_dir=None, task_info=None, augmentation=None, valid_classes=None, semantic_mask_flag=0):


    file_path = "/home/ai/disk/data/doppio/{}/{}/doppio_labels/{}_labels/files.json".format(dataset, split_dir,list(task_info.keys())[0])
    label_path = "/home/ai/disk/data/doppio/{}/{}/doppio_labels/{}_labels/".format(dataset, split_dir, list(task_info.keys())[0])

    total_json_files = {"label_files": [], "image_files": [], "mask_files" : []}

    with open(file_path, "r") as json_path:

        json_file = json.load(json_path)

    json_files = json_file['label_files']
    image_files = json_file['image_files']
    mask_files = json_file['mask_files']

    if valid_classes == None or semantic_mask_flag == 1:
        return json_file
       
    for json_file_name in json_files:

        json_path = os.path.join(label_path, json_file_name)  

        with open(json_path, "r") as json_path_:
            json_file = json.load(json_path_)

        img_name = json_file['image_name']
        json_name = json_file_name

        flag = 0 
        for ann in json_file['annotation']:
            classes = ann['class']
            if classes in valid_classes:
                flag = 1
                break
        if flag == 1:

           total_json_files["label_files"].append(json_name)
           total_json_files['image_files'].append(img_name)
    

    return total_json_files
