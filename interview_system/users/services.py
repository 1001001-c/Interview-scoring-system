# services.py
import csv
from .models import Candidate, UserProfile

def process_csv_files(examiners_file, candidates_file):
    if examiners_file:
        process_examiners_csv(examiners_file)
    if candidates_file:
        process_candidates_csv(candidates_file)

def process_examiners_csv(file):
    file_data = file.read().decode('utf-8').splitlines()
    reader = csv.reader(file_data)
    next(reader)  # Skip header if needed

    for row in reader:
        full_name, id_number = row
        username = full_name.lower().replace(' ', '')
        password = id_number[-6:]
        if UserProfile.objects.filter(username=username).exists():
            username += str(UserProfile.objects.filter(username__startswith=username).count() + 1)
        UserProfile.objects.create(username=username, password=password, full_name=full_name, role='evaluator')

def process_candidates_csv(file):
    file_data = file.read().decode('utf-8').splitlines()
    reader = csv.reader(file_data)
    next(reader)  # Skip header if needed
    
    for row in reader:
        full_name, id_number, gender = row
        if gender not in dict(Candidate.GENDER_CHOICES).keys():
            continue  # 或者处理无效性别的情况
        Candidate.objects.create(full_name=full_name, id_number=id_number, gender=gender)

def get_candidate_info(id_number):
    return Candidate.objects.filter(id_number=id_number).first()