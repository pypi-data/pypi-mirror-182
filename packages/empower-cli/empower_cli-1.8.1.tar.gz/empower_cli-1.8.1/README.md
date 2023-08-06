# Empower cli client

A Command Line Interface ("CLI") is designed to provide rapid access to key Empower functions without the need to construct REST calls manually.
The Empower CLI can be used to manage all Empower functions,
and certain functions may only be available via the CLI.

[Documentation](https://docs.empoweranalytics.io/empower/docs)

## How to start

1. Setup discovery URL `empowercli context set --discovery-url https://discovery.empoweranalytics.io`.
Follow step 2 or step 3.
2. Login with your domain if browser flow is used `empowercli auth login <domain>`
3. Login with credentials flow. To do that export EMPOWER_CLI_CLIENT_ID and EMPOWER_CLI_CLIENT_SECRET into environment variables. Those variables represent keycloak client id and secret. After that type
`empowercli auth login-pipeline`
4. After the login, cli lists information for this domain from the discovery service. Now you can copy one of the available empower api URLs and setup it up for context.
`empowercli empowercli context set --api-url <api-url>`
5. Now cli is able to perform commands to api endpoints, for example `empowercli api sources list`
All other commands could be checked in [docs](https://docs.empoweranalytics.io/empower/docs/cli) or with empowercli --help
