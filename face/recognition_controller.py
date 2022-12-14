import os
import time
import numpy as np
import face_recognition

def load_known_data(encoding_filename, records_filename):

    with open(encoding_filename, 'rb') as f:
        known_face_encodings = np.load(f)

    with open(records_filename, 'rb') as f:
        employee_records = np.load(f, allow_pickle='TRUE')
    
    return [known_face_encodings, employee_records]

def learn_unknown_face(unknown_face_path):
    unknown_face_image = face_recognition.load_image_file(unknown_face_path)
    try:
        unknown_face_encoding = face_recognition.face_encodings(unknown_face_image)[0]
        print(f"{unknown_face_path.split('/')[-1]} loaded with shape: {np.shape(unknown_face_image)}")
    except IndexError:
        print("Unable to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()

    return unknown_face_encoding

def lookup_employee(employee_records, ref_index):
    for employee in employee_records.keys():
        if ref_index in employee_records[employee]:
            return employee
    return 'Employee not found'

def find_closest_match(known_face_encodings, unknown_face_encoding, employee_records, threshold=0.5):
    start_time = time.time()
    distances = face_recognition.face_distance(known_face_encodings, unknown_face_encoding)
    closest_distance = np.min(distances)
    results = 'Face does not match with database'
    if closest_distance < threshold:
        results = lookup_employee(employee_records, np.argmin(distances))
    print(f"Time taken to recognize: {time.time() - start_time}")
    return results

def recognition_controller(unknown_face_path):
    encoding_filename = './learned_data/known_encodings.npy'
    records_filename = './learned_data/employee_records.npy'

    known_face_encodings, employee_records = load_known_data(encoding_filename, records_filename)
    unknown_face_encoding = learn_unknown_face(unknown_face_path)
    recognition = find_closest_match(known_face_encodings, unknown_face_encoding, employee_records, threshold=0.5)
    return recognition

