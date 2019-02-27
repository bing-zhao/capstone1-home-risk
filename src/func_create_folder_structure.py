# function to create folder structure
def func_create_folder_structure(PATH):
    """function to create a folder structure
    Keyword arguments: PATH (project directory); Return: SubFoldersList
    """
    # prepare a folder structure
    import os
    SubFolders=['data/external','data/interim','data/processed','data/raw',
    'reports/figures','src']
    # 'src','src/data','src/data/raw','src/data/int','src/features','src/models','src/visualization','test']
    SubFoldersList = []
    for f in SubFolders:
        dirName = PATH+f
        SubFoldersList.append(dirName)
        os.makedirs(dirName, exist_ok=True)
        # try:
        # except FileExistsError:
        #     print("Directory " , dirName ,  " already exists")
    print(len(SubFoldersList))
    return tuple(SubFoldersList)

# example
# func_create_folder_structure('C:/Users/Admin/Dropbox/development/kaggle-2018-home-credit/src/test')
