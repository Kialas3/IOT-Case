import firebase_admin.firestore
import streamlit as st
from google.cloud import firestore
import json

# Authenticate to Firestore with the JSON account key.
fb_credentials = st.secrets["firebase"]['my_project_settings']
print(fb_credentials)
fb_credentials_dict = dict(fb_credentials)
print(type(fb_credentials_dict))

if not firebase_admin._apps:
    # key = json.loads(fb_credentials)
    cred = firebase_admin.credentials.Certificate(fb_credentials_dict)
    firebase_admin.initialize_app(cred)

@st.cache_resource
def get_db():
    key = json.loads(fb_credentials)
    cred = firebase_admin.credentials.Certificate(key)
    try:
        firebase_admin.get_app()
    except ValueError:
        firebase_admin.initialize_app(cred)
        
    db = firebase_admin.firestore.client()
    return db


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

db = get_db()
# Create a reference to the Google post.
doc_ref = db.collection("IOT").document("PackageName")

# Then get the data at that reference.
doc = doc_ref.get()

# Let's see what we got!
st.write("The id is: ", doc.id)
st.write("The contents are: ", doc.to_dict())