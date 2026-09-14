# - storage.py: save/load from JSON
import json
import os
FILENAME="tasks.json"
def load_json():
    '''Read whatever is in the file'''
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME,"r") as json_file:
            file_cntent=json_file.read().strip()
            if not file_cntent:
                return []
            return json.loads(file_cntent)
    except Exception as e:
        print(f"Error: {e}")
    return []
#demo
print("Reading the file")
contents=load_json()
print(contents)

def save_json(task_list):

    '''Save whatever is in the task_list to json file'''
    try:

        with open(FILENAME,"w") as j_file:

            json.dump(task_list,j_file,indent=4)
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
#demo
print("Saving the file to the file")
my_lists=["Coding","Web development","AI learning"
                   ]
saved=save_json(my_lists)
print(saved)
