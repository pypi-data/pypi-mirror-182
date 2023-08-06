"""
An asynchronous client for Google Cloud KMS
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from future import standard_library
standard_library.install_aliases()
from builtins import object
import json
import os
from typing import Any
from typing import AnyStr
from typing import Dict
from typing import IO
from typing import Optional
from typing import Tuple
from typing import Union

from gcloud.rest.auth import SyncSession  # pylint: disable=no-name-in-module
from gcloud.rest.auth import BUILD_GCLOUD_REST  # pylint: disable=no-name-in-module
from gcloud.rest.auth import Token  # pylint: disable=no-name-in-module

# Selectively load libraries based on the package
if BUILD_GCLOUD_REST:
    from requests import Session
else:
    from aiohttp import ClientSession as Session  # type: ignore[assignment]


SCOPES = [
    'https://www.googleapis.com/auth/cloudkms',
]


def init_api_root(api_root               )                    :
    if api_root:
        return True, api_root

    host = os.environ.get('KMS_EMULATOR_HOST')
    if host:
        return True, 'http://{}/v1'.format((host))

    return False, 'https://cloudkms.googleapis.com/v1'


class KMS(object):
    #_api_root: str
    #_api_is_dev: bool

    def __init__(
            self, keyproject     , keyring     , keyname     ,
            service_file                                   = None,
            location      = 'global', session                    = None,
            token                  = None, api_root                = None,
    )        :
        self._api_is_dev, self._api_root = init_api_root(api_root)
        self._api_root = (
            '{}/projects/{}/locations/{}/'
            'keyRings/{}/cryptoKeys/{}'.format((self._api_root), (keyproject), (location), (keyring), (keyname))
        )

        self.session = SyncSession(session)
        self.token = token or Token(
            service_file=service_file,
            session=self.session.session,  # type: ignore[arg-type]
            scopes=SCOPES,
        )

    def headers(self)                  :
        if self._api_is_dev:
            return {'Content-Type': 'application/json'}

        token = self.token.get()
        return {
            'Authorization': 'Bearer {}'.format((token)),
            'Content-Type': 'application/json',
        }

    # https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/decrypt
    def decrypt(
        self, ciphertext     ,
        session                    = None,
    )       :
        url = '{}:decrypt'.format((self._api_root))
        body = json.dumps({
            'ciphertext': ciphertext,
        }).encode('utf-8')

        s = SyncSession(session) if session else self.session
        resp = s.post(url, headers=self.headers(), data=body)

        plaintext      = (resp.json())['plaintext']
        return plaintext

    # https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt
    def encrypt(
        self, plaintext     ,
        session                    = None,
    )       :
        url = '{}:encrypt'.format((self._api_root))
        body = json.dumps({
            'plaintext': plaintext,
        }).encode('utf-8')

        s = SyncSession(session) if session else self.session
        resp = s.post(url, headers=self.headers(), data=body)

        ciphertext      = (resp.json())['ciphertext']
        return ciphertext

    def close(self)        :
        self.session.close()

    def __enter__(self)         :
        return self

    def __exit__(self, *args     )        :
        self.close()
