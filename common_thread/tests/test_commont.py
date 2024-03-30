from odoo.tests.common import TransactionCase
from odoo.service import server

class TestCommon(TransactionCase):

    def test_common(self):

        import wdb;wdb.set_trace()

        if not hasattr(server,'common_data'):
            server.common_data = dict()
