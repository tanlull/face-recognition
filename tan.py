import face_recognition
known_image = face_recognition.load_image_file("tan.jpg")
face_locations = face_recognition.face_locations(known_image)
# face_encoding = face_recognition.face_encodings(face_locations)[0]

# unknown_Pic = face_recognition.load_image_file("tan1.jpg")
# unknown_face_encoding = face_recognition.face_encodings(unknown_Pic)[0]

# results = face_recognition.compare_faces([face_encoding], unknown_face_encoding)

# if results[0] == True:
#      print("It’s Tanya")
# else:
#     print("Unknow")