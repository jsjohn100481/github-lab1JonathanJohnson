import json

def search_json(json_data, search_string):
    
    results = []
    for x in json_data:
        #print(len(x))
        if(x["User"] == search_string):
            results.append(x)
            print ("success")

                
    # Place your search code here
    # you will have to loop through the json_data file you created earlier
    # finally you can store the match in the result list and return it
    return results