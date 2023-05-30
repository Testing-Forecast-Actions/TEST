import os


def run ():
    print ("Running check")
    jsonInputFile = "../assets/repo_access_mapping.json"
    with open(jsonInputFile) as f_json_input:
        j_in = json.load(f_json_input)
        if j_in == None :
            print("Failed to open input file")
        else :
            print("Input file opened: {}".format(j_in))



if __name__ == "__main__":
    print ("Testing script")
    run()
