  
import json
def split_string(string):
  
    # Split the string based on space delimiter
    list_string = string.split(' ')
      
    return list_string

def join_string(list_string):
  
    # Join the string based on '-' delimiter
    string = 'T'.join(list_string)
      
    return string
# Opening JSON file and loading the data
# into the variable data

def prepare_index_json(filename,indexname,jsonFilePath):
  with open(filename) as json_file:
    data = json.load(json_file)
  
    pdadata = data['data']
    overalldata = []
    processeddata =dict()
    duplicatedrecords = dict()
    print("duplicated records below")
    for row in pdadata:
        indexkey = row['id']
        indexline = {"index":{"_index":indexname,"_type":"_doc","_id":indexkey}}
        overalldata.append(indexline)
        if processeddata.get(indexkey) :
           duplicatedrecords[indexkey]=True
           print(indexkey)   
        else : 
         processeddata[indexkey]=True

        overalldata.append(row)
    if len(duplicatedrecords)==0 :
        print('none') 
    else:
        print("-------")
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            for data in overalldata:
                jsonf.write(json.dumps(data))
                jsonf.write('\n')
            jsonf.write('\n')


if __name__ == '__main__':
    prepare_index_json('<json file path>','<es index>','coverted.json')






    