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
import urllib
import json
from random import randint

from google.protobuf.json_format import MessageToDict

from transactions import SmallBankDependentTxns, \
                         SupplyChainDependentTxns
                         
 
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

@pytest.fixture(scope="function")
def setup_dep_accounts(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_account(1,'cust1', 100)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature'] 
    
    txn2=dep_txns._create_account(2,'cust2', 100, deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list=[batch1,batch2]
    return batch_list


@pytest.fixture(scope="function")
def setup_deposit_checking(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_deposit_checking(1,10000)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature'] 
    txn2=dep_txns._create_deposit_checking(2,10000,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list

@pytest.fixture(scope="function")
def setup_send_payment(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_send_payment(1,2,1)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']
    txn2=dep_txns._create_send_payment(2,1,2,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list


@pytest.fixture(scope="function")
def setup_write_check(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_write_check(1,100)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']
    txn2=dep_txns._create_write_check(2,200,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list

@pytest.fixture(scope="function")
def setup_transact_savings(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txns=dep_txns._create_transact_savings(1,100)
    txn1=dep_txns._create_transact_savings(1,100)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']

    txn2=dep_txns._create_transact_savings(1,200)
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list


@pytest.fixture(scope="function")
def setup_amalgamate_accounts(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._amalgamate_accounts(1,2)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']
    txn2=dep_txns._amalgamate_accounts(2,1,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list


@pytest.fixture(scope="function")
def setup_invalid(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn=dep_txns._create_invalid_txn()
    return txn

@pytest.fixture(scope="function")
def setup_supply_agent(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SupplyChainDependentTxns()
    txn1=dep_txns._create_agent('agent1')
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature'] 
    
    txn2=dep_txns._create_agent('agent2')
    batch2=dep_txns.create_batch([txn2])
    batch_list=[batch1,batch2]
    return batch_list
  
@pytest.fixture(scope="function")
def setup_invalid_send_payment(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_send_payment(1,2,3)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']
    txn2=dep_txns._create_send_payment(1,3,2,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list
  
@pytest.fixture(scope="function")
def setup_invalid_write_check(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_write_check(1,0)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']
    txn2=dep_txns._create_write_check(5,0,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list
  
@pytest.fixture(scope="function")
def setup_invalid_amalgamate_accounts(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._amalgamate_accounts(1,2)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']
    txn2=dep_txns._amalgamate_accounts(1,3,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list
  
@pytest.fixture(scope="function")
def setup_invalid_transact_savings(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_transact_savings(1,0)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']

    txn2=dep_txns._create_transact_savings(3,0)
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list

@pytest.fixture(scope="function")
def setup_invalid_deposit_checking(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_deposit_checking(1,0)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature'] 
    txn2=dep_txns._create_deposit_checking(5,0,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list

@pytest.fixture(scope="function")
def setup_dep_accounts_invalid(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    randomAccNum = randint(0, 1000)
    txn1=dep_txns._create_account(randomAccNum,'CustRandom', 100)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature'] 
    
    txn2=dep_txns._create_account(randomAccNum,'', 100, deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list=[batch1,batch2]
    return batch_list

@pytest.fixture(scope="function")
def setup_invalid_Address_send_payment(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_send_payment(1,2,3)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']
    txn2=dep_txns._create_send_payment_invalid_Address(2,1,2,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list

@pytest.fixture(scope="function")
def setup_invalid_Address_write_check(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_write_check(1,100)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']
    txn2=dep_txns._create_write_check_invalid_Address(2,100,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list

@pytest.fixture(scope="function")
def setup_invalid_id_dep_write_check(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_write_check(1,400)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature'] +'asd'
    txn2=dep_txns._create_write_check(2,500,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list

@pytest.fixture(scope="function")
def setup_invalid_id_dep_send_payment(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_send_payment(1,2,3)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']+'abc'
    txn2=dep_txns._create_send_payment_invalid_Address(2,1,2,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list

@pytest.fixture(scope="function")
def setup_empty_id_dep_send_payment(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_send_payment(1,2,3)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']
    txn2=dep_txns._create_send_payment_invalid_Address(2,1,2,deps=['', txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list

@pytest.fixture(scope="function")
def setup_invalid_Address_deposit_checking(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_deposit_checking(1,100)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature'] 
    txn2=dep_txns._create_deposit_checking_invalid_Address(2,100,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list

@pytest.fixture(scope="function")
def setup_invalid_Address_transact_savings(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._create_transact_savings(1,100)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']

    txn2=dep_txns._create_transact_savings_invalid_Address(2,100)
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list

@pytest.fixture(scope="function")
def setup_invalid_Address_amalgamate_accounts(request):
    """Setup method for posting batches and returning the 
       response
    """
    dep_txns=SmallBankDependentTxns()
    txn1=dep_txns._amalgamate_accounts(1,2)
    batch1=dep_txns.create_batch([txn1])
    dict = MessageToDict(
            txn1,
            including_default_value_fields=True,
            preserving_proto_field_name=True)
    txn_id=dict['header_signature']
    txn2=dep_txns._amalgamate_accounts_invalid_Address(2,1,deps=[txn_id])
    batch2=dep_txns.create_batch([txn2])
    batch_list = [batch1,batch2]
    return batch_list