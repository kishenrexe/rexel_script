from getfiles import getfiles
from processfile import processfile

def main():
    files = getfiles('Etimklassedz')
    i = 0
    while i < len(files):
        processfile(files[i])

        
        i= i + 1
    
    



main()

