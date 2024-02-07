import streamlit as st
import pexpect



logs = ""
chain_id = "shielded-expedition.88f17d1d14"
default_rpc = "tcp://namada-rpc.zenode.app:80"
join_network_cmd = f"namada client utils join-network --chain-id {chain_id}"

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


def run_command(command):
    process = pexpect.spawn(command)
    process.expect(pexpect.EOF)
    output = process.before.decode()
    return command, output

def update_status(logs):
    st.text_area("Logs", value=logs, height=300)




# Create three columns
col1, col2, col3 = st.columns(3)

# Column 1 - Chain ID
with col1:
    chain_id = st.text_input("Chain ID", value="shielded-expedition.88f17d1d14", help="Enter the chain ID")

# Column 2 - RPC
with col2:
    rpc = st.text_input("RPC", value=default_rpc, help="Enter the RPC")

# Column 3 - Wallet Address
with col3:
   wallet_addr = st.text_input("Connected Wallet", value="", help="Enter the wallet address", key="wallet_addr", disabled=True)

j, w = st.columns([1, 2])
with j:
    with st.expander("# **Join Network**"):
        st.markdown("### Join Testnet")

        if st.button("Join Network", use_container_width=True):
            command, output = run_command(join_network_cmd)
            logs = logs + f"Command:\n{command}\n\nOutput:\n{output}" 
        
        st.text_input("Chain ID", value="shielded-expedition.88f17d1d14", disabled=True)


with w:
    with st.expander("# **Add Wallet**"):
        st.markdown("### Connect Wallet")
        left, mid, right = st.columns([2,2,1])
        with left:
            st.text_input("Password", value="", key="password", type="password")
            
        with mid:
            st.text_input("Mnemonic Phrase", value="", key="mnemonic")
            
        with right:
            st.text_input("Name", value="", key="alias")
            
        st.text_input("Connected Wallet", value="")


    
    

update_status(logs)