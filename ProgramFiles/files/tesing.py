import unittest
import con_to_sql as sql_conn


class LoginTest(unittest.TestCase):

    # Login Testing

    def test_login(self):
        datas = sql_conn.Login()
        datas.login('pyderator','highway')
        self.assertEqual(datas.islogged, True)

    # Accounts Management Testing

    def test_fetch_acc_info(self):
        acc = sql_conn.Account_manager(26)
        data = acc.fetch_account_info()
        self.assertEqual(len(data), 1)

    def test_pending_acc_info(self):
        acc = sql_conn.Account_manager(26)
        data = acc.pending_account_info()
        self.assertEqual(len(data), 0)

    def test_update_acc_info(self):
        acc = sql_conn.Account_manager(26)
        data = acc.update_pending_acc([{'Age': '185'}, {'Work': 'Nopea'}],36)
        self.assertEqual(data, True)

    # Esewa Transaction

    def test_load_esewa(self):
        acc = sql_conn.Transaction(26)
        data = acc.load_esewa('e81c5d7c-17bf-4f09-bb67-9359a630071e', 100)
        self.assertEqual(data, True)

unittest.main()
