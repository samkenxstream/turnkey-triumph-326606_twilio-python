import unittest
from mock import patch, Mock

from tests.tools import create_mock_json
from twilio.rest.resources.sip.ip_access_control_lists import (
    IpAddress,
    IpAddresses,
)
from twilio.rest.resources.util import UNSET_TIMEOUT


class SipIpAddressTest(unittest.TestCase):
    ACCOUNT_SID = 'AC123'
    AUTH = (ACCOUNT_SID, 'token')
    API_URI = 'https://api.twilio.com/2010-04-01/Accounts'
    BASE_URI = '%s/%s/SIP' % (API_URI, ACCOUNT_SID)
    SID = 'AL123'

    def setUp(self):
        self.list_resource = IpAddresses(self.BASE_URI, self.AUTH,
                                         UNSET_TIMEOUT)
        self.instance_resource = IpAddress(self.list_resource,
                                           self.SID)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_load(self, mock):
        resp = create_mock_json('tests/resources/sip/'
                                'sip_ip_address_list.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/IpAddresses' % (self.BASE_URI)
        self.list_resource.list().execute()

        mock.assert_called_with("GET", uri, params={}, auth=self.AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_create(self, mock):
        resp = create_mock_json('tests/resources/sip/'
                                'sip_ip_address_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/IpAddresses' % (self.BASE_URI)
        self.list_resource.create(friendly_name='cred', ip_address='ip').execute()

        data = {
            'FriendlyName': 'cred',
            'IpAddress': 'ip'
        }
        mock.assert_called_with("POST", uri, data=data,
                                auth=self.AUTH, use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_fetch(self, mock):
        resp = create_mock_json('tests/resources/sip/'
                                'sip_ip_address_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/IpAddresses/%s' % (self.BASE_URI, self.SID)
        self.list_resource.get(self.SID).execute()

        mock.assert_called_with("GET", uri, auth=self.AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_delete(self, mock):
        resp = Mock()
        resp.status_code = 204
        mock.return_value = resp

        uri = '%s/IpAddresses/%s' % (self.BASE_URI, self.SID)
        self.list_resource.delete(self.SID).execute()

        mock.assert_called_with("DELETE", uri, auth=self.AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_list_update(self, mock):
        resp = create_mock_json('tests/resources/sip/'
                                'sip_ip_address_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/IpAddresses/%s' % (self.BASE_URI, self.SID)
        self.list_resource.update(self.SID, friendly_name='cred').execute()

        mock.assert_called_with("POST", uri,
                                data={'FriendlyName': 'cred'},
                                auth=self.AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_instance_update(self, mock):
        resp = create_mock_json('tests/resources/sip/'
                                'sip_ip_address_instance.json')
        resp.status_code = 201
        mock.return_value = resp

        uri = '%s/IpAddresses/%s' % (self.BASE_URI, self.SID)
        self.instance_resource.update(friendly_name='cred').execute()

        mock.assert_called_with("POST", uri, data={'FriendlyName': 'cred'},
                                auth=self.AUTH,
                                use_json_extension=True)

    @patch("twilio.rest.resources.base.make_twilio_request")
    def test_instance_delete(self, mock):
        resp = Mock()
        resp.status_code = 204
        mock.return_value = resp

        uri = '%s/IpAddresses/%s' % (self.BASE_URI, self.SID)
        self.instance_resource.delete().execute()

        mock.assert_called_with("DELETE", uri,
                                auth=self.AUTH,
                                use_json_extension=True)