import os


for i in range(1, 15):
    path = 'm' + str(i)
    if not os.path.exists(path):
        os.makedirs(path)
        os.chdir(os.getcwd() + '/' + path)
        open(path + '.docx', 'a').close()
        os.chdir('..')
    else:
        print(os.getcwd())
print('done')