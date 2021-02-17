import argparse
import ast

import requests

def main(values_list, secret, endpoint):
    url = endpoint
    #url = 'http://127.0.0.1:81/task1/'
    headers = {'Content-type': 'application/json', 'secret':str(secret)}
    json_body = {'values' : values_list}
    try:
        r = requests.post(url, json=json_body, headers=headers)
        print(f'Response Code: {r.status_code}')
        print(f'Response Content: {r.text}')
    except Exception as e:
        print(f'Following error happend: {e}')



def parse_arguments():
    """Parse Input Parameters from CLI"""
    parser = argparse.ArgumentParser()
    parser.add_argument("values", # name
                        #nargs="*", # 0 or more values expected => creates a list
                        #type= int
                        type=str, 
                        help="List of Integer Values")
    parser.add_argument("secret", # name
                        type=str, 
                        help="Provided API Key")
    parser.add_argument("--endpoint", # name
                        type=str, 
                        default="http://fastapi:80/task1/",  # default if nothing is provided
                        help="Specify the endpoint to send the request to")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    arguments = parse_arguments()
    values_args = arguments.values
    secret_args = arguments.secret
    endpoint_args = arguments.endpoint
    values_list_args = ast.literal_eval(values_args)
    if all(isinstance(value, int) for value in values_list_args):
        main(values_list_args, secret_args, endpoint_args)
    else:
        print("Not all elements in the provided list are from type integer") 