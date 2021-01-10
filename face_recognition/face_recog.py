import face_recognition 

image1 = face_recognition.load_image_file("sam_picture/sam_2.jpg")
height, width, _ = image1.shape
# location is in css order - top, right, bottom, left
face_location = (0, width, height, 0)

my_face_encoding1 = face_recognition.face_encodings(image1, known_face_locations=[face_location])[0]


# load another pic
image2 = face_recognition.load_image_file("sam_picture/sam_3.jpg")

height, width, _ = image2.shape
# location is in css order - top, right, bottom, left
face_location = (0, width, height, 0)

my_face_encoding2 = face_recognition.face_encodings(image2, known_face_locations=[face_location])[0]

# let compare sam_1 with sam_2 (should be very similar theoretically)
results = face_recognition.compare_faces([my_face_encoding1], my_face_encoding2)

if results[0]==True:
    print('He is Sam')
else:
    print('He is not Sam')