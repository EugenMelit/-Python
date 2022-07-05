x = 'abcdefghijklmnopqrstuvwxyz'
y = input('Input strings:\n')
for i in x:
    count =0
    for r in y:
        if i == r:
            count += 1
    if count > 0:
            print('Leter', i,'was', count)
    
