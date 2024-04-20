
symptom_dataset = ['itching', 'skin rash', 'nodal skin eruptions',
       'continuous sneezing', 'shivering', 'chills', 'joint pain',
       'stomach pain', 'acidity', 'ulcers on tongue', 'muscle wasting',
       'vomiting', 'burning micturition', 'spotting urination', 'fatigue',
       'weight gain', 'anxiety', 'cold hands and feets', 'mood swings',
       'weight loss', 'restlessness', 'lethargy', 'patches in throat',
       'irregular sugar level', 'cough', 'high fever', 'sunken eyes',
       'breathlessness', 'sweating', 'dehydration', 'indigestion',
       'headache', 'yellowish skin', 'dark urine', 'nausea',
       'loss of appetite', 'pain behind the eyes', 'back pain',
       'constipation', 'abdominal pain', 'diarrhoea', 'mild fever',
       'yellow urine', 'yellowing of eyes', 'acute liver failure',
       'fluid overload', 'swelling of stomach', 'swelled lymph nodes',
       'malaise', 'blurred and distorted vision', 'phlegm',
       'throat irritation', 'redness of eyes', 'sinus pressure',
       'runny nose', 'congestion', 'chest pain', 'weakness in limbs',
       'fast heart rate', 'pain during bowel movements',
       'pain in anal region', 'bloody stool', 'irritation in anus',
       'neck pain', 'dizziness', 'cramps', 'bruising', 'obesity',
       'swollen legs', 'swollen blood vessels', 'puffy face and eyes',
       'enlarged thyroid', 'brittle nails', 'swollen extremeties',
       'excessive hunger', 'extra marital contacts',
       'drying and tingling lips', 'slurred speech', 'knee pain',
       'hip joint pain', 'muscle weakness', 'stiff neck',
       'swelling joints', 'movement stiffness', 'spinning movements',
       'loss of balance', 'unsteadiness', 'weakness of one body side',
       'loss of smell', 'bladder discomfort', 'foul smell ofurine',
       'continuous feel of urine', 'passage of gases', 'internal itching',
       'toxic look (typhos)', 'depression', 'irritability', 'muscle pain',
       'altered sensorium', 'red spots over body', 'belly pain',
       'abnormal menstruation', 'dischromic patches',
       'watering from eyes', 'increased appetite', 'polyuria',
       'family history', 'mucoid sputum', 'rusty sputum',
       'lack of concentration', 'visual disturbances',
       'receiving blood transfusion', 'receiving unsterile injections',
       'coma', 'stomach bleeding', 'distention of abdomen',
       'history of alcohol consumption', 'blood in sputum',
       'prominent veins on calf', 'palpitations', 'painful walking',
       'pus filled pimples', 'blackheads', 'scurring', 'skin peeling',
       'silver like dusting', 'small dents in nails',
       'inflammatory nails', 'blister', 'red sore around nose',
       'yellow crust ooze', 'prognosis']

