from domain.patients import  *
class Department:
    def __init__(self,id,name,number_beds):
        self.__id=id
        self.__name=name
        self.__number_bed=number_beds
        self.__list_patients=[]
        self.__number_patients=0

    def get_id(self):
        return self.__id
    def set_id(self,id):
        self.__id=id

    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name

    def get_number_beds(self):
        return self.__number_bed
    def set_number_beds(self,number_beds):
        self.__number_bed=number_beds

    def get_list_patients(self):
        return self.__list_patients

    def get_number_patient(self):
        return self.__number_patients

    '''
    description: the function adds patients in department
    input: the patients data
    output: if the department is full it return a message 
        '''
    def add_patient(self,patient):
        if self.__number_patients < self.__number_bed:
            self.__list_patients.append(patient)
            self.__number_patients+=1
        else:
            print("The department is full")

    '''
    description:updates a patient by the index
    input: index: the index we want to update the patient
            f_name: new first name
            l_name= new last name
            pers_code= ew personal code
            disease: new disease
    output: the list with the names
    '''
    def update_patient_given_index(self,index,f_name,l_name,pers_code,disease):
        for i in range(len(self.__list_patients)):
            if index==i:
                self.__list_patients[i].set_f_name(f_name)
                self.__list_patients[i].set_l_name(l_name)
                self.__list_patients[i].set_personal_code(pers_code)
                self.__list_patients[i].set_disease(disease)
        return

    def __del__(self):
        delete=1

    '''
    description: the function deletes a patient from a given index from a department
    input: the index where you want to delete the patient
    output: the list of patients without the index'th patient
    '''
    def delete_patient_given_index(self,index):
        for i in range(len(self.__list_patients)):
            if i==index:
                del self.__list_patients[index]
        return self.__list_patients


    '''
    description: the function sorts patients in department by their personal numeric code
    input: nothing
    output: the sorted list of patients
    '''
    def sort_patient_by_personal_code(self):
        self.__list_patients=sorted(self.__list_patients, key=lambda patient: patient.get_personal_code())

    '''
    description: the function finds departments  with patients' age under a given value
    input: number: the number we compare the age of the patient with
           month: the month we want to see if he is older or not
           day: we want to verify is he is older or not from a given date constructed by the month and day which belong to the year 2024
    output: a new list with the name of the departments that varifies the conditions
    '''
    def number_patients_with_age_above(self,number,month,day):
        final_number=0 #the number of patients with the age above the given number
        for patient in self.__list_patients:
            prefix_pers_code=patient.get_personal_code()//1000000
            if (prefix_pers_code//1000000==1 or prefix_pers_code//1000000==2):
                prefix_pers_code=prefix_pers_code%1000000//10000
                age=2024-1900
                age=age-prefix_pers_code
            else:
                prefix_pers_code = prefix_pers_code % 1000000
                prefix_pers_code = prefix_pers_code // 10000
                age=2024-2000-prefix_pers_code
            if (prefix_pers_code//100)%100<month and prefix_pers_code%10<day:  # I verifi if the person celebrated his birtday this year
                age -= 1
            if age>number:
                final_number+=1
        return final_number

    '''
    description: the function sorts patients in a department alphabetically
    input: nothing
    output: the new department with the patients sorted 
    '''
    def sort_patients_alphabetically(self):
        self.__list_patients=sorted(self.__list_patients, key=lambda patient: (patient.get_f_name(),patient.get_l_name()))
        #return self.__list_patients

    '''
    description: the function sorts patients in a department by a given string
    input: the string
    output: the new department with the patients sorted 
    '''
    def get_patients_string(self,string):
        new_patients=[]
        for patient in self.__list_patients:
            if string.lower() in (patient.get_f_name()+" "+patient.get_l_name()).lower():
                new_patients.append(patient)
        return new_patients

    '''
    description: the function wants to pint just the patients without the departments
    input: none
    output: patients as lists 
    '''
    def print_patients(self):
        for patient in self.__list_patients:
            print(patient)
    '''
    description:the function counts how many patients there are with a specific disease
    input: the disease
    output: the final count
    '''
    def get_patients_with_same_disease_count(self, disease):
        k=0
        for patient in self.__list_patients:
            if patient.get_disease()==disease:
                k+=1
        return k

    def __str__(self):
        patients_list="\n".join(str(patient) for patient in self.__list_patients)
        return f"Id:{self.__id}, Name of department: {self.__name} \n"\
               f"Number of beds in the department:{self.__number_bed} \n"\
               f"List of patients: "\
               f" \n{patients_list} "\
               f"\n"
