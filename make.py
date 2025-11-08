import subprocess,pathlib,sys



base_dir = pathlib.Path(r'C:\projects\introduction_to_graphics_programming')
src_dir = base_dir/'src'

project_name = sys.argv[1]
if project_name:
    project_dir = src_dir/project_name
    project_dir.mkdir(exist_ok=True)
    main_cpp = project_dir/'main.cpp'
    main_cpp.touch(exist_ok=True)
    with open(main_cpp,'w') as file:
        file.write(f'//{project_name}\n\nint main ()'+'{'+'}')
    print("\n\n**Opening main cpp file\n\n**")
    subprocess.run(['code',str(main_cpp)])