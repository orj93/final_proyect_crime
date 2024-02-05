import streamlit as st
from pickle import load
import numpy as np
import pandas as pd

descent_dict={'Other Asian': 4, 'Black':0,'Chinese':6,'Cambodian':12,'Filipino':7,'Guamanian':16,
                  'Hispanic/Latin/Mexican':1, 'American Indian/Alaskan Native':9, 'Japanese':11,
                  'Korean':8, 'Laotian':18, 'Other':5, 'Pacific Islander':15, 'Samoan':17, 'Hawaiian':14,
                  'Vietnamese':10, 'White':2, 'Unknown':3, 'Asian Indian':13}
#  A - Other Asian B - Black C - Chinese D - Cambodian F - Filipino G - Guamanian H - Hispanic/Latin/Mexican
# I - American Indian/Alaskan Native J - Japanese K - Korean L - Laotian O - Other P - Pacific Islander
# S - Samoan U - Hawaiian V - Vietnamese W - White X - Unknown Z - Asian Indian

area_dict={"Southwest":0, "Central":1,"N Hollywood":2,"Mission":3,"Harbor":4,"Rampart":5,"Hollenbeck":6,
                "77th Street":7,"Wilshire":8,"Hollywood":9,"Northeast":10,"West LA":11,"Van Nuys":12,
                "West Valley":13,"Newton":14,"Olympic":15,"Southeast":16,"Topanga":17,"Foothill":18,
                "Pacific":19, "Devonshire":20}

sex_dict = {'Woman':0,'Man':1,'Other':2}

class_dict={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J'}

st.markdown('<style>h1 { color: navy; text-align: center;}</style>', unsafe_allow_html=True)

st.title("LA crime")

image = "../data/images/image.png"

st.image(image, output_format="PNG")

crime = st.selectbox(
    'Pick a crime you want to analyze',
    ('Select a type of crime','Burglary','Child abuse','Homicide','Rape' , 'Robbery'))



if crime == 'Burglary':
    lat = st.slider('Select latitude', min_value=33.7064, max_value=34.3276, step=0.0001)
    lon = st.slider('Select longitude', min_value=-118.6673, max_value=-118.156, step=0.0001)
    if st.button("Predecir"):
        with (open(r"../models/best_model_burglary.pk", "rb")) as openfile:
         model = load(openfile)
        row = [lon,lat]
        array=np.array(row)
        
        row_reshaped = array.reshape(1, -1)    
        y_pred = model.predict(row_reshaped)[0]
        pred_class = class_dict[y_pred]
        #st.text("The burglary profile: " + str(y_pred[0]))
        data = {'latitude': [lat], 'longitude': [lon]}

        df = pd.DataFrame(data)
        st.map(df, size=20, color='#0044ff')

#    st.text(str(y_pred))

    
        st.write("Possible burglary gang:", pred_class)

elif crime == 'Robbery':
    lat = st.slider('Select latitude', min_value=34.0, max_value=35.0, step=0.01)
    lon = st.slider('Select longitude', min_value=-119.0, max_value=-118.0, step=0.01)
    if st.button("Predecir"):
        with (open(r"../models/model_robbery.pk", "rb")) as openfile:
         model = load(openfile)
        row = [lon,lat]
        array=np.array(row)
        
        row_reshaped = array.reshape(1, -1)    
        y_pred = model.predict(row_reshaped)[0]
        pred_class = class_dict[y_pred]
        #st.text("The burglary profile: " + str(y_pred[0]))
        data = {'latitude': [lat], 'longitude': [lon]}

        df = pd.DataFrame(data)
        st.map(df, size=20, color='#0044ff')

#    st.text(str(y_pred))

    
        st.write("Possible robbery gang:", pred_class)

elif crime == 'Homicide':
    age = st.slider('Select age', min_value=1, max_value=100, step=1)
    sex = st.selectbox("Select Sex: ", [key for key in sorted(sex_dict)])
    descent = st.selectbox("Select Descent: ", [key for key in sorted(descent_dict)])
    area = st.selectbox("Select Area: ", [key for key in sorted(area_dict)])
    
    fact_sex=sex_dict[sex]   
    fact_descent=descent_dict[descent]   
    fact_area=area_dict[area]



    if st.button("Predecir"):
        with (open(r"../models/best_model_killers.pk", "rb")) as openfile:
         model = load(openfile)
        row = [
            age,
            fact_sex,
            fact_descent,
            fact_area
        ]
        array=np.array(row)
        
        row_reshaped = array.reshape(1, -1)    
        y_pred = model.predict(row_reshaped)[0]
        pred_class = class_dict[y_pred]
#    st.text(str(y_pred))

    
        st.write("Possible homicide profile:", pred_class)

elif crime == 'Rape':
    age = st.slider('Select age', min_value=1, max_value=100, step=1)   
    descent = st.selectbox("Select Descent: ", [key for key in sorted(descent_dict)])
    area = st.selectbox("Select Area: ", [key for key in sorted(area_dict)])
    
    fact_descent=descent_dict[descent]   
    fact_area=area_dict[area]



    if st.button("Predecir"):
        with (open(r"../models/best_model_rapists.pk", "rb")) as openfile:
         model = load(openfile)
        row = [
            age,
            fact_descent,
            fact_area
        ]
        array=np.array(row)
        
        row_reshaped = array.reshape(1, -1)    
        y_pred = model.predict(row_reshaped)[0]
        pred_class = class_dict[y_pred]
#    st.text(str(y_pred))

    
        st.write("Possible rapist profile:", pred_class)

elif crime == 'Child abuse':
    age = st.slider('Select age', min_value=0, max_value=17, step=1)
    sex = st.selectbox("Select Sex: ", [key for key in sorted(sex_dict)])
    descent = st.selectbox("Select Descent: ", [key for key in sorted(descent_dict)])
    
    fact_sex=sex_dict[sex]   
    fact_descent=descent_dict[descent]   
    
    if st.button("Predecir"):
        with (open(r"../models/best_model_child.pk", "rb")) as openfile:
         model = load(openfile)
        row = [
            age,
            fact_sex,
            fact_descent,        
        ]
        array=np.array(row)
        
        row_reshaped = array.reshape(1, -1)    
        y_pred = model.predict(row_reshaped)[0]
        pred_class = class_dict[y_pred]
#    st.text(str(y_pred))

    
        st.write("Possible child molester:", pred_class)

else:
    st.text("No crime selected")

