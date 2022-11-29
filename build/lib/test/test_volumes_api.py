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
from fusion.api.volumes_api import VolumesApi  # noqa: E501
from fusion.rest import ApiException


class TestVolumesApi(unittest.TestCase):
    """VolumesApi unit test stubs"""

    def setUp(self):
        self.api = VolumesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_volume(self):
        """Test case for create_volume

        Creates a Volume.  # noqa: E501
        """
        pass

    def test_delete_volume(self):
        """Test case for delete_volume

        Eradicate a specific volume.  # noqa: E501
        """
        pass

    def test_get_volume(self):
        """Test case for get_volume

        Gets a specific Volume.  # noqa: E501
        """
        pass

    def test_get_volume_by_id(self):
        """Test case for get_volume_by_id

        Gets a specific Volume.  # noqa: E501
        """
        pass

    def test_get_volume_performance(self):
        """Test case for get_volume_performance

        (Provider) Gets performance metrics of a specific Volume.  # noqa: E501
        """
        pass

    def test_get_volume_space(self):
        """Test case for get_volume_space

        (Provider) Gets space metrics of a specific Volume.  # noqa: E501
        """
        pass

    def test_list_volumes(self):
        """Test case for list_volumes

        Gets a list of all Volumes.  # noqa: E501
        """
        pass

    def test_query_volumes(self):
        """Test case for query_volumes

        (Opt-in) Get all Volumes in the org. Provide a filter to search for specific volumes.  # noqa: E501
        """
        pass

    def test_update_volume(self):
        """Test case for update_volume

        Updates a Volume -- renaming, and resizing it; changing its Storage Class; changing its Placement Group; adding or removing host connections.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()