def getfiles(filename):
    cleaned_files = []
    with open(f'{filename}.txt','r') as f_in:
        for line in f_in:
            modified_line = line.strip()[:-1]
            cleaned_files.append(modified_line)
    return cleaned_files

