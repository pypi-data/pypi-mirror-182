import sys, getopt
import fileinput
import os
def main(arg):
    if arg[2] == 'project' and arg[1] == '--create':
        ProjectCreator(arg[4])
    if arg[2] != 'project' and arg[1] == '--create':
        SRCCreator(arg[2], arg[4], arg[6])

class ProjectCreator():
    def __init__(self, project_name) -> None:
        try:
            self.set_project_name(project_name)
            if not os.path.exists(os.path.join("", project_name)):
                os.mkdir(os.path.join(os.getcwd(),project_name))
        except Exception as err: 
            message = f"Error While Creating Project: {err}"
            print(message)
            return
        try:
            self.set_directories_paths()
        except Exception as err:
            message = f"Error While Setting Directories List: {err}"
            print(message)
            return
        try:
            self.set_files_paths()
        except Exception as err:
            message = f"Error While Setting Files List: {err}"
            print(message)
            return
        try:
            self.directories_creator()
        except Exception as err:
            message = f"Error While Creating Directories: {err}"
            print(message)
            return
        try:
            self.files_creator()
        except Exception as err:
            message = f"Error While Creating Files: {err}"
            print(message)
            return
        print("Project Was Created Successfully...")

    def set_directories_paths(self):
        self.directories_paths = ['src', 'src/service', 'src/api',
                                    'src/controller', 'storage',
                                    'storage/files', 'storage/media'
                                ]
        
    def get_directories_paths(self):
        return self.directories_paths
    
    def set_files_paths(self):
        self.files_paths = ['src/main.py', 'src/service/service_main.py',
                                'src/controller/controller_main.py',
                                'src/api/api_main.py', 'Dockerfile',
                                'docker-compose.yml', '.dockerignore',
                                '.gitignore', 'README.md'
                            ]
    def get_files_paths(self):
        return self.files_paths

    def set_project_name(self, project_name):
        self.project_name = project_name
    
    def get_project_name(self):
        return self.project_name
    
    def set_project_path(self, project_name):
        self.project_path = os.path.join(os.getcwd(), f"{project_name}")
    
    def get_project_path(self):
        return self.project_path
    
    def directories_creator(self):
        sal_directories = self.get_directories_paths()
        for dir in sal_directories:
            project_name = self.get_project_name()
            dir_path = f"{project_name}/{dir}"
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

    def files_creator(self):
        sal_files = self.get_files_paths()
        for file in sal_files:
            project_name = self.get_project_name()
            file_path = f"{project_name}/{file}"
            with open(os.path.join(file_path), 'w') as file:
                pass

class SRCCreator():
    def __init__(self, type, name, project) -> None:
        service_location = os.path.join(f"{project}/src/{type}")
        service_name = os.path.join(f"{service_location}/{name}_{type}")
        if not os.path.exists(service_name):
                os.mkdir(service_name)
        with open(f"{service_name}/{name}.py", 'w') as python_file:
            pass
        with open(f"{service_location}/{type}_main.py", 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            line = f"import {name}_{type}.{name} as {name}"
            f.write(line.rstrip('\r\n') + '\n' + content)
        
if __name__ == "__main__":
    pass