import face_recognition
import shutil
import os


pro_photos_path = '/Users/shivam/Compass/Compass/static/user_photos'
photos_path = '/Users/shivam/Pictures/bkp/'

def move_pics(user_face_embedding, user_id, file):
    unkown_pic = os.path.join(photos_path, file)
    unknown_face = face_recognition.load_image_file(unkown_pic)
    unknown_face_encodings = face_recognition.face_encodings(unknown_face)

    for unknown_face_encoding in unknown_face_encodings:
        results = face_recognition.compare_faces([user_face_embedding],
                                                 unknown_face_encoding)
        if results[0]:
            shutil.copy(unkown_pic,
                        os.path.join(pro_photos_path,
                                     user_id,
                                     'event_photos',
                                     file))

def rec_face(user):
    profile_pic_path = os.path.join(pro_photos_path,
                                    str(user.id),
                                    'profile_photo')
    profile_pic = os.listdir(profile_pic_path)[0]
    pro_pic = os.path.join(profile_pic_path, profile_pic)   
    user_face = face_recognition.load_image_file(pro_pic)
    user_face_embedding = face_recognition.face_encodings(user_face)[0]

    for file in os.listdir(photos_path):
        try:
            move_pics(user_face_embedding, str(user.id), file)
        except Exception as e:
            print(e)