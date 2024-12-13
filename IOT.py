import firebase_admin.firestore
import streamlit as st
from google.cloud import firestore
import json
from google.oauth2 import service_account


import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
import json
key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="iot-final-project-b1550")


# db = firestore.Client.from_service_account_json(fb_credentials_dict)

if st.button("Refresh Now"):
    st.rerun()

# # delete button
# if st.button("Delete"):
#     # Create a reference to the Google post.
#     doc_ref = db.collection("IOT").document("PackageName")
#     doc_ref.delete()
    
# # add button
# if st.button("Add"):
#     # Create a reference to the Google post.
#     doc_ref = db.collection("IOT").document("PackageName")
#     doc_ref.set({
#         "Package No.1": 1,
#     })


# Create a reference to the Google post.
doc_ref = db.collection("IOT").document("PackageName")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())