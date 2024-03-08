
with open('Test.txt', 'r') as f: 
        read = sorted(f.readlines())
with open('Test.txt', 'w') as fb: 
        fb.writelines(read)

    