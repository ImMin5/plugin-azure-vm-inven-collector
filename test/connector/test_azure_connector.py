import unittest
import os
from datetime import datetime, timedelta
from unittest.mock import patch

from spaceone.core.unittest.result import print_data
from spaceone.core.unittest.runner import RichTestRunner
from spaceone.core import config
from spaceone.core import utils
from spaceone.core.transaction import Transaction
from spaceone.inventory.connector.azure_vm_connector import AzureVMConnector


class TestAzureConnector(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        config.init_conf(package='spaceone.monitoring')
        config_path = os.environ.get('TEST_CONFIG')
        test_config = utils.load_yaml_from_file(config_path)

        cls.schema = 'azure_client_secret'
        cls.azure_credentials = test_config.get('AZURE_CREDENTIALS', {})
        cls.azure_connector = AzureVMConnector(Transaction(), {})
        super().setUpClass()

    @classmethod
    def tearDownClass(cls) -> None:
        super().tearDownClass()

    def test_set_connect_with_azure_credential(self):
        self.azure_connector.set_connect(self.azure_credentials)

    def test_list_resource_groups(self):
        self.test_set_connect_with_azure_credential()
        return self.azure_connector.list_resource_groups()

    def test_list_vms(self):
        vms = self.azure_connector.list_vms('cloudone-test', )

        for vm in vms:
            print('0000')
            print(vm)
            print('0000')


if __name__ == "__main__":
    unittest.main(testRunner=RichTestRunner)
