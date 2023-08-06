"""Provides functions used to manage secrets."""
import os
from typing import Any

import requests
from google.cloud import secretmanager
from google.cloud.secretmanager import SecretManagerServiceClient
from google.oauth2.credentials import Credentials
from jupyterhub.services.auth import HubAuth


def get_secret_client() -> SecretManagerServiceClient:
    """Get a secret manager seervice client instance.

    If in a jupyterhub environment, use HubAuth, otherwise use application default credentials.
    """
    if os.getenv("NB_USER") != "jovyan":
        return secretmanager.SecretManagerServiceClient()

    hub = HubAuth()
    response = requests.get(
        os.environ["LOCAL_USER_PATH"],
        headers={"Authorization": "token %s" % hub.api_token},
        cert=(str(hub.certfile), str(hub.keyfile)),
        verify=str(hub.client_ca),
        allow_redirects=False,
    )
    token = response.json()["exchanged_tokens"]["google"]["access_token"]
    credentials = Credentials(token=token)
    return secretmanager.SecretManagerServiceClient(credentials=credentials)


def add_secret_version(project_id: str, secret_id: str, payload: Any) -> None:
    """Requests google cloud storage client to create a secret.

    Args:
        project_id: The ID of the project that the secret should be created in.
        secret_id: The ID of the secret to be created.
        payload: The payload of the secret to be created.
    """
    client = get_secret_client()

    parent = client.secret_path(project_id, secret_id)

    payload = payload.encode("UTF-8")

    response = client.add_secret_version(
        request={
            "parent": parent,
            "payload": {"data": payload},
        }
    )

    print(f"Added secret version: {response.name}")


def request_secret_creation(project_id: str, secret_id: str) -> None:
    """Requests google cloud storage client to create a secret.

    Args:
        project_id: The ID of the project that the secret should be created in.
        secret_id: The ID of the secret to be created.
    """
    client = get_secret_client()

    parent = f"projects/{project_id}"

    response = client.create_secret(
        request={
            "parent": parent,
            "secret_id": secret_id,
            "secret": {"replication": {"user_managed": {"replicas": [{"location": "europe-north1"}]}}},
        }
    )

    print(f"Created secret: {response.name}")
