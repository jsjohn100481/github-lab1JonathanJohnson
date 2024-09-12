import json

def search_json(json_data, search_string):
    
    results = []

    #Search function returns which "User #" was entered by User.  '#' = 1-150
    for x in json_data:
        if(x["User"] == search_string):
            results.append(x)
                            
    # Place your search code here
    # you will have to loop through the json_data file you created earlier
    # finally you can store the match in the result list and return it
    return results