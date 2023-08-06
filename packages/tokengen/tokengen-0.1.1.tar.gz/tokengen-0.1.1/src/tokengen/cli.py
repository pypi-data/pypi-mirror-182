
from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser(description="""
    Azurekeyvault Tokens Automation
    """)

    subparsers = parser.add_subparsers(
        title='subcommads',
        help='choose one of the subcommands with -h flag to see more',
        description='valid subcommands',
        dest='cmd',
        required=True
        )

    generate = subparsers.add_parser('generate', help='Generate all 3 Tokens at once. To see more, use --help/-h')
    bridgetoken = subparsers.add_parser('bridgetoken', help='Generate a bridgetoken for a store. To see more, use --help/-h')

    generate.add_argument(
        "--vault", '-v',
        help='Azure keyvault name',
        nargs=1,
        default='aifi-client'
    )
    generate.add_argument(
        "--vault_url", '-vu',
        help='Keyvault URL',
        nargs=1,
        default='https://aifi-client.vault.azure.net/'
    )
    generate.add_argument(
        "--secret", '-s',
        help='Retailer name for keyvault secret eg; zucchini',
        nargs=1,
        required=True
    )
    generate.add_argument(
        "--username", '-u',
        help='Username of GitLab Registry',
        nargs=1,
    )
    generate.add_argument(
        "--email", '-e',
        help='Email of GitLab Registry',
        nargs=1,
    )
    generate.add_argument(
        "--password", '-p',
        help='Password of GitLab Registry',
        nargs=1,
    )
    generate.add_argument(
        "--domain", '-d',
        help='Prefix of the Domain of the store from shopify',
        nargs=1,
        required=True
    )
    generate.add_argument(
        "--btoken", '-b',
        help='Store of client code or fruit (eg; zucchini-nano-001)',
        nargs=1,
    )


    bridgetoken.add_argument(
        "--btoken", '-b',
        help='Store/client ID code or fruit name (eg; zucchini-nano-001)',
        nargs=1,
        required=True
    )
    bridgetoken.add_argument(
        "--vault_url", '-vu',
        help='Keyvault URL',
        nargs=1,
        default='https://aifi-client.vault.azure.net/'
    )
   

    return parser


def main():
    from tokengen.source import (
        generate_aifi_api_token_and_pepper_token,
        generate_oasis_api_token_for_retailer_token,
        generate_keycloak_credentials, 
        generate_retailer_bridge_token,
        retrieve_retailer_token_and_create_bridgetoken,
        verify_retailer_token_already_exists,
    )
    import logging
    import os
    import sys


    """Configure logger to stream to stdout"""
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    logger = logging.getLogger("tokengen")

    args = create_parser().parse_args()

    
    if args.cmd == "generate":
        """Generate aifi and pepper tokens and push to Azure keyvault"""
        aifi_secret_name = ''.join(args.secret)+"-cloud-oasis-api-retailer-token"
        generate_aifi_api_token_and_pepper_token(aifi_secret_name, ''.join(args.vault_url))


        """Use Pepper token and Domain Prefix to generate oasis token"""
        def inject_registry_credentials():
            retailer_secret_name = ''.join(args.secret)+"-cloud-oasis-api-token"
            
            if os.getenv("username") and os.getenv("email") and os.getenv("password"):
                logger.info("Using GitLab Credentials from Environment Variables")
                generate_oasis_api_token_for_retailer_token(
                    username=''.join(os.getenv("username")),
                    email=''.join(os.getenv("email")),
                    password=''.join(os.getenv("password")), 
                    domain=''.join(args.domain),
                    vault_url=''.join(args.vault_url),
                    secret_name=retailer_secret_name,
                )
            else:
                logger.info("Using GitLab Credentials from CLI input values"),
                generate_oasis_api_token_for_retailer_token(
                    username=''.join(args.username),
                    email=''.join(args.email),
                    password=''.join(args.password), 
                    domain=''.join(args.domain),
                    vault_url=''.join(args.vault_url),
                    secret_name=retailer_secret_name,
                )

        # Inject GitLab Credentials from Environmental variables else, use input from CLI 
        inject_registry_credentials()


        """Generate keycloak admin tokens"""
        keycloak_secret_name = ''.join(args.secret)+"-cloud-keycloak-admin"
        generate_keycloak_credentials(keycloak_secret_name, ''.join(args.vault_url))


        if args.btoken:
            print("Bridge accepted: ", args.btoken)
            """Generate Retailer bridge token"""
            bridge_secret_name = ''.join(args.secret)+"-retailer-bridge-token"
            generate_retailer_bridge_token(bridge_secret_name, ''.join(args.vault_url))


    if args.cmd == 'bridgetoken':
        
        """Verify that the bridgetoken you're about to create already has an existing retailer token in Azurekeyvault
        Then pass the value to the retrieve_retailer_token_and_create_bridgetoken() function as retailer_secret
        """
        retailer_secret = verify_retailer_token_already_exists(''.join(args.btoken), ''.join(args.vault_url))

        retrieve_retailer_token_and_create_bridgetoken(''.join(args.vault_url), ''.join(args.btoken), retailer_secret)


    print('All Processes completed!')

