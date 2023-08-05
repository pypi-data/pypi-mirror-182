import sys, getopt
import command_executer

def main(argv):
    args_processing(argv)

def args_processing(argv):
    print(argv)
    if argv[1] not in ["--create"]:
        print("This Command Is Not Available")
        return
    if argv[2] not in ["project", "api", "controller", "service"]:
        print("This Type Is Not Available")
        return
    if argv[3] not in ["--name"]:
        print("This Command Is Not Available")
        return
    if argv[5] not in ["--project"]:    
        try:
            if argv[5] not in ["--project"]:
                print("This Command Is Not Available")
                return 
        except IndexError:
            argv.append("--project")
            argv.append("NewProjectToken")
    else:
        command_executer.main(argv)
if __name__ == "__main__":
    pass