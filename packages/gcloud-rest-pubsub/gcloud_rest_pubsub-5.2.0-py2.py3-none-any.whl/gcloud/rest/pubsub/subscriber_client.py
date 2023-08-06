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
from copy import deepcopy
from typing import Any
from typing import AnyStr
from typing import Dict
from typing import IO
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

from gcloud.rest.auth import SyncSession  # pylint: disable=no-name-in-module
from gcloud.rest.auth import BUILD_GCLOUD_REST  # pylint: disable=no-name-in-module
from gcloud.rest.auth import Token  # pylint: disable=no-name-in-module

from .subscriber_message import SubscriberMessage

if BUILD_GCLOUD_REST:
    from requests import Session
else:
    from aiohttp import ClientSession as Session  # type: ignore[assignment]

SCOPES = [
    'https://www.googleapis.com/auth/pubsub',
]


def init_api_root(api_root               )                    :
    if api_root:
        return True, api_root

    host = os.environ.get('PUBSUB_EMULATOR_HOST')
    if host:
        return True, 'http://{}/v1'.format((host))

    return False, 'https://pubsub.googleapis.com/v1'


class SubscriberClient(object):
    #_api_root: str
    #_api_is_dev: bool

    def __init__(
            self, **_3to2kwargs
    )        :
        if 'api_root' in _3to2kwargs: api_root = _3to2kwargs['api_root']; del _3to2kwargs['api_root']
        else: api_root =  None
        if 'session' in _3to2kwargs: session = _3to2kwargs['session']; del _3to2kwargs['session']
        else: session =  None
        if 'token' in _3to2kwargs: token = _3to2kwargs['token']; del _3to2kwargs['token']
        else: token =  None
        if 'service_file' in _3to2kwargs: service_file = _3to2kwargs['service_file']; del _3to2kwargs['service_file']
        else: service_file =  None
        self._api_is_dev, self._api_root = init_api_root(api_root)

        self.session = SyncSession(session, verify_ssl=not self._api_is_dev)
        self.token = token or Token(
            service_file=service_file, scopes=SCOPES,
            session=self.session.session,  # type: ignore[arg-type]
        )

    def _headers(self)                  :
        headers = {
            'Content-Type': 'application/json',
        }
        if self._api_is_dev:
            return headers

        token = self.token.get()
        headers['Authorization'] = 'Bearer {}'.format((token))
        return headers

    # https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/create
    def create_subscription(
        self,
        subscription     ,
        topic     ,
        body                           = None, **_3to2kwargs
    )                  :
        if 'timeout' in _3to2kwargs: timeout = _3to2kwargs['timeout']; del _3to2kwargs['timeout']
        else: timeout =  10
        if 'session' in _3to2kwargs: session = _3to2kwargs['session']; del _3to2kwargs['session']
        else: session =  None
        """
        Create subscription.
        """
        body = {} if not body else body
        url = '{}/{}'.format((self._api_root), (subscription))
        headers = self._headers()
        payload                 = deepcopy(body)
        payload.update({'topic': topic})
        encoded = json.dumps(payload).encode()
        s = SyncSession(session) if session else self.session
        resp = s.put(url, data=encoded, headers=headers, timeout=timeout)
        result                 = resp.json()
        return result

    # https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/delete
    def delete_subscription(
        self, subscription     , **_3to2kwargs
    )        :
        if 'timeout' in _3to2kwargs: timeout = _3to2kwargs['timeout']; del _3to2kwargs['timeout']
        else: timeout =  10
        if 'session' in _3to2kwargs: session = _3to2kwargs['session']; del _3to2kwargs['session']
        else: session =  None
        """
        Delete subscription.
        """
        url = '{}/{}'.format((self._api_root), (subscription))
        headers = self._headers()
        s = SyncSession(session) if session else self.session
        s.delete(url, headers=headers, timeout=timeout)

    # https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/pull
    def pull(
        self, subscription     , max_messages     , **_3to2kwargs
    )                           :
        if 'timeout' in _3to2kwargs: timeout = _3to2kwargs['timeout']; del _3to2kwargs['timeout']
        else: timeout =  30
        if 'session' in _3to2kwargs: session = _3to2kwargs['session']; del _3to2kwargs['session']
        else: session =  None
        """
        Pull messages from subscription
        """
        url = '{}/{}:pull'.format((self._api_root), (subscription))
        headers = self._headers()
        payload = {
            'maxMessages': max_messages,
        }
        encoded = json.dumps(payload).encode()
        s = SyncSession(session) if session else self.session
        resp = s.post(
            url, data=encoded,
            headers=headers, timeout=timeout,
        )
        data = resp.json()
        return [
            SubscriberMessage.from_repr(m)
            for m in data.get('receivedMessages', [])
        ]

    # https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/acknowledge
    def acknowledge(
        self, subscription     , ack_ids           , **_3to2kwargs
    )        :
        if 'timeout' in _3to2kwargs: timeout = _3to2kwargs['timeout']; del _3to2kwargs['timeout']
        else: timeout =  10
        if 'session' in _3to2kwargs: session = _3to2kwargs['session']; del _3to2kwargs['session']
        else: session =  None
        """
        Acknowledge messages by ackIds
        """
        url = '{}/{}:acknowledge'.format((self._api_root), (subscription))
        headers = self._headers()
        payload = {
            'ackIds': ack_ids,
        }
        encoded = json.dumps(payload).encode()
        s = SyncSession(session) if session else self.session
        s.post(url, data=encoded, headers=headers, timeout=timeout)

    # https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/modifyAckDeadline
    def modify_ack_deadline(
        self, subscription     ,
        ack_ids           ,
        ack_deadline_seconds     , **_3to2kwargs
    )        :
        if 'timeout' in _3to2kwargs: timeout = _3to2kwargs['timeout']; del _3to2kwargs['timeout']
        else: timeout =  10
        if 'session' in _3to2kwargs: session = _3to2kwargs['session']; del _3to2kwargs['session']
        else: session =  None
        """
        Modify messages' ack deadline.
        Set ack deadline to 0 to nack messages.
        """
        url = '{}/{}:modifyAckDeadline'.format((self._api_root), (subscription))
        headers = self._headers()
        data = json.dumps({
            'ackIds': ack_ids,
            'ackDeadlineSeconds': ack_deadline_seconds,
        }).encode('utf-8')
        s = SyncSession(session) if session else self.session
        s.post(url, data=data, headers=headers, timeout=timeout)

    # https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/get
    def get_subscription(
        self, subscription     , **_3to2kwargs
    )                  :
        if 'timeout' in _3to2kwargs: timeout = _3to2kwargs['timeout']; del _3to2kwargs['timeout']
        else: timeout =  10
        if 'session' in _3to2kwargs: session = _3to2kwargs['session']; del _3to2kwargs['session']
        else: session =  None
        """
        Get Subscription
        """
        url = '{}/{}'.format((self._api_root), (subscription))
        headers = self._headers()
        s = SyncSession(session) if session else self.session
        resp = s.get(url, headers=headers, timeout=timeout)
        result                 = resp.json()
        return result

    # https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions/list
    def list_subscriptions(
        self, project     ,
        query_params                           = None, **_3to2kwargs
    )                  :
        if 'timeout' in _3to2kwargs: timeout = _3to2kwargs['timeout']; del _3to2kwargs['timeout']
        else: timeout =  10
        if 'session' in _3to2kwargs: session = _3to2kwargs['session']; del _3to2kwargs['session']
        else: session =  None
        """
        List subscriptions
        """
        url = '{}/{}/subscriptions'.format((self._api_root), (project))
        headers = self._headers()
        s = SyncSession(session) if session else self.session

        all_results                 = {'subscriptions': []}
        nextPageToken = None
        next_query_params = query_params if query_params else {}
        while True:
            resp = s.get(
                url, headers=headers, params=next_query_params,
                timeout=timeout,
            )
            page                 = resp.json()
            all_results['subscriptions'] += page['subscriptions']
            nextPageToken = page.get('nextPageToken', None)
            if not nextPageToken:
                break
            next_query_params.update({'pageToken': nextPageToken})

        return all_results

    def close(self)        :
        self.session.close()

    def __enter__(self)                      :
        return self

    def __exit__(self, *args     )        :
        self.close()
