# this program reader json files from out-text folder
# and outputs their [] responses > {} 0 >fullTextAnnotation > text filed
import json
import os
import re

# read json file
def read_json(file_name):    
    with open(file_name, encoding="utf-8") as f:
        data = json.load(f)
    return data 


# sorts returned file in order 1-n
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)


# this function returns all files in a directory
def get_files(directory):
    files = []
    for file in os.listdir(directory):
        if file.endswith(".json"):
            files.append(file)
    return files

# get html from json data
def getHtml(jsondata):
    pagehtml = ""
    total_pages = 0
    i = 0
    # check if there is any OCR data in the json file
    if 'fullTextAnnotation' in jsondata['responses'][0]:
        #print("number : " + str(len(jsondata['responses'][0]['fullTextAnnotation']['pages'][0]['blocks'])))
        for page in jsondata['responses']: # each file can have multiple pages
            pagehtml = pagehtml + "<div class='page'>" + page['fullTextAnnotation']['text'] + "</div>"
            total_pages = total_pages + 1
    pagehtml = pagehtml.replace("\n", "<br/>")
    return pagehtml, total_pages

# Final function, read json file, convert to html and save to file.
def saveHtml(json_folder_name, new_file_name):
    jfiles = get_files(json_folder_name)
    total_pages = 0
    #sort the files alphabetically
    jfiles = natural_sort(jfiles)
    pages = ""
    for f in jfiles:
        print(f)
        jdata = read_json(json_folder_name + "/" + f)
        page_data  = getHtml(jdata)
        pages = pages + page_data[0]
        total_pages = total_pages + page_data[1]
    with open(new_file_name, "w", encoding="utf-8") as f:
        # attach stylesheet (style.css) to html
        withCSS = "<html><head><link rel='stylesheet' href='style.css'></head><body>" + pages + "</body><html>"
        f.write(withCSS)
    print(new_file_name + " saved." + "\n" + "Total pages: " + str(total_pages))


# main function
if __name__ == "__main__":
    saveHtml("jw-book-out", "jw-book-out.html")

