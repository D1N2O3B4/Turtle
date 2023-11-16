from urllib import request
import numpy as np

request.urlretrieve('https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv',
                    'climate.txt')
csv_var = np.genfromtxt('climate.txt',delimiter=",",skip_header=1)
print(csv_var)

weights = np.array([0.3, 0.2, 0.5])

end_val = csv_var @ weights
print(end_val.shape)

csv_var_final = np.concatenate((csv_var,end_val.reshape(10000,1)),axis=1)
print(csv_var_final)

a = np.array([12,34,55,8,10,90])
b = np.array([[34,21],[233,12],[5,1],[0,9],[78,15],[44,6]])

c = np.concatenate((a.reshape(6,1),b),axis=1)
print(c)

ap = np.array([[56,12],[77,88],[90,33]])
bp = np.array([[11,22,55]])
cp = np.concatenate((ap,np.transpose(bp)),axis=1)
print(cp)

np.savetxt('climatenew.txt',csv_var_final,delimiter=',',fmt="%.2f",header='temperature,rainfall,humidity,yeild_apples')