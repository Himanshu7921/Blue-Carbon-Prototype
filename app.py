import streamlit as st
from blockchain import add_block, view_chain, issue_tokens, tokens

st.title("Blue Carbon Blockchain MRV Prototype")

# Form to add project
with st.form("project_form"):
    project_name = st.text_input("Project Name")
    user = st.text_input("NGO/Community Name")
    trees = st.number_input("Number of Trees Planted", min_value=1)
    gps = st.text_input("GPS Coordinates (lat,long)")
    photo_url = st.text_input("Photo URL")
    verify = st.checkbox("Verify this project?")
    
    submitted = st.form_submit_button("Add Project")
    
    if submitted:
        project_data = {
            "project_name": project_name,
            "user": user,
            "trees": trees,
            "gps": gps,
            "photo_url": photo_url
        }
        # Add block with verification status
        block = add_block(project_data, verified=verify)
        
        # Issue tokens only if verified
        if verify:
            issue_tokens(user, trees)
            st.success(f"Project verified! {trees} tokens issued to {user}.")
        else:
            st.warning("Project not verified. No tokens issued.")
        
        st.info(f"Block added for project: {project_name}")

import pandas as pd

st.subheader("Blockchain Summary (Registered Projects)")

# Prepare data for table
table_data = []
for i, block in enumerate(view_chain(), start=1):
    data = block['data']
    table_data.append({
        "Block#": i,
        "Project": data['project_name'],
        "NGO/Community": data['user'],
        "Trees": data['trees'],
        "GPS": data['gps'],
        "Photo URL": data['photo_url'],
        "Verified": data['verified'],
        "Hash": block['hash'][:10] + "..."  # shorten hash
    })

# Convert to DataFrame
df = pd.DataFrame(table_data)

# Display as table
st.table(df)  # or st.dataframe(df) for scrollable table

# Display blockchain summary
st.subheader("Blockchain Summary")
for i, block in enumerate(view_chain()):
    st.write(f"Block {i+1}: {block}")
