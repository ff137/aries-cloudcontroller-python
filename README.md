<p align="center">
  <br />
  <img
    alt="Hyperledger Aries logo"
    src="https://raw.githubusercontent.com/didx-xyz/aries-cloudcontroller-python/main/assets/aries-logo.png"
    height="250px"
  />
</p>
<h1 align="center"><b>Aries Cloud Controller Python</b></h1>
<p align="center">
  <img
    alt="Pipeline Status"
    src="https://github.com/didx-xyz/aries-cloudcontroller-python/actions/workflows/python-publish.yml/badge.svg?branch=main"
  />
        <a href="https://pypi.org/project/aries-cloudcontroller/">
        <img alt="aries-cloudcontroller version" src="https://badge.fury.io/py/aries-cloudcontroller.svg"/>
      </a>
  <a
    href="https://raw.githubusercontent.com/didx-xyz/aries-cloudcontroller-python/main/LICENSE"
    ><img
      alt="License"
      src="https://img.shields.io/badge/License-Apache%202.0-blue.svg"
  /></a>
  <a href="https://www.python.org/"
    ><img
      alt="Python"
      src="https://img.shields.io/badge/%3C%2F%3E-Python-%230074c1.svg"
  /></a>
</p>
<br />

<p align="center">
  <a href="#features">Features</a> &nbsp;|&nbsp;
  <a href="#usage">Usage</a> &nbsp;|&nbsp;
  <a href="#available-apis">Available APIs</a> &nbsp;|&nbsp;
  <a href="#contributing">Contributing</a> &nbsp;|&nbsp;
  <a href="#license">License</a>
</p>

Aries Cloud Controller Python is a client library, written in Python, for interacting with an instance of [Aries Cloud Agent Python](https://github.com/hyperledger/aries-cloudagent-python) (ACA-Py). It is generated based on the OpenAPI definition provided by ACA-Py, offering a fully-typed and comprehensive API for interacting with the cloud agent.

Furthermore, the library supports integration with FastAPI to streamline the creation of robust and scalable API services. FastAPI can help handle requests asynchronously, offering high performance even with high traffic, making Aries Cloud Controller Python an optimal choice for large-scale applications.

Each version of Aries Cloud Controller corresponds to a specific ACA-Py version, as outlined in the table below.

| Aries Cloud Controller Version | Aries Cloud Agent Python Version |
| ------------------------------ | -------------------------------- |
| 0.5.1-0.5.2                    | 0.7.3                            |
| 0.6.0-0.6.3                    | 0.7.4                            |
| 0.7.0                          | 0.7.5                            |
| 0.8.0                          | 0.8.0                            |

## Features

Aries Cloud Controller Python offers a fully featured client for interacting with ACA-Py. It provides:

- Fully typed wrapper around Aries Cloud Agent Python
- Compatibility with the latest ACA-Py version (0.8.0)
- Auto generation based on OpenAPI definitions, ensuring alignment with new releases
- Support for multi-tenant APIs and authentication
- Asynchronous API
- Integration with FastAPI for high-performance API services

## Usage

Aries Cloud Controller Python is published on PyPi and can be installed using pip:

```sh
pip install aries-cloudcontroller
```

### Creating a client

```python
from aries_cloudcontroller import AcaPyClient

client = AcaPyClient(
    base_url="http://localhost:8000",
    api_key="myApiKey"
)
```

#### Admin insecure mode

If you are running ACA-Py with the admin insecure flag and don't have an API key, you must set the `admin_insecure` property:

```python
client = AcaPyClient(
    base_url="http://localhost:8000",
    # Explicitly mark that no api key is used
    admin_insecure=True
)
```

#### Multitenancy

To provision the agent in the context of a specific tenant of the agent, set the `tenant_jwt` property:

```python
client = AcaPyClient(
    base_url="http://localhost:8000",
    tenant_jwt="eyXXX"
)
```

### Interacting with the client

Once the client is set up, you're ready to interact with it. As the API is fully typed, the best way to discover available operations is by exploring the ACA-Py swagger UI, or the properties on the client.

For example, to create and receive an invitation, call the following methods:

```python
invitation = await client.connection.create_invitation(
    body=CreateInvitationRequest(my_label="Cloud Controller")
)

connection = await client.connection.receive_invitation(body=result.invitation)
```

## Available APIs

The following top-level APIs are currently available in the client. Each API maps to the topics used by the ACA-Py swagger UI:

- `action_menu`
- `basicmessage`
- `connection`
- `credential_definition`
- `credentials`
- `default`
- `did_exchange`
- `discover_features`
- `discover_features_v2_0`
- `endorse_transaction`
- `introduction`
- `issue_credential_v1_0`
- `issue_credential_v2_0`
- `jsonld`
- `ledger`
- `mediation`
- `multitenancy`
- `out_of_band`
- `present_proof_v1_0`
- `present_proof_v2_0`
- `resolver`
- `revocation`
- `schema`
- `server`
- `trustping`
- `wallet`

## Contributing

If you're interested in contributing to this project, please read the [CONTRIBUTING](/CONTRIBUTING.md) guidelines. These documents will provide more information to help you get started!

## License

Aries Cloud Controller Python is licensed under the [Apache License Version 2.0 (Apache-2.0)](/LICENSE).