symptom_relation = {
    'itching': ['skin rash', 'nodal skin eruptions'],
    'skin rash': ['itching', 'nodal skin eruptions'],
    'nodal skin eruptions': ['itching', 'skin rash'],
    'continuous sneezing': ['cough', 'throat irritation', 'runny nose'],
    'shivering': ['chills', 'high fever', 'sweating', 'runny nose'],
    'chills': ['shivering', 'high fever', 'sweating', 'runny nose'],
    'joint pain': ['muscle pain', 'stiff neck', 'swelling joints'],
    'stomach pain': ['acidity', 'ulcers on tongue', 'abdominal pain'],
    'acidity': ['stomach pain', 'ulcers on tongue', 'abdominal pain'],
    'ulcers on tongue': ['stomach pain', 'acidity', 'abdominal pain'],
    'muscle wasting': ['muscle weakness', 'weight loss', 'weakness in limbs'],
    'vomiting': ['burning micturition', 'nausea', 'abdominal pain'],
    'burning micturition': ['vomiting', 'abdominal pain', 'urinary tract infection'],
    'spotting urination': ['burning micturition', 'urinary tract infection', 'abdominal pain'],
    'fatigue': ['lethargy', 'restlessness', 'weakness in limbs'],
    'weight gain': ['increased appetite', 'obesity', 'swelling of stomach'],
    'anxiety': ['mood swings', 'depression', 'irritability'],
    'cold hands and feets': ['cold hands and feet', 'sweating', 'fatigue'],
    'mood swings': ['anxiety', 'depression', 'irritability'],
    'weight loss': ['fatigue', 'mood swings', 'anxiety'],
    'restlessness': ['fatigue', 'mood swings', 'anxiety'],
    'lethargy': ['fatigue', 'weakness in limbs', 'restlessness'],
    'patches in throat': ['sore throat', 'throat irritation', 'swollen lymph nodes'],
    'irregular sugar level': ['diabetes', 'excessive hunger', 'polyuria'],
    'cough': ['continuous sneezing', 'throat irritation', 'phlegm'],
    'fever': ['high fever', 'mild fever', 'shivering', 'chills', 'sweating', 'runny nose'],
    'sunken eyes': ['dehydration', 'fatigue', 'dark urine'],
    'breathlessness': ['sweating', 'chest pain', 'fast heart rate'],
    'sweating': ['shivering', 'chills', 'breathlessness'],
    'dehydration': ['sunken eyes', 'dark urine', 'sweating'],
    'indigestion': ['stomach pain', 'abdominal pain', 'nausea'],
    'headache': ['migraine', 'dizziness', 'neck pain'],
    'yellowish skin': ['jaundice', 'yellowing of eyes', 'dark urine'],
    'dark urine': ['jaundice', 'yellowing of eyes', 'yellowish skin'],
    'nausea': ['vomiting', 'indigestion', 'abdominal pain'],
    'loss of appetite': ['abdominal pain', 'nausea', 'fatigue'],
    'pain behind the eyes': ['headache', 'eye pain', 'sensitivity to light'],
    'back pain': ['abdominal pain', 'muscle pain', 'neck pain'],
    'constipation': ['abdominal pain', 'diarrhoea', 'abnormal bowel movements'],
    'abdominal pain': ['stomach pain', 'indigestion', 'constipation'],
    'diarrhoea': ['abdominal pain', 'constipation', 'stomach pain'],
    'yellow urine': ['urinary tract infection', 'kidney stones', 'dehydration'],
    'yellowing of eyes': ['jaundice', 'yellowish skin', 'dark urine'],
    'acute liver failure': ['jaundice', 'abdominal pain', 'dark urine'],
    'fluid overload': ['swelling of stomach', 'swollen extremeties', 'puffy face and eyes'],
    'swelling of stomach': ['abdominal pain', 'fluid overload', 'swollen extremeties'],
    'swelled lymph nodes': ['sore throat', 'patches in throat', 'throat irritation'],
    'malaise': ['lethargy', 'fatigue', 'restlessness'],
    'blurred and distorted vision': ['visual disturbances', 'redness of eyes', 'eye pain'],
    'phlegm': ['cough', 'throat irritation', 'chest congestion'],
    'throat irritation': ['sore throat', 'phlegm', 'cough'],
    'redness of eyes': ['eye pain', 'itching', 'blurred and distorted vision'],
    'sinus pressure': ['runny nose', 'congestion', 'headache'],
    'runny nose': ['sinus pressure', 'congestion', 'throat irritation'],
    'congestion': ['sinus pressure', 'runny nose', 'throat irritation'],
    'chest pain': ['breathlessness', 'fast heart rate', 'sweating'],
    'weakness in limbs': ['muscle weakness', 'muscle wasting', 'fatigue'],
    'fast heart rate': ['breathlessness', 'chest pain', 'sweating'],
    'pain during bowel movements': ['abdominal pain', 'constipation', 'diarrhoea'],
    'pain in anal region': ['abdominal pain', 'constipation', 'diarrhoea'],
    'bloody stool': ['abdominal pain', 'diarrhoea', 'constipation'],
    'irritation in anus': ['abdominal pain', 'constipation', 'diarrhoea'],
    'continuous feel of urine': ['bladder discomfort', 'foul smell ofur'],
    'passage of gases': ['pain during bowel movements', 'abdominal pain'],
    'internal itching': ['itching', 'skin rash'],
    'toxic look (typhos)': ['sunken eyes', 'dehydration'],
    'depression': ['irritability', 'mood swings'],
    'irritability': ['depression', 'mood swings'],
    'muscle pain': ['joint pain', 'stiff neck'],
    'altered sensorium': ['irritability', 'mood swings'],
    'red spots over body': ['rashes', 'itching'],
    'belly pain': ['stomach pain', 'abdominal pain'],
    'abnormal menstruation': ['irregular sugar level', 'acidity'],
    'dischromic patches': ['patches in throat', 'skin rash'],
    'watering from eyes': ['redness of eyes', 'sinus pressure'],
    'increased appetite': ['weight gain', 'obesity'],
    'polyuria': ['irregular sugar level', 'acidity'],
    'mucoid sputum': ['phlegm', 'throat irritation'],
    'rusty sputum': ['phlegm', 'throat irritation'],
    'lack of concentration': ['irritability', 'depression'],
    'visual disturbances': ['redness of eyes', 'sinus pressure'],
    'receiving blood transfusion': ['extra marital contacts', 'receiving unsterile injections'],
    'receiving unsterile injections': ['extra marital contacts', 'receiving blood transfusion'],
    'coma': ['altered sensorium', 'irritability'],
    'stomach bleeding': ['abdominal pain', 'pain during bowel movements'],
    'distention of abdomen': ['abdominal pain', 'pain during bowel movements'],
    'history of alcohol consumption': ['obesity', 'altered sensorium'],
    'blood in sputum': ['rusty sputum', 'phlegm'],
    'prominent veins on calf': ['swollen legs', 'swelling joints'],
    'palpitations': ['chest pain', 'fast heart rate'],
    'pus filled pimples': ['skin rash', 'itching'],
    'blackheads': ['skin rash', 'itching'],
    'scurring': ['skin rash', 'itching'],
    'skin peeling': ['skin rash', 'itching'],
    'silver like dusting': ['skin rash', 'itching'],
    'small dents in nails': ['brittle nails', 'enlarged thyroid'],
    'inflammatory nails': ['brittle nails', 'enlarged thyroid'],
    'blister': ['skin rash', 'itching'],
    'red sore around nose': ['sinus pressure', 'runny nose'],
    'yellow crust ooze': ['drying and tingling lips', 'slurred speech'],
    'prognosis': [],
     'itching': ['skin rash', 'nodal skin eruptions', 'internal itching'],
    'fatigue': ['lethargy', 'restlessness', 'malaise'],
    'restlessness': ['fatigue', 'lethargy', 'malaise'],
    'lethargy': ['fatigue', 'restlessness', 'malaise'],
    'patches in throat': ['throat irritation', 'dischromic patches', 'redness of eyes'],
    'abnormal menstruation': ['irregular sugar level', 'acidity', 'increased appetite'],
    'muscle pain': ['joint pain', 'stiff neck', 'cramps'],
    'palpitations': ['chest pain', 'fast heart rate', 'dizziness'],
    'pus filled pimples': ['skin rash', 'itching', 'blister'],
    'blackheads': ['skin rash', 'itching', 'blister'],
    'scurring': ['skin rash', 'itching', 'blister'],
    'neck pain': ['headache', 'stiff neck', 'dizziness'],
    'dizziness': ['headache', 'neck pain', 'palpitations'],
    'cramps': ['muscle pain', 'joint pain', 'stiff neck'],
    'bruising': ['muscle pain', 'joint pain', 'cramps'],
    'obesity': ['weight gain', 'enlarged thyroid', 'family history'],
    'swollen legs': ['swelling of stomach', 'fluid overload', 'swelling joints'],
    'swollen blood vessels': ['swelling of stomach', 'swelled lymph nodes', 'prominent veins on calf'],
    'puffy face and eyes': ['swelling of stomach', 'fluid overload', 'swollen extremeties'],
    'enlarged thyroid': ['obesity', 'brittle nails', 'inflammatory nails'],
    'brittle nails': ['enlarged thyroid', 'small dents in nails', 'inflammatory nails'],
    'swollen extremeties': ['swelled lymph nodes', 'muscle weakness', 'swollen legs'],
    'excessive hunger': ['increased appetite', 'polyuria'],
    'extra marital contacts': ['receiving unsterile injections', 'receiving blood transfusion', 'toxic look (typhos)'],
    'drying and tingling lips': ['toxic look (typhos)', 'yellow crust ooze', 'slurred speech'],
    'slurred speech': ['drying and tingling lips', 'yellow crust ooze'],
    'knee pain': ['hip joint pain', 'swelling joints', 'pain behind the eyes'],
    'hip joint pain': ['knee pain', 'swelling joints', 'movement stiffness'],
    'muscle weakness': ['joint pain', 'stiff neck', 'swelled lymph nodes'],
    'stiff neck': ['joint pain', 'muscle weakness', 'movement stiffness'],
    'swelling joints': ['knee pain', 'hip joint pain', 'movement stiffness'],
    'movement stiffness': ['joint pain', 'stiff neck', 'muscle pain'],
    'spinning movements': ['joint pain', 'stiff neck', 'movement stiffness'],
    'loss of balance': ['dizziness', 'unsteadiness', 'weakness of one body side'],
    'unsteadiness': ['joint pain', 'stiff neck', 'loss of balance'],
    'weakness of one body side': ['joint pain', 'stiff neck', 'muscle weakness'],
    'loss of smell': ['throat irritation', 'congestion', 'visual disturbances'],
    'bladder discomfort': ['continuous feel of urine', 'foul smell of urine', 'passage of gases'],
    'foul smell ofurine': ['bladder discomfort', 'continuous feel of urine']    
}