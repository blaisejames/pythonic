class Patient(object):
    patient_count = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.id = Patient.patient_count
        self.bed_num = None
        Patient.patient_count += 1

class Hospital(object):
    def __init__(self, name, cap):
        self.name = name
        self.cap = cap
        self.patients = []
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for i in range(0, self.cap):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds

    def admit(self, patient):
        if len(self.patients) <= self.cap:
            self.patients.append(patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bed_num = self.beds[i]["bed_id"]
                    self.beds[i]["Available"] = False
                    break
            print "Patient #{} ({}) admitted to bed #{} at {} with a capacity of {} beds. \nThe patient is allergic to {}.\n".format(patient.id, patient.name, patient.bed_num, self.name, self.cap, patient.allergies)
        else:
            "Hospital is at full capacity"
    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break
                self.patients.remove(patient)
                print "Patient #{} ({}) sucessfully discharged.\nBed #{} at {} now available.".format(patient.id, patient.name, patient.bed_num, self.name)
                return self
        return "Patient not found"

pat0 = Patient("Barbara Bogster", "ragweed, boxwood, snails")
pat1 = Patient("Jimbo Jumbo", "diets, moderation, reasonable portions")
pat2 = Patient("Marre Soupial", "the rich, the poor, the bougeoise")
pat3 = Patient("Henrietta Hypochondriac", "everything")
hos0 = Hospital("Our Lady of Murgatroid", 500)
hos1 = Hospital("University Hospital", 350)
hos2 = Hospital("St. Elsewhere", 225)
hos0.admit(pat0)
hos1.admit(pat1)
hos1.admit(pat2)
hos2.admit(pat3)
hos2.discharge(3)