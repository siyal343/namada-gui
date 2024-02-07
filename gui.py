import streamlit as st


st.set_page_config(layout="wide")


# Header
st.markdown("""
    <style>
        h1 {
            margin-bottom: 5px;
        }
        hr {
            margin-top: 5px;
        }
    </style>

    <h1 style='text-align: center;'>Namada Shielded Expedition</h1>
    <hr style='border: none; height: 3px; background-color: grey'>
""", unsafe_allow_html=True)


# Create three columns
col1, col2, col3 = st.columns(3)

# Column 1 - Chain ID
with col1:
    chain_id = st.text_input("Chain ID", value="", help="Enter the chain ID")

# Column 2 - RPC
with col2:
    default_rpc = "tcp://namada-rpc.zenode.app:80"
    rpc = st.text_input("RPC", value=default_rpc, help="Enter the RPC")

# Column 3 - Wallet Address
with col3:
   wallet_addr = st.text_input("Connected Wallet", value="", help="Enter the wallet address", key="wallet_addr", disabled=True)

with st.expander("# **Wallet Info**"):
    st.markdown("### Add Wallet")