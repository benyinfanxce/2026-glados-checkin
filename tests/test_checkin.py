import unittest

from checkin import checkin_succeeded, mask_email


class CheckinResultTests(unittest.TestCase):
    def test_fresh_checkin_is_success(self):
        self.assertTrue(checkin_succeeded({'message': 'Checkin! Got 19 Points'}))

    def test_legacy_repeat_is_success(self):
        self.assertTrue(checkin_succeeded({'message': 'Checkin Repeats! Please Try Tomorrow'}))

    def test_current_repeat_is_success(self):
        self.assertTrue(checkin_succeeded({
            'message': "Today's observation logged. Return tomorrow for more points."
        }))

    def test_old_domain_instruction_is_failure(self):
        self.assertFalse(checkin_succeeded({
            'message': 'please checkin via https://glados.cloud'
        }))

    def test_network_failure_is_failure(self):
        self.assertFalse(checkin_succeeded(None))

    def test_email_is_masked_for_logs(self):
        self.assertEqual(mask_email('1583987413@example.com'), '15***@example.com')


if __name__ == '__main__':
    unittest.main()
