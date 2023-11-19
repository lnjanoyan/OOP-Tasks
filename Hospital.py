# hamarya done
import abc


class Patient:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.medical_history = []
        self.appointments = []


class MedicalStuff(abc.ABC):
    def __init__(self, name: str, position: str):
        self.name = name
        self.position = position


class Doctor:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info

    def create_appointment(self, patient: Patient, appointment: str):
        patient.appointments.append(appointment)
        print(f'Current appointments of {patient.name}: ', patient.appointments)
        patient.medical_history.append(appointment)

    def delete_appointment(self, patient: Patient, appointment: str):
        if appointment in patient.appointments:
            patient.medical_history.remove(appointment)
        else:
            print("No such appointment in patient's appointment")


class MedicalOperation(abc.ABC):
    def __init__(self):
        self.med_stuff = []

    @abc.abstractmethod
    def implement(self, patient: Patient, doctor: Doctor, *stuff_member: MedicalStuff):
        pass


class Surgery(MedicalOperation):
    def __init__(self):
        super().__init__()

    def implement(self, doctor: Doctor, patient: Patient, *stuff_member: MedicalStuff):
        for i in stuff_member:
            self.med_stuff.append(i.name)
        print(f"'{doctor.name}' with the staff {self.med_stuff}' are "
              f"implementing surgery for the patient '{patient.name}'")
        patient.medical_history.append('surgery')


class OtherMedicalOperation(MedicalOperation):
    def __init__(self):
        super().__init__()

    def implement(self, doctor: Doctor, patient: Patient, *stuff_member: MedicalStuff):
        self.med_stuff.append(stuff_member)
        print(f"'{doctor.name}' with the staff '{self.med_stuff}' are "
              f"implementing OtherMedicalOperation for the patient '{patient.name}'")
        patient.medical_history.append('OtherMedicalOperation')


patient1 = Patient('Anna', 22)
patient2 = Patient('Lily', 42)
doctor = Doctor('Dr. James', 'dr.james@gmail.com')
nurse1 = MedicalStuff('Ella', 'nurse')
nurse2 = MedicalStuff('Ani', 'nurse')
doctor.create_appointment(patient1, 'appointment1')
doctor.create_appointment(patient1, 'appointment2')
surgery1 = Surgery()
surgery1.implement(doctor, patient1, nurse1, nurse2)
print(patient1.medical_history)
doctor.delete_appointment(patient1, 'appointment1')
print(patient1.medical_history)


class HospitalSystem:
    patients = []
    doctors = []
    staff = []

    def create_patient(self, patient: Patient):
        self.patients.append(patient)
        return patient

    def create_doctor(self, doctor: Doctor):
        self.doctors.append(doctor)
        return doctor

    def create_staff(self, med_staff: MedicalStuff):
        self.staff.append(med_staff)
        return med_staff

