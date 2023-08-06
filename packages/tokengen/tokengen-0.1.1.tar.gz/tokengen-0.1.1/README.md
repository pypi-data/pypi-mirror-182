

# Configure Azure CLI from CLI or Environment Variables
```sh
# 1. Authenticate with Azure CLI Creds from Terminal 
az login 

# 2. Authenticate with Environmental variables
export AZURE_CLIENT_ID="*******"
export AZURE_TENANT_ID="*******"
export AZURE_CLIENT_SECRET="*******"

# Make sure Role has Azurekeyvault read/write permissions
```

# Authenticate with Gitlab Registry
```sh
# In order not to be passing flags for the gitlab credentials, export them once on your terminal session
export username="*******"
export email="*******"
export password="*******"
```

# How to Setup
```sh
# Create virtual environment -- Optional
python -m venv venv && source venv/bin/activate

# Install via pip
pip install tokengen

# Check commands and subcommands
tokengen -h

# Available subcommands
tokengen generate               # To create 4 Tokens at Once
tokengen bridgetoken            # To optionally create Bridgetoken later
```

# How to generate tokens
```sh
# Create and Store 4 Tokens in Azurekeyvault at ONCE -- Optional(bridgetoken)
# 1. AIFI_API_TOKEN and PEPPER Token as retailere>-cloud-oasis-api-retailer-token
# 2. KEYCLOAK credentials as <retailer>-cloud-keycloak-admin
# 3. RETAILER_TOKEN and oasis-api-token secret as <retailer>-cloud-oasis-api-token
# 4. RETAILER_BRIDGE_TOKEN as <store-id>-retailer-bridge-token
```

# Generate 4 Tokens at ONCE
```sh
# --btoken is optional if you want to generate a Bridgetoken, else just elimimate it from the --flags
tokengen generate --vault <vault_name> \
        --vault_url <vault_url> \
        --secret <secret_name> \
        --domain <store-domain-prefix> \
        --btoken ronaldo-express-003


# To Use Default credentials of keyvault, Run
tokengen generate --secret <retailer_name_example_zucchini> --domain holtebar

```

# Generate Bridgetoken separately
```sh
# tokengen bridgetoken --btoken <store-id>
tokengen bridgetoken --btoken umari-express-0001
```

## Why Python Secrets?
```sh
# From Python Docs
The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.

In particularly, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling and simulation, not security or cryptography.
```

# To Contribute, Setup Environment
```sh
# create venv
python3 -m venv venv

# Activate the venv
source venv/bin/activate

# Install packages
pip install -r requirements.txt

# Switch to developer mode
python3 setup.py develop

# To test with your Azure keyvault, pass these flags to bypass default flags set for keyvault
--vault
--vault_url
```