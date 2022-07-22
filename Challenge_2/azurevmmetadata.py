import subprocess, sys
import json

def recur_json_key(data,searchkey):
    for key,value in data.items():
        if key == searchkey: 
            print(str(value))
        elif isinstance(value, dict):
            recur_json_key(value,searchkey)
        elif isinstance(value, list):
            for val in value:
                if isinstance(val, str):
                    pass
                elif isinstance(val, list):
                    pass
                else:
                    recur_json_key(val,searchkey)

if __name__ == '__main__': 
    p = subprocess.Popen(["powershell","C:\Work\curlcommand.ps1"], stdout=subprocess.PIPE)
    p_out, p_err = p.communicate()
    metadata = json.loads(p_out)
    searchkey = raw_input('Enter The Key To Search \n')
    recur_json_key(metadata,searchkey)