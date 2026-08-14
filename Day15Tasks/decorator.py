from functools import wraps

# 1. Store users and their assigned roles in a dictionary
USER_ROLES = {
    "alice": "admin",
    "bob": "editor",
    "charlie": "viewer"
}

# Active user context (simulating a logged-in session)
CURRENT_USER = "bob"


# 2. Parametrized Decorator to check user roles
def require_role(allowed_roles):
    """
    Decorator factory that restricts function execution based on user role.
    :param allowed_roles: List or tuple of roles permitted to call the function.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Fetch current user's role from dictionary
            user_role = USER_ROLES.get(CURRENT_USER)

            # 3. Use condition inside decorator to grant or deny access
            if user_role in allowed_roles:
                return func(*args, **kwargs)
            else:
                raise PermissionError(
                    f"Access Denied for user '{CURRENT_USER}' (Role: {user_role}). "
                    f"Required roles: {allowed_roles}"
                )
        return wrapper
    return decorator


# 4. Apply decorator to multiple functions with different permissions

@require_role(["admin"])
def delete_database():
    return "Database successfully deleted!"


@require_role(["admin", "editor"])
def publish_article(title):
    return f"Article '{title}' published!"


@require_role(["admin", "editor", "viewer"])
def view_dashboard():
    return "Welcome to the dashboard!"


# --- Testing the Implementation ---
if __name__ == "__main__":
    print(f"Current logged in user: {CURRENT_USER} ({USER_ROLES[CURRENT_USER]})\n")

    # Access permitted (Editor can view dashboard)
    print(view_dashboard())

    # Access permitted (Editor can publish articles)
    print(publish_article("Python Decorators Guide"))

    # Access denied (Editor cannot delete database)
    try:
        delete_database()
    except PermissionError as e:
        print(f"\nCaught expected error:\n  {e}")
        