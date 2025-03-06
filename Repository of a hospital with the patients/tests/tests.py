from repository.hospital import *


def test_add_patient():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    department1 = Department(1, 'Urgent', 10)
    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)

    h_rep.add_department(department1)

    assert department1.get_list_patients()[0].get_f_name()=='Ana'
    assert department1.get_id()[1].get_disease()=='cough'
    assert department1.get_list_patients()[0].get_l_name()=="Popa"

def update_patient_given_index():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    department1 = Department(1, 'Urgent', 10)
    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)

    h_rep.add_department(department1)
    department1.update_patient_given_index(0,'Andrei','Oltean','1900621154741','cough')
    assert department1.get_list_patients()[0].get_f_name()=='Andrei'
    assert department1.get_list_patients()[0].get_l_name()=='Oltean'
    assert department1.get_list_patients()[0].get_pers_code()!=19542185742

def delete_patient_given_index():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    department1 = Department(1, 'Urgent', 10)
    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)

    h_rep.add_department(department1)
    department1.delete_patient_given_index(1)
    assert department1.get_list_patients()[1].get_f_name()=='Vlad'
    assert department1.get_list_patients()[1].get_pers_code()==5051259201368
    assert department1.get_list_patients()[1].get_l_name()!='Cristea'

def sort_patient_by_pers_code():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    department1 = Department(1, 'Urgent', 10)
    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)

    h_rep.add_department(department1)
    department1.sort_patient_by_personal_code()
    assert department1.get_list_patients()[1].get_f_name()=='Vlad'
    assert department1.get_list_patients()[0].get_f_name()=='Oana'
    assert department1.get_list_patients()[2].get_f_name()=='Ana'

def test_sort_patients_age_above():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    department1 = Department(1, 'Urgent', 10)
    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)

    h_rep.add_department(department1)
    assert department1.number_patients_with_age_above(2,1,11)==3
    assert department1.number_patients_with_age_above(18,1,11)==2
    assert department1.number_patients_with_age_above(50,1,11)==1

def test_sort_by_number_patients():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    department1 = Department(1, 'Urgent', 10)
    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)

    h_rep.add_department(department1)

    patient7 = Patient("Maria", 'Popescu', 6020315236415, 'stomachache')
    patient8 = Patient('Daria', 'Rus', 2920310230154, 'otitis')
    department2 = Department(2, 'Neuro', 30)

    department2.add_patient(patient7)
    department2.add_patient(patient8)

    h_rep.add_department(department2)
    h_rep.sort_by_number_patients()
    assert h_rep.print_department()[0]=='Neuro'
    assert h_rep.print_department()[1]=='Urgent'
    assert h_rep.print_department()[1]!='Cardio'

def test_get_patients_string():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    department1 = Department(1, 'Urgent', 10)
    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)

    h_rep.add_department(department1)
    assert department1.get_patients_string('z')==[]
    assert department1.get_patients_string('v').get_f_name()=='Vlad'
    assert department1.get_patients_string('m').get_f_name()=='Vlad'

def test_sort_patients_alphabethically():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    department1 = Department(1, 'Urgent', 10)
    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)

    h_rep.add_department(department1)
    department1.sort_patients_alphabetically()
    assert department1.get_list_patients()[0].get_f_name()=='Ana'
    assert department1.get_list_patients()[1].get_f_name()=='Oana'
    assert department1.get_list_patients()[2].get_f_name()=='Vlad'
def test_add_department():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    department1 = Department(1, 'Urgent', 10)
    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)

    h_rep.add_department(department1)

    patient7 = Patient("Maria", 'Popescu', 6020315236415, 'stomachache')
    patient8 = Patient('Daria', 'Rus', 2920310230154, 'otitis')
    department2 = Department(2, 'Neuro', 30)

    department2.add_patient(patient7)
    department2.add_patient(patient8)

    h_rep.add_department(department2)
    assert h_rep.print_department()[0]=='Urgent'
    assert h_rep.print_department()[1]=='Neuro'
    assert h_rep.print_department()[2]==[]

def test_sort_departments_by_number_patients_above_given_value():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    department1 = Department(1, 'Urgent', 10)
    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)

    h_rep.add_department(department1)

    patient7 = Patient("Maria", 'Popescu', 6020315236415, 'stomachache')
    patient8 = Patient('Daria', 'Rus', 2920310230154, 'otitis')
    department2 = Department(2, 'Neuro', 30)

    department2.add_patient(patient7)
    department2.add_patient(patient8)

    h_rep.add_department(department2)
    h_rep.sort_departments_by_number_patients_above_given_value(20,1,11)
    assert h_rep.print_department()[0]=='Neuro'
    assert h_rep.print_department()[1]=='Urgent'
    assert h_rep.print_department()[2]==[]

def test_identify_departments_patients_under_age():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    department1 = Department(1, 'Urgent', 10)
    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)

    h_rep.add_department(department1)

    patient7 = Patient("Maria", 'Popescu', 6020315236415, 'stomachache')
    patient8 = Patient('Daria', 'Rus', 2920310230154, 'otitis')
    department2 = Department(2, 'Neuro', 30)

    department2.add_patient(patient7)
    department2.add_patient(patient8)

    h_rep.add_department(department2)
    h_rep.identify_departments_patients_under_age(20,1,11)
    assert h_rep.print_department()[0]=='Urgent'
    assert h_rep.print_department()[1]==[]
    assert h_rep.print_department()[2]==[]

def test_get_patients_in_department_first_last_name():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    department1 = Department(1, 'Urgent', 10)
    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)

    h_rep.add_department(department1)

    patient7 = Patient("Maria", 'Popescu', 6020315236415, 'stomachache')
    patient8 = Patient('Daria', 'Rus', 2920310230154, 'otitis')
    department2 = Department(2, 'Neuro', 30)

    department2.add_patient(patient7)
    department2.add_patient(patient8)

    h_rep.add_department(department2)
    assert h_rep.get_patients_in_department_first_last_name(department1,'ana')[0].get_f_name()=='Ana'
    assert h_rep.get_patients_in_department_first_last_name(department1,'ana')[1].get_f_name()=='Oana'
    assert h_rep.get_patients_in_department_first_last_name(department1,'ana')[1].get_f_name()!='dana'

def test_get_patients_by_first_name():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    department1 = Department(1, 'Urgent', 10)
    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)

    h_rep.add_department(department1)

    patient7 = Patient("Maria", 'Popescu', 6020315236415, 'stomachache')
    patient8 = Patient('Daria', 'Rus', 2920310230154, 'otitis')
    department2 = Department(2, 'Neuro', 30)

    department2.add_patient(patient7)
    department2.add_patient(patient8)

    h_rep.add_department(department2)
    assert h_rep.get_patients_by_first_name('Ana').get_pers_code()==6040412235486
    assert h_rep.get_patients_by_first_name('Maria').get_pers_code()==6020315236415
    assert h_rep.get_patients_by_first_name('Vlad').get_pers_code()==5051259201368
def tests():
    test_sort_by_number_patients()
    test_add_patient()
    update_patient_given_index()
    delete_patient_given_index()
    sort_patient_by_pers_code()
    test_sort_patients_age_above()
    test_get_patients_string()
    test_add_department()
    test_sort_patients_alphabethically()
    test_sort_departments_by_number_patients_above_given_value()
    test_identify_departments_patients_under_age()
    test_get_patients_in_department_first_last_name()
    test_get_patients_by_first_name()