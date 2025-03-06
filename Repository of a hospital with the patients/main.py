from repository.hospital import *

def print_menu():
    menu=('\t Menu:\n'
          '\t 1. CRUD operations \n'
          '            \t 1.1 Print the Hospital\n'
          '            \t 1.2 Departments \n'
          '                 \t 1. Add a department to the Hospital\n'
          '                 \t 2. Update a department in the Hospital\n'
          '                 \t 3. Delete a department\n'
          '             \t 1.3 Patients\n'
          '                     \t 1.3.1 Add a patient\n'
          '                     \t 1.3.2 Update a patient\n'
          '                     \t 1.3.3 Delete a patient\n'
          '\t 2. Sort the patients in a department by personal numeric code\n'
          '\t 3. Sort departments by the number of patients\n'
          '\t 4. Sort departments by the number of patients having the age above a given limit\n'
          '\t 5. Sort departments by the number of patients and the patients in a department alphabetically\n'
          '\t 6. Identify departments where there are patients under a given age\n'
          '\t 7. Identify patients from a given department for which the first name or last name contain a given string\n'
          '\t 8. Identify department/departments where there are patients with a given first name\n'
          '\t 9. Form groups of 𝒌 patients from the same department and the same disease\n'
          '\t 10. Form groups of 𝒌 departments having at most 𝒑 patients suffering from the same disease \n'
          '\t 0. Quit \n')
    print(menu)

