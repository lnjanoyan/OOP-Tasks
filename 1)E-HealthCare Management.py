import abc
import datetime


class Doctor:
    def __init__(self, name: str, specialization: str, ex_years: float, contact_info: str):
        self.name = name
        self.specialization = specialization
        self.ex_years = ex_years
        self.contact_info = contact_info


class Patient:
    def __init__(self, name: str, birth_date: str, gender: str, contact_info: str, conditions: str):
        self.name = name
        self.birth_date = birth_date
        self.gender = gender
        self.contact_info = contact_info
        self.condition = conditions
        self.history = dict(diagnoses=[], treatments=[], medications=[])


class System(abc.ABC):
    @abc.abstractmethod
    def doctor_register(self, doctor: Doctor):
        pass

    def patient_register(self, patient: Patient):
        pass

    @abc.abstractmethod
    def record_history(self, patient: Patient):
        pass

    @abc.abstractmethod
    def display_history(self, patient: Patient):
        pass

    @abc.abstractmethod
    def generate_report(self, patient: Patient):
        pass

    @abc.abstractmethod
    def save_report(self, patient: Patient):
        pass


class MySystem(System):
    def __init__(self):
        self.doctors = []
        self.patients = []
        self.report = ''

    def doctor_register(self, doctor: Doctor):
        self.doctors.append(doctor.name)

    def patient_register(self, patient: Patient):
        self.patients.append(patient.name)

    def record_history(self, patient: Patient):
        diagnoses = input('Type diagnose for recording(If there is no one type "-" or press Enter ): ')
        if diagnoses.isalnum():
            patient.history['diagnoses'].append(diagnoses)

        treatments = input('Type treatment for recording(If there is no one type "-" or press Enter ): ')
        if treatments.isalnum():
            patient.history['treatments'].append(treatments)

        medications = input('Type medication for recording(If there is no one type "-" or press Enter ): ')
        if medications.isalnum():
            patient.history['medications'].append(medications)

    def display_history(self, patient: Patient):
        print(f"\n{patient.name}'s history:")
        for i in patient.history.keys():
            print(i, patient.history[i])

    def generate_report(self, patient: Patient):
        self.report = f"\n{patient.name}'s medical history report\nPatient's info\nName:{patient.name}\n" \
                      f"Gender:{patient.gender}\nContact info: {patient.contact_info}\nBirth date: {patient.birth_date}" \
                      f"\nMedical history:" + str(patient.history.items())[12:-2]
        print(self.report)

    def save_report(self, patient: Patient):
        filename = f"{patient.name}'s report {datetime.datetime.now().strftime('%d.%m.%Y,%H;%M;%S')}.txt"
        f = open(filename, 'w')
        f.write(self.report)
        f.close()


patient1 = Patient('Anna', '18.06.2002', 'female', '+2565131', 'cond1')
patient2 = Patient('Bob', '22.04.2001', 'male', '+64513', 'cond2')
doctor1 = Doctor('Lily', 'spec1', 10, '+5315')
sys = MySystem()
sys.patient_register(patient1)
sys.patient_register(patient2)
sys.doctor_register(doctor1)
print(f"Patients: {sys.patients}, Doctors: {sys.doctors}")
sys.record_history(patient1)
sys.display_history(patient1)
sys.generate_report(patient1)
sys.save_report(patient1)
