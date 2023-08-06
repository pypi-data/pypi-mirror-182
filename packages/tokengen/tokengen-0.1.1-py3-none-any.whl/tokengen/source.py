
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from azure.core.exceptions import ResourceModifiedError
import secrets
import docker
from docker.errors import APIError, ContainerError
import logging
import sys
import subprocess
import os
import time
import randomname


"""Configure logger to stream to stdout"""
logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logger = logging.getLogger("tokengen")


credential = DefaultAzureCredential()


################################# Generate All 3 Tokens ########################################################
def generate_hex_secret(hex_value):
    """
    hex_value(16) -- 32 characters
    hex_value(40) -- 80 characters
    """
    SECRET = secrets.token_hex(hex_value)

    return SECRET


def generate_aifi_api_token_and_pepper_token(secret_name, vault_url):
    """
    Authentication procedure -- Azure CLI login
    Target -- Environment variables
    """
    secret_client = SecretClient(vault_url=vault_url, credential=credential)

    hex_30_secret = generate_hex_secret(16)         # AIFI_API_TOKEN
    hex_80_secret = generate_hex_secret(40)         # PEPPER

    try:
        """Send AIFI_API_TOKEN and PEPPER tokens to the secret in the Azurekeyvault"""
        secret = secret_client.set_secret(
            secret_name,
            "AIFI_API_TOKEN: {0}\nPEPPER: {1}".format(hex_30_secret, hex_80_secret)
            )

        os.environ['AIFI_API_TOKEN'] = hex_30_secret
        os.environ['PEPPER'] = hex_80_secret

    except ResourceModifiedError as e:
        logger.error(e.message)


def get_secret_value(vault_url, secret_name):

    secret_client = SecretClient(vault_url=vault_url, credential=credential)
    secret = secret_client.get_secret(secret_name)

    logger.info(secret.name)
    logger.info(secret.value)


def generate_oasis_api_token_for_retailer_token(username=None, password=None, email=None, registry=None, domain=None, vault_url=None, secret_name=None):
    """Push RETAILER_TOKEN to Keyvault"""
    client = docker.from_env()
    try:
        client.login(
            username=username, 
            password=password, 
            email=email,
            registry='registry.gitlab.com')

        logger.info("Successfully Logged in to registry!")
    except APIError as e:
        logger.error(e)

    try:
        """ auto_remove=True removes container after it exits """
        image_name = "registry.gitlab.com/aifi-ml/production/cloud-api/utils:2.130.0"
        environment_variables = ["type=aifi", "PEPPER={}".format(os.getenv("PEPPER")), "ADMIN={}".format(domain)]

        container = client.containers.run(image_name, environment=environment_variables, detach=True)
        print('Logs streaming...')
        time.sleep(5)
        
        proc = subprocess.Popen(["docker", "logs", f"{container.id}"], stdout=subprocess.PIPE)
        token = subprocess.check_output(('grep', 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'), stdin=proc.stdout, text=True).strip(" '").replace("token: '", "").replace("'", "")
        os.environ['oasis_token'] = token
        print(token)

    except ContainerError as e:
        print(e)

    secret_client = SecretClient(vault_url=vault_url, credential=credential)

    try:
        """Save token as RETAILER_TOKEN and push to Azurekeyvault"""
        secret = secret_client.set_secret(
            secret_name,
            "RETAILER_TOKEN: {}".format(token)
            )

        os.environ['RETAILER_TOKEN'] = token

    except ResourceModifiedError as e:
        logger.error(e.message)



def generate_keycloak_credentials(secret_name, vault_url):
    """
    KEYCLOAK_USER: admin
    KEYCLOAK_PASSWORD: ****
    """
    secret_client = SecretClient(vault_url=vault_url, credential=credential)

    KEYCLOAK_PASSWORD = '-'.join([randomname.get_name(), randomname.get_name()]) 

    try:
        """Send KEYCLOAK_USER and KEYCLOAK_PASSWORD tokens to the secret in the Azurekeyvault"""
        secret = secret_client.set_secret(
            secret_name,
            "KEYCLOAK_USER: admin\nKEYCLOAK_PASSWORD: {}".format(KEYCLOAK_PASSWORD)
            )
        os.environ['KEYCLOAK_PASSWORD'] = KEYCLOAK_PASSWORD

    except ResourceModifiedError as e:
        logger.error(e.message)



def generate_retailer_bridge_token(secret_name, vault_url):
    """
    RETAILER_BRIDGE_TOKEN: token
    """
    secret_client = SecretClient(vault_url=vault_url, credential=credential)
    secret_name = ''.join(secret_name)+"-retailer-bridge-token"
    try:
        """Send RETAILER_BRIDGE_TOKEN tokens to the secret in the Azurekeyvault"""
        secret = secret_client.set_secret(
            secret_name,
            "RETAILER_BRIDGE_TOKEN: {}".format(os.getenv('oasis_token'))
            )

        os.environ['RETAILER_BRIDGE_TOKEN'] = os.getenv('oasis_token')

    except ResourceModifiedError as e:
        logger.error(e.message)





##################### Generate Bridgetoken ################################################################################
def verify_retailer_token_already_exists(bridgetoken_name, vault_url):
    """Split the store codename/fruit, take the first part and generate the retailer secret name
       Eg: zucchini-nano-001 --> zucchini --> zucchini-cloud-oasis-api-token
    """

    secret_name = ''.join(bridgetoken_name.split('-')[0])+"-cloud-oasis-api-token"

    secret_client = SecretClient(vault_url=vault_url, credential=credential)
    secret_properties = secret_client.list_properties_of_secrets()

    secrets_list_box = []
    for secret_property in secret_properties:
        secrets_list_box.append(secret_property.name)

    try:
        assert secret_name in secrets_list_box
        print(f"{secret_name} already exists. Good to Go!")
        return secret_name

    except:
        raise AssertionError(f"{secret_name} not found in Azurekeyvault. Make sure it's already generated before you can use it to create bridgetoken")



def retrieve_retailer_token_and_create_bridgetoken(vault_url, bridgetoken_name, retailer_secret_name):
    secret_name = ''.join(bridgetoken_name)+"-retailer-bridge-token"

    secret_client = SecretClient(vault_url=vault_url, credential=credential)
    secret = secret_client.get_secret(retailer_secret_name)

    logger.info(secret.name)
    # store the retailer token in a variable
    secret_value = secret.value
    print("value here: ", secret_value)

    try:
        """Send RETAILER_BRIDGE_TOKEN tokens to the secret in the Azurekeyvault"""
        secret = secret_client.set_secret(
            secret_name,
            f"{secret_value}"
            )

    except Exception as e:
        logger.error(e)