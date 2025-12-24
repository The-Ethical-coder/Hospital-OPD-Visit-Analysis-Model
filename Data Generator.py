import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_hospital_data(n_rows=1000):
    """
    Generates a synthetic dataset for Hospital OPD visits.
    """
    np.random.seed(42)
    
    # Configuration
    departments = ['Cardiology', 'Pediatrics', 'General Medicine', 'Orthopedics', 'Dermatology', 'Neurology']
    genders = ['Male', 'Female', 'Other']
    payment_methods = ['Insurance', 'Cash', 'Digital Wallet']
    
    start_date = datetime(2023, 1, 1)
    
    data = []
    for i in range(n_rows):
        # Generate random date/time within a 6-month period
        random_days = random.randint(0, 180)
        random_hours = random.randint(8, 20) # OPD hours 8 AM to 8 PM
        random_minutes = random.randint(0, 59)
        
        appointment_time = start_date + timedelta(days=random_days, hours=random_hours, minutes=random_minutes)
        
        # Patient metrics
        age = np.random.normal(40, 20)
        age = int(np.clip(age, 1, 95))
        
        # Logic: Older people might wait longer or visit specific depts
        dept = random.choice(departments)
        wait_time = random.randint(5, 120) if dept != 'General Medicine' else random.randint(5, 45)
        
        data.append({
            'Patient_ID': f'P-{1000+i}',
            'Timestamp': appointment_time,
            'Age': age,
            'Gender': random.choice(genders),
            'Department': dept,
            'Consultation_Fee': random.choice([500, 800, 1200, 1500, 2000]),
            'Wait_Time_Min': wait_time,
            'Payment_Method': random.choice(payment_methods)
        })

    df = pd.DataFrame(data)
    df.to_csv('hospital_opd_visits.csv', index=False)
    print("Success: 'hospital_opd_visits.csv' generated with 1000 records.")

if __name__ == "__main__":
    generate_hospital_data()