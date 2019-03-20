# Copyright 2018 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------
     
import pytest
import logging
import json
import urllib.request
import urllib.error
import aiohttp
import inspect
  
from utils import get_peers

from base import RestApiBaseTest  
  
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
  
pytestmark = [pytest.mark.get , pytest.mark.peers]

PEER_LIST = []

@pytest.fixture(autouse=True, scope="function")
def desc_test_api_get_peers(json_metadata, request, capsys):
   
    count=0
    list3 =  [TestPeerList.test_api_get_peer_list
             ]
    for f in list3:

          json_metadata[count] = inspect.getdoc(f)
          count=count + 1
          
          
          
class TestPeerList(RestApiBaseTest):
    
    async def test_api_get_peer_list(self, setup):
     
        """This class tests the peer list with different parameters
        """  
        address = setup['address']
        expected_link = '{}/peers'.format(address)
        
        try:
            async with aiohttp.ClientSession() as session:        
                async with session.get(url='{}/peers'.format(address)) as data:
                    response = await data.json()
        except aiohttp.client_exceptions.ClientResponseError as error:
            LOGGER.info("Rest Api is Unreachable")
        
        self.assert_valid_link(response, expected_link)
        
   
