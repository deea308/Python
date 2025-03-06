class Patient:
    def __init__(self,f_name,l_name,personal_code,disease):
        self.__f_name=f_name
        self.__l_name=l_name
        self.__personal_code=personal_code
        self.__disease=disease

    def get_f_name(self):
        return self.__f_name
    def set_f_name(self,f_name):
        self.__f_name=f_name

    def get_l_name(self):
        return self.__l_name
    def set_l_name(self,l_name):
        self.__l_name=l_name

    def get_personal_code(self):
        return self.__personal_code
    def set_personal_code(self,personal_code):
        self.__personal_code=personal_code

    def get_disease(self):
        return self.__disease
    def set_disease(self,disease):
        self.__disease=disease

    def __str__(self):
        return f" {self.__f_name} {self.__l_name}, code:{self.__personal_code}, disease: {self.__disease} "

