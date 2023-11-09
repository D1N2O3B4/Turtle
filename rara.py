import urllib.request as url
import numpy as np


url.urlretrieve('https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv', 
    'climate.txt')

data = np.genfromtxt('climate.txt',delimiter=',',skip_header=1)

print(data)