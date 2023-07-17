import os
import json
import sys

#
def getEnvInfo ():

    env_file = os.getenv('GITHUB_ENV')

    test_var = os.getenv('Test_Parameter')

    print ("Test parameter from env: {}".format(test_var))

    with open(env_file, "a") as myfile:
        myfile.write("MY_VAR=MY_FLUCAST_VALUE")
        print ("MyFile: {}".format(myfile))

#
def getInputFromOutput():
    env_file = os.getenv('GITHUB_OUTPUT')

    
    # actor = os.getenv("gh-actor")
    # repo = os.getenv("gh-repo")
    # pr_number = os.getenv("pr-number")
    # changes = os.getenv("all-changes")
    # test_p = os.getenv("test-p")
    with open (env_file, 'r') as gh_env_file:
        print ("OUTPUT content read START>>>>>>>>>> ")
        print (gh_env_file.read())
        print ("OUTPUT content read STOP >>>>>>>>>> ")
    


#
def getInputFromEnv ():
    
    env_file = os.getenv('GITHUB_ENV')

    
    # actor = os.getenv("gh-actor")
    # repo = os.getenv("gh-repo")
    # pr_number = os.getenv("pr-number")
    # changes = os.getenv("all-changes")
    # test_p = os.getenv("test-p")
    with open (env_file, 'r') as gh_env_file:
        print ("Env content read START>>>>>>>>>> ")
        print (gh_env_file.read())
        print ("Env content read STOP >>>>>>>>>> ")

    # print ("Input info -> \nactor: {0}, \nrepo: {1}, \npr num: {2}, \nchanges: {3}".format(actor, repo, pr_number, changes))


#
def run (jsonInputFile):

    print ("Running check")

    getInputFromEnv()
    getInputFromOutput()

    with open(jsonInputFile) as f_json_input:
        j_in = json.load(f_json_input)
        if j_in == None :
            print("Failed to open input file")
        else :
            print("Input file opened: {}".format(j_in))

        teams = j_in['mapping']['teams']

        for team in teams:
            print ("Team content: {}".format(team))



if __name__ == "__main__":
    print ("Testing script")

    # if len(sys.argv) <= 1 :
    #   print ("Missing input. Abort!")
    #   exit(0)

    # input_data_json = sys.argv[1]
    # print ("Input data: \n {}".format(input_data_json))

    runningPath = os.path.dirname(__file__)

    jsonInputFile = os.path.join(runningPath, '..', 'assets', 'repo_access_mapping.json')

    print ("Running path: {0}, file: {1}".format(runningPath, jsonInputFile))
    run(jsonInputFile)
