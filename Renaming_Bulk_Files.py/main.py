import os

def rename_files(directory, newname): 
    files = os.listdir(directory) ##used to get the list of all files and directoreis in the spcefied directory 
    counter = 0 
    for file in files: 
        filetype =  file.split('.')[-1]
         ##split the text into wordds 
        ##-1 will remove the file type after the last dot 
        os.rename(directory + '/' + file, directory + '/' + newname + str(counter) + '.' + filetype)
        # renmae() renames the file or directory src to dst
        print("Renaming " + file + "to" + newname + str(counter) + "." + filetype)
        counter += 1

rename_files("/Users/josephina/Desktop/testdir", "mynewname")