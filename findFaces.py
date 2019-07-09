import face_recognition

image = face_recognition.load_image_file('./img/groups/team1.jpg')

#get location of images

face_locations = face_recognition.face_locations(image)

#array of cordinates of each face

print(face_locations)
# print(f'There are {len(face_locations)} people in this image')