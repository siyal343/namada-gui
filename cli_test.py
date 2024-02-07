import pexpect

# Provide the password
password = 'CALcium01@'


# Provide the passphrase
passphrase = 'CALcium01@'


# Provide the mnemonic code
mnemonic_code = 'theme grape help rebel file album clerk crouch connect label lens crouch\n'

command = 'namadaw derive --alias mushii'

# Spawn a new process
process = pexpect.spawn(command)

# Expect the password prompt
process.expect('Enter your encryption password:')

process.sendline(password)

# Expect the passphrase prompt
process.expect('Enter same passphrase again:')

process.sendline(passphrase)

# Expect the mnemonic code prompt
process.expect('Input mnemonic code:')

# Provide the mnemonic co
process.sendline(mnemonic_code)

# Expect the BIP39 passphrase prompt
process.expect('Enter BIP39 passphrase (empty for none):')

# Press enter for BIP39 passphrase (empty for none)
process.sendline()

# Wait for the process to finish
process.wait()

# Get the output
output = process.before.decode()

# Print the output
print(output)