from med_tracker.main.models import Medication
from datetime import datetime

def record_dose(medication, dosage):
    dose = Medication(medication=medication, dosage=dosage, time=datetime.utcnow())
    # Add to Firebase database here
