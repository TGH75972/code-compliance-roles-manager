import unittest
from role_manager import RolePermissionsManager

class TestMilestone1(unittest.TestCase):
    def setUp(self):
        self.manager = RolePermissionsManager()

    def test_roles_loaded(self):
        self.assertIn("reviewer", self.manager.roles_data)
        self.assertIn("approver", self.manager.roles_data)
        self.assertIn("auditor", self.manager.roles_data)

    def test_permission_checks(self):
        allowed, _ = self.manager.check_permission("usr_001", "read_findings")
        self.assertTrue(allowed)
        
        allowed, _ = self.manager.check_permission("usr_001", "sign_off_clearance")
        self.assertFalse(allowed)

    def test_invalid_role_assignment(self):
        success, msg = self.manager.assign_role("admin", "usr_001", "super_admin")
        self.assertFalse(success)
        self.assertIn("Invalid role", msg)

if __name__ == '__main__':
    unittest.main()