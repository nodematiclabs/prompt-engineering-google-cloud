import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
import os

# Initialize Firebase Admin
firebase_admin.initialize_app()

# Firestore database
db = firestore.client()

# Function to add a JSON file to Firestore
def add_json_to_firestore(file_path, collection_name):
    with open(file_path, 'r') as file:
        data = json.load(file)
        doc_id = os.path.splitext(os.path.basename(file_path))[0]  # Use file name as document ID
        db.collection(collection_name).document(doc_id).set(data)
        print(f"Document {doc_id} added to Firestore")

# Walk through the current directory
collection_name = 'prompts'
for root, dirs, files in os.walk('./data'):  # '.' represents the current directory
    for file in files:
        if file.endswith('.json'):
            file_path = os.path.join(root, file)
            add_json_to_firestore(file_path, collection_name)
