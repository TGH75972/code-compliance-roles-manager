import json
import os
from datetime import datetime

class RolePermissionsManager:
    def __init__(self, roles_path="data/roles_permissions.json", users_path="data/users.json"):
        self.roles_path = roles_path
        self.users_path = users_path
        self.roles_data = self._load_json(self.roles_path).get("roles", {})
        self.users_data = self._load_json(self.users_path).get("users", [])
        
        # Dictionary hash map for O(1) user lookup
        self.user_map = {u["user_id"]: u for u in self.users_data}

    def _load_json(self, filepath):
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Configuration file not found: {filepath}")
        with open(filepath, 'r') as f:
            return json.load(f)

    def get_user_role(self, user_id):
        user = self.user_map.get(user_id)
        if not user:
            return None, "User not found"
        return user.get("role"), "Success"

    def get_role_permissions(self, role_name):
        role = self.roles_data.get(role_name)
        if not role:
            return None, f"Role '{role_name}' does not exist"
        return role.get("permissions", []), "Success"

    def check_permission(self, user_id, permission_name):
        role_name, status = self.get_user_role(user_id)
        if not role_name:
            return False, status
        
        permissions, status = self.get_role_permissions(role_name)
        if permission_name in permissions:
            return True, f"Permission granted under role '{role_name}'"
        return False, f"Permission '{permission_name}' denied for role '{role_name}'"

    def assign_role(self, actor_id, target_user_id, new_role):
        if new_role not in self.roles_data:
            return False, f"Invalid role: '{new_role}'"
            
        target_user = self.user_map.get(target_user_id)
        if not target_user:
            return False, f"Target user '{target_user_id}' not found"

        old_role = target_user["role"]
        target_user["role"] = new_role
        
        # Generate append-only audit log record
        log_entry = {
            "actor_id": actor_id,
            "target_user_id": target_user_id,
            "old_role": old_role,
            "new_role": new_role,
            "timestamp": datetime.utcnow().isoformat() + "Z"
        }
        
        return True, log_entry


if __name__ == "__main__":
    manager = RolePermissionsManager()
    
    print("=== Milestone 1 Verification Demo ===")
    user_id = "usr_001"
    
    # 1. Lookup user & role
    role, _ = manager.get_user_role(user_id)
    print(f"User '{user_id}' current role: {role}")
    
    # 2. Check permission
    allowed, msg = manager.check_permission(user_id, "read_findings")
    print(f"Check 'read_findings': {allowed} ({msg})")
    
    allowed, msg = manager.check_permission(user_id, "sign_off_clearance")
    print(f"Check 'sign_off_clearance': {allowed} ({msg})")
    
    # 3. Assign new role & generate audit record
    success, log = manager.assign_role("admin_01", "usr_001", "approver")
    print(f"Assign 'approver' status: {success}")
    print(f"Audit Log Record Generated: {json.dumps(log, indent=2)}")