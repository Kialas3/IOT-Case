import streamlit as st
from google.cloud import firestore

# Authenticate to Firestore with the JSON account key.
db = firestore.Client.from_service_account_json("./iot-final-project-key.json")

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