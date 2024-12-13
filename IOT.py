import streamlit as st
from google.cloud import firestore
import json
from google.oauth2 import service_account

import pandas as pd

import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds)


# db = firestore.Client.from_service_account_json('./key.json')

if st.button("Refresh Now"):
    st.rerun()

# # delete button
# if st.button("Delete"):
#     # Create a reference to the Google post.
#     doc_ref = db.collection("IOT").document("PackageName")
#     doc_ref.delete()

# dict_data = {'Package NO.': 'Number',
#              "No.1": 5}

# add button
# if st.button("Add"):
#     # Create a reference to the Google post.
#     doc_ref = db.collection("IOT").document("PackageName")
#     doc_ref.set(dict_data)


# Create a reference to the Google post.
doc_ref = db.collection("IOT").document("PackageName")

# Then get the data at that reference.
doc = doc_ref.get()
doc_dict = doc.to_dict()

# @st.cache_data
def get_df(doc_dict):
    df = pd.DataFrame(list(doc_dict.items()), columns=["Package NO.", "Number"])
    # df.columns = df.iloc[0]
    # df = df[1:]
    return df

df = get_df(doc_dict)

mytabel = st.table(df)