import streamlit as st
import pandas as pd
import numpy as np
    
# Main function
def main():

    st.set_page_config(layout="wide")
    
    LOGO_SIDEBAR_URL = "https://static.wixstatic.com/media/dd11e9_145d7c62f0a647979cbe9e9adef92f5b~mv2.png/v1/fill/w_344,h_60,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/White%20logo%20with%20tagline%20on%20Transparent%20b.png"

    if LOGO_SIDEBAR_URL: st.sidebar.image(
            LOGO_SIDEBAR_URL,             
            caption= 'Sharing expertise. Building relationships'
    )
        
    
    merged_df = pd.read_csv("water_potability.csv")
    merged_df['Predicted Potability'] = merged_df['Predicted Potability'].replace({0: 'No', 1: 'Yes'})

    st.subheader("This is the predicted file for potability")
    st.write(merged_df)   
        
if __name__ == "__main__":
    main()