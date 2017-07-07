# cites = ['Adelaide','Alice Springs','Darwin','Melbourne', 'Sydney']

# with open('./cites.txt', 'w') as cites_file:
#     for city in cites:
#         print(city, file=cites_file)

# =========================================================

with open('imelda3.txt', 'r') as music_file:
    content = music_file.readline()

imelda3 = eval(content)

print(imelda3)

title, artist, album, tracks = imelda3

print(title)
print(artist)
print(album)
print(tracks)
