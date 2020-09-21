# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SchemaTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.events.v1.schemas("id").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://events.twilio.com/v1/Schemas/id',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "id": "DataTaps.TestEventSchema",
                "url": "https://events.twilio.com/v1/Schemas/DataTaps.TestEventSchema",
                "last_created": "2018-07-30T20:00:00Z",
                "last_version": 1,
                "links": {
                    "versions": "https://events.twilio.com/v1/Schemas/DataTaps.TestEventSchema/Versions"
                }
            }
            '''
        ))

        actual = self.client.events.v1.schemas("id").fetch()

        self.assertIsNotNone(actual)
