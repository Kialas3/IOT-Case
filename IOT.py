import streamlit as st
from google.cloud import firestore
import firebase_admin

# Authenticate to Firestore with the JSON account key.
fb_credentials = st.secrets["firebase"]['my_project_settings']
print(type(fb_credentials))
fb_credentials_dict = fb_credentials.to_dict()
print(type(fb_credentials_dict))

cred = firebase_admin.credentials.Certificate(fb_credentials_dict)
firebase_admin.initialize_app(cred)
db = firebase_admin.firestore.client()

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