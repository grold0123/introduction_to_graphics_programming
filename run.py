import subprocess,pathlib,sys


base_dir = pathlib.Path(r'C:\projects\introduction_to_graphics_programming')
src_dir = base_dir/'src'
build_dir = base_dir/'build'



project_name = sys.argv[1]
if project_name:
    projects = [path.name for path in src_dir.iterdir()]
    if project_name in projects:
        project_dir = src_dir/project_name
        cpp_files = [str(cpp) for cpp in project_dir.glob("*.cpp")]
        include = base_dir/'include'
        lib = base_dir/'lib'        
        project_build = str(build_dir/project_name)+".exe"
        if include in project_dir.iterdir() and lib in project_dir.iterdir(): 
            args = [
                    'g++',
                    *cpp_files,
                    '-Iinclude',
                    '-Llib',
                    '-o',
                    project_build
                ]
            print("\n\n\t**BUILDING PROJECT**\n\n")
            result = subprocess.run(args)
            if result.returncode == 0:
                subprocess.run(project_build)
        else: 
            print("\n\n\t**Include and Lib folders does not exist Creating them now**\n\n")
            include.mkdir(exist_ok=True)
            lib.mkdir(exist_ok=True)
            args = [
                    'g++',
                    *cpp_files,
                    '-Iinclude',
                    '-Llib',
                    '-o',
                    project_build
                ]
            print("\n\n\t**BUILDING PROJECT**\n\n")
            result = subprocess.run(args)
            if result.returncode == 0:
                subprocess.run(project_build)
    else: print("\n\n\t**Project not found**\n\n")
