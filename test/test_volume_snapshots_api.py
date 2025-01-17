# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import fusion
from fusion.api.volume_snapshots_api import VolumeSnapshotsApi  # noqa: E501
from fusion.rest import ApiException


class TestVolumeSnapshotsApi(unittest.TestCase):
    """VolumeSnapshotsApi unit test stubs"""

    def setUp(self):
        self.api = VolumeSnapshotsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_query_volume_snapshots(self):
        """Test case for query_volume_snapshots

        (Opt-in) Get all Volume Snapshots in the org. Provide a filter to search for specific volume snapshots.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