def start():
    h_rep = Hospital()

    patient1 = Patient("Ana", "Popa", 6040412235486, 'fever')
    patient2 = Patient('Oana', 'Cristea', 2750232547891, 'cough')
    patient3 = Patient('Vlad', 'Metea', 5051259201368, 'cough')
    patient4 = Patient('Cristian', 'Molnar', 1960698125478, 'otitis')
    patient5 = Patient('Matei', 'Pacurar', 5100698125478, 'otitis')
    patient6 = Patient('Marius', 'Pacurar', 1900528514204, 'stomachache')

    department1 = Department(1, 'Urgent', 10)

    department1.add_patient(patient1)
    department1.add_patient(patient2)
    department1.add_patient(patient3)
    department1.add_patient(patient4)
    department1.add_patient(patient5)
    department1.add_patient(patient6)

    patient7 = Patient("Maria", 'Popescu', 6020315236415, 'stomachache')
    patient8 = Patient('Daria', 'Rus', 2920310230154, 'otitis')
    patient9 = Patient('Mihai', 'Gherman', 5000698125478, 'cough')
    patient10 = Patient('Cristian', 'Avram', 1551110125478, ' nausea')
    patient11 = Patient('Dana', 'Avram', 6051130152465, ' nausea')

    department2 = Department(2, 'Neuro', 30)

    department2.add_patient(patient7)
    department2.add_patient(patient8)
    department2.add_patient(patient9)
    department2.add_patient(patient10)
    department2.add_patient(patient11)

    patient12=Patient('Ana','Nistor',605101288532,"diabetes")
    patient13=Patient('Luiza','Chenti',285062285212,"heart failure")
    patient14=Patient('Ana','Ordean',6040822658416,"diabetes")
    patient15=Patient('Andreea','Marginean',6041130011151,"heart failure")

    department3=Department(3,"Cardiology",44)

    department3.add_patient(patient12)
    department3.add_patient(patient13)
    department3.add_patient(patient14)
    department3.add_patient(patient15)

    h_rep.add_department(department1)
    h_rep.add_department(department2)
    h_rep.add_department(department3)

    print_menu()
    stop=False
    while stop==False:
        option=input("give an option: ")
        if option=='1':
            print(h_rep)
            choice=input("choose the one you want to modify things: Department or Patient \n")
            if choice=='Department':
                h_rep.print_department()
                cooption=input("give an option from the department: ")
                if cooption=='1':
                    department=input("Give the name of the department: ")
                    id=input("Give the id of the department "+department)
                    number_beds=int(input("Give the number of the beds in the department "+department))
                    new_department=Department(id,department,number_beds)
                    n=int(input("give the number of the patients you want to add to department "+department))
                    for i in range(n+1):
                        f_name=input("give the first name of the patient")
                        l_name=input("give the last name of the patient")
                        pers_code=input("give the personal code of the patient")
                        disease=input("give the disease of the patient")
                        patient=Patient(f_name,l_name,pers_code,disease)
                        new_department.add_patient(patient)
                    h_rep.add_department(new_department)
                    print(h_rep)
                elif cooption=='2':
                    index = int(input("give the index where you want to update the department"))
                    if index < 0 or index > h_rep.number_departments():
                        print("the index doesn't exist")
                    else:
                        department = input("Give the name of the new department: ")
                        id = input("Give the id of the new department")
                        number_beds = int(input("Give the number of the beds in the new department"))
                        h_rep.update_department_by_index(index,id,department,number_beds)
                        department4=Department(department,id,number_beds)
                        for i in range(number_beds):
                            f_name = input("give the first name of the patient")
                            l_name = input("give the last name of the patient")
                            pers_code = input("give the personal code of the patient")
                            disease = input("give the disease of the patient")
                            patient = Patient(f_name, l_name, pers_code, disease)
                            department4.add_patient(patient)
                        print(h_rep)
                elif cooption=='3':
                    index=int(input("give the index where you want to delete the department: "))
                    if index < 0 or index > h_rep.number_departments():
                        print("the index doesn't exist")
                    else:
                        h_rep.delete_department_by_index(index)
                        print(h_rep)
                else:
                    print("the cooption doesn't exist")

            else:
                h_rep.printt_patients__()
                cooption = input("give an option from the patients list: ")
                if cooption=='1':
                    ddepartment=input("give the department where you want to add a patient(Urgent or Neuro or Cardiology): ")
                    if ddepartment == 'Urgent':
                        f_name=input("give the first name of the patient: ")
                        l_name=input("give the last name of the patient: ")
                        pers_code=int(input("give the personal code of the patient: "))
                        disease=input("give the disease of the patient: ")
                        patient=Patient(f_name,l_name,pers_code,disease)
                        department1.add_patient(patient)
                        print(h_rep)
                    elif ddepartment=="Neuro":
                        f_name = input("give the first name of the patient: ")
                        l_name = input("give the last name of the patient: ")
                        pers_code = int(input("give the personal code of the patient: "))
                        disease = input("give the disease of the patient: ")
                        patient = Patient(f_name, l_name, pers_code, disease)
                        department2.add_patient(patient)
                        print(h_rep)
                    elif ddepartment=="Cardioogy":
                        f_name = input("give the first name of the patient: ")
                        l_name = input("give the last name of the patient: ")
                        pers_code = int(input("give the personal code of the patient: "))
                        disease = input("give the disease of the patient: ")
                        patient = Patient(f_name, l_name, pers_code, disease)
                        department3.add_patient(patient)
                        print(h_rep)
                    else:
                        print("the department doesn't exist")

                elif cooption=='2':
                    ddepartment = input("give the department where you want to update a patient(Urgent or Neuro o5r Cardiology): ")
                    if ddepartment=='Urgent':
                        index = int(input("give the index where you want to update the patient: "))
                        f_name = input("give the first name of the patient: ")
                        l_name = input("give the last name of the patient: ")
                        pers_code = int(input("give the personal code of the patient: "))
                        disease = input("give the disease of the patient: ")
                        department1.update_patient_given_index(index,f_name,l_name,pers_code,disease)
                        print(h_rep)
                    elif ddepartment=='Neuro':
                        index = int(input("give the index where you want to update the patient: "))
                        f_name = input("give the first name of the patient: ")
                        l_name = input("give the last name of the patient: ")
                        pers_code = int(input("give the personal code of the patient: "))
                        disease = input("give the disease of the patient: ")
                        department2.update_patient_given_index(index,f_name,l_name,pers_code,disease)
                        print(h_rep)
                    elif ddepartment == "Cardioogy":
                        index = int(input("give the index where you want to update the patient: "))
                        f_name = input("give the first name of the patient: ")
                        l_name = input("give the last name of the patient: ")
                        pers_code = int(input("give the personal code of the patient: "))
                        disease = input("give the disease of the patient: ")
                        department3.update_patient_given_index(index, f_name, l_name, pers_code, disease)
                        print(h_rep)
                    else:
                        print("the department dosn't exist")
                elif cooption=='3':
                    ddepartment = input("give the department where you want to delete a patient(Urgent or Neuro or Cardiology): ")
                    if ddepartment=='Urgent':
                        index = int(input("give the index where you want to delete the patient: "))
                        if index<0 or index>len(department1.get_list_patients()):
                            print("the index doesn't exist")
                        else:
                            department1.delete_patient_given_index(index)
                            print(h_rep)
                    elif ddepartment=='Neuro':
                        index = int(input("give the index where you want to delete the patient: "))
                        if index<0 or index>len(department2.get_list_patients()):
                            print("the index doesn't exist")
                        else:
                            department2.delete_patient_given_index(index)
                            print(h_rep)
                    elif ddepartment=='Cardiology':
                        index = int(input("give the index where you want to delete the patient: "))
                        if index<0 or index>len(department3.get_list_patients()):
                            print("the index doesn't exist")
                        else:
                            department3.delete_patient_given_index(index)
                            print(h_rep)
                    else:
                        print("the department doesn't exist")
                else:
                    print("the cooption doesn't exist")

        elif option=='2':
            stop1=False
            The_department = input("Choose a department: Urgent/ Neuro/ Cardiology/ all\n")
            while stop1==False:
                if The_department=='Urgent':
                    department1.sort_patient_by_personal_code()
                    print(h_rep)
                    stop1=True
                elif The_department=='Neuro':
                    department2.sort_patient_by_personal_code()
                    print(h_rep)
                    stop1=True
                elif The_department=='Cardiology':
                    department3.sort_patient_by_personal_code()
                    print(h_rep)
                    stop1=True
                elif The_department=='all':
                    department1.sort_patient_by_personal_code()
                    department2.sort_patient_by_personal_code()
                    department3.sort_patient_by_personal_code()
                    print(h_rep)
                    stop1 = True
                else:
                    print("The department does not exist in this Hospital")
                    The_department = input("give other department: ")
        elif option=='3':
            h_rep.sort_by_number_patients()
            print(h_rep)
        elif option=='4':
            age=int(input("give a age number you want to compare the age of the patients with "))
            month=int(input("give a month(prefferable the actuall month) "))
            day=int(input("give a day(prefferable the actuall day) "))
            department1.number_patients_with_age_above(age, month, day)
            department2.number_patients_with_age_above(age, month, day)
            department3.number_patients_with_age_above(age,month,day)
            h_rep.sort_departments_by_number_patients_above_given_value(age,month,day)
            print(h_rep)
        elif option=='5':
            h_rep.sort_alphabetically_patient()
            print(h_rep)
        elif option=='6':
            age = int(input("give a age number you want to compare the age of the patients with "))
            month = int(input("give a month(prefferable the actuall month) "))
            day = int(input("give a day(prefferable the actuall day) "))
            department1.number_patients_with_age_above(age, month, day)
            department2.number_patients_with_age_above(age, month, day)
            department3.number_patients_with_age_above(age, month, day)
            print(h_rep.identify_departments_patients_under_age(age, month, day))
        elif option=='7':
            The_department = input("Choose a department: Urgent/ Neuro/ Cardiology\n")
            if The_department!="Urgent" or The_department!="Neuro" or The_department!="Cardiology":
                print('The department does not exist')
            else:
                string=input("give the string")
                h_rep.get_patients_in_department_first_last_name(The_department,string)
        elif option=='8':
            string = input("give the name: ")
            h_rep.get_patients_by_first_name(string)
        elif option=='9':
            k=int(input("k= "))
            print("\t Groups of "+str(k)+" patients from the same department with dif disease")
            print(h_rep.groups_department_repo_disease(k,2))
        elif option=='0':
            stop=True

        else:
            print("The option does not exist")

start()
