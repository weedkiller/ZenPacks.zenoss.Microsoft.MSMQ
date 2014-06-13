##############################################################################
#
# Copyright (C) Zenoss, Inc. 2014, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from Products.ZenTestCase.BaseTestCase import BaseTestCase

from ZenPacks.zenoss.Microsoft.MSMQ import MSMQQueue


class TestMSMQQueue(BaseTestCase):
    def test_contains_class(self):
        self.assertTrue(hasattr(MSMQQueue, 'MSMQQueue'))


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestMSMQQueue))
    return suite
