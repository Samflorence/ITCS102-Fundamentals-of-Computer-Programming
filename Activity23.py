anime = ['one piece','naruto','solo leveling','dan da dan']
print(anime)
print(anime[3])
print(anime[2 : 4])

#adding item
anime.append('death note')
print(anime)

anime.insert(2 , 'jujutsu kaisen')
print(anime)

#Removing item
anime.remove('naruto')
print(anime)

anime.pop() #remove last
print(anime)

#determine the number of items in a list 
print(len(anime))

#sorting
anime.sort()
print(anime)

anime.reverse()
print(anime)