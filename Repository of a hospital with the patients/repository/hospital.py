from repository.departments import *
class Hospital:
    def __init__(self):
        self.__hospital=[]

    '''
    description: adds a new department to the hospital
    input: the department
    output: nothing
    '''
    def add_department(self,departments):
        self.__hospital.append(departments)

    '''
    description: the name of the  departments
    input: none
    output: the list with the names
    '''
    def print_department(self):
        new=[]
        for department in self.__hospital:
            new.append(department.get_name())
        print(new)

    '''
    description: the number of the departments
    input: none
    output: how many departments has the hosptal
    '''
    def number_departments(self):
        k=0
        for department in self.__hospital:
            k+=1
        return k

    '''
    description: the patients data
    input: none
    output: the list with the patients
    '''
    def printt_patients__(self):
        for department in self.__hospital:
            department.print_patients()


    '''
    description: the function updates a department by the index
    input: the index where you want to update the department
    output: the list of department updated
    '''
    def update_department_by_index(self,index,id,name,number_beds):
        # for i in range(len(self.__hospital)):
        #     if index==i:
        #         self.__hospital[i].set_id(id)
        #         self.__hospital[i].set_name(name)
        #         self.__hospital[i].set_number_beds(number_beds)
        self.__hospital[index]=Department(id,name,number_beds)
                # department = self.__hospital[index]
                # department.set_id(id)
                # department.set_name(name)
                # department.set_number_beds(number_beds)
        return self.__hospital

    '''
    description: the function updates a pacient from a department
    input: the index where you want to delete the patient
    output: the list of patients without the index'th patient
    '''

    def __del__(self):
        delete=1
    '''
    description: the function deletes a department by the id of the departments
    input: the id of the department you want to delete
    output: the hospital without the id'th patient
    '''
    def delete_department_by_index(self,index):
        for i in range(len(self.__hospital)):
            if i==index:
                del self.__hospital[i]
        return self.__hospital

    '''
    description: the function sorts a department  by the number of patients in it
    input: nothing
    output: the new hospital with the patients of the departments sorted 
    '''
    def sort_by_number_patients(self):
        self.__hospital=sorted(self.__hospital, key=lambda department: department.get_number_patient())

    '''
    description: the function sorts a department  by the number of patients which has the age above a given number
    input: number: the number we compare the age of the patient with
           month: the month we want to see if he is older or not
           day: we want to verify is he is older or not from a given date constructed by the month and day which belong to the year 2024
    output: the new hospital with the patients of the departments sorted 
    '''
    def sort_departments_by_number_patients_above_given_value(self,number,month,day):
        self.__hospital=sorted(self.__hospital, key=lambda department: str(department.number_patients_with_age_above(number,month,day)))

    '''
    description: the function sorts a department  by the name of patients in it alphabetically
    input: nothing
    output: the new hospital with the patients of the departments sorted 
    '''
    def sort_alphabetically_patient(self):
        self.__hospital=sorted(self.__hospital, key=lambda department: (department.get_number_patient(),department.sort_patients_alphabetically()))

    '''
    description: the function finds departments  with patients' age undr a given value
    input: age:the number we compare the age of the patient with
           month:the month we want to see if he is older or not
           day:we want to verify is he is older or not from a given date constructed by the month and day which belong to the year 2024
    output: a new list with the name of the departments that varifies the conditions
    '''
    def identify_departments_patients_under_age(self,age,month,day):
        departments=[] #a new list where I put the names of the departments that has patients with the age uder a given age

        for department in self.__hospital:
            ppatients_age_above=department.number_patients_with_age_above(age,month,day)
            patients_age_under=department.get_number_patient()-ppatients_age_above
            if patients_age_under>0:
                departments.append(department.get_name())
            else:
                return 'there are not departments with patients under that age'
        return departments

    '''
        description: the function finds departments  with a string contained in the name of the patient
        input: department: the department we search the string in the names of the patient      
                string: the string we search 
        output: a new list with the name of the departments that varifies the conditions
        '''
    def get_patients_in_department_first_last_name(self,department,string):
        new_patients=[]
        for d in self.__hospital:
            if d.get_name()==department:
                for patient in d.get_list_patients():
                    name_patient=patient.get_f_name() + " " + patient.get_l_name()
                    #print(name_patient)
                    if string.lower() in name_patient.lower():
                        new_patients.append(patient.get_f_name()+" "+patient.get_l_name())
        print(new_patients)

    '''
    description: the function finds departments  with patients' first names
    input: first_name: the given string we search is it is in the patients name from each department
    output: a new list with the name of the departments that varifies the conditions
    '''
    def get_patients_by_first_name(self,first_name):
        new_list=[]
        for department in self.__hospital:
            ok=0
            for patient in department.get_list_patients():
                if first_name==patient.get_f_name() and ok==0:
                    new_list.append(department.get_name())
                    ok=1
        if new_list==[]:
            print ("that first name is not a name from our patients")
        else:
            print(new_list)

    '''
    description: the function forms groups ofk elem if the patients has the same name
    input: the department and how many we want to be in groups
    output: thr groups
    '''
    def form_sol_same_department_same_disease(self,department,k):
        hospital=department.sort_patients_alphabetically()
        hospital.insert(0,self.__hospital[0])
        domain=[i for i in range(0,len[hospital])]
        def initSolution():
            return domain[0]

        def getNext(i):
            return i+1

        def getLast():
            return domain[-1]

        def isSolution(sol,k):
            return len(sol)==k


        def isConsistent(sol, hospital):
            for i in range(0,len(sol)-1):
                if hospital[sol[i]].get_disease()==hospital[sol[-1]].get_disease():
                    return False
            return True

        def groupPersons(groupSize, hospital):
            k = 0
            sol = []
            unique_solution=[]
            sol.append(initSolution())
            while k >= 0:
                isSelected = False
                while (not isSelected) and (sol[k] < getLast()):
                    sol[k] = getNext(sol[k])
                    isSelected = isConsistent(sol, hospital)
                    if isSelected:
                        if isSolution(sol,groupSize):
                            current_solution=sorted(sol)
                            if current_solution not in unique_solution:
                                unique_solution.append(current_solution)
                                yield [hospital[i] for i in sol]
                            else:
                                k += 1
                                sol.append(0)
                        else:
                            k -= 1
                            sol.pop()
        return groupPersons(k,hospital)

    '''
    Description: The function counts how many patients have a specific disease
    input: none
    output: the final count 
    '''
    def get_patients_with_same_disease_count(self):
        max_count = 0
        max_disease = None
        for department in self.__hospital:
            for patient in department.get_list_patients():
                current_count = department.get_patients_with_same_disease_count(patient.disease)
                if current_count > max_count:
                    max_count = current_count
                    max_disease = patient.disease
        if max_disease is not None:
            print(f"The disease with the maximum number of patients is '{max_disease}' with {max_count} patients.")
        else:
            print("No patients in the hospital.")

    '''
    description: the function forms groups of k elem if there is a maximum of patients with same disease
    input: many we want to be in groups 
    output: thr groups
    '''
    def groups_department_repo_disease(self, k, p):
        if k <= 0 or k > len(self.__hospital):
            return ("k is not available")
        else:
            hospital = self.__hospital.copy()
            hospital.insert(0, self.__hospital[0])
            domain = [i for i in range(0, len(hospital))]

            def initSolution():
                return domain[0]

            def getNext(i):
                return i + 1

            def getLast():
                return domain[-1]

            def isSolution(sol, k):
                return len(sol) == k

            def isConsistent(sol, hospital):
                if k == 1 and hospital[sol[0]].get_patients_with_same_disease_count(p) == False:
                    return False
                for i in range(0, len(sol) - 1):
                    if ((hospital[sol[i]].get_patients_with_same_disease_count(p) == hospital[sol[-1]].get_patients_with_same_disease_count(p) == False) or (hospital[sol[i]].get_patients_with_same_disease_count(p) == False) or 
                            (hospital[sol[-1]].get_patients_with_same_disease_count(p) == False) or (hospital[sol[i]].getname() == hospital[sol[-1]].getname())):
                        return False
                return True

            def groupPersons(groupSize, hospital):
                k = 0
                sol = []
                unique_solution = []
                sol.append(initSolution())
                while k >= 0:
                    isSelected = False
                    while (not isSelected) and (sol[k] < getLast()):
                        sol[k] = getNext(sol[k])
                        isSelected = isConsistent(sol, hospital)
                    if isSelected:
                        if isSolution(sol, groupSize):
                            current_solution = sorted(sol)
                            if current_solution not in unique_solution:
                                unique_solution.append(current_solution)
                                yield [hospital[i] for i in sol]
                        else:
                            k += 1
                            sol.append(initSolution())
                    else:
                        k -= 1
                        sol.pop()

            s = ""
            for group in groupPersons(k, hospital):
                s += str(([str(department) for department in group])) + "\n"
            return s


    def __str__(self):
        department_list="\n".join(str(department) for department in self.__hospital)
        return f"Hospitals:\n{department_list}"


