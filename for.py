names = ['abdelrhman','ahmed','abdo','abdullah']

for name in names:
      if name == 'abdelrhman' or name == 'ahmed':
            #  print(names.get(name) )
            # print(f"developer name is {name}")
            # while name == "abdelrhman":
             names.remove(name)    
             names.append('abdelrhman abdullah') 
            #       # names.pop(name)
            #       # names.insert('')
            #       # print(name)
            # break
      else:
            print(name)


def firstFunction(name):
      if name in names:
            return f"your name {name} is already exists please try again "
      else:
            names.append(name)
            print(names)
            return f"your name {name} has been added successfully "



n = input('please inter your name: ')
func = firstFunction(n)
print(func)