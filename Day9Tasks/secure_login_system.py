def login_required(func):
    def wrapper(*args, **kwargs):
        if not is_logged_in:
            print("Access denied! Please log in first.")
            return
        return func(*args, **kwargs)
    return wrapper


is_logged_in = False


@login_required
def view_profile():
    print("Displaying user profile...")


@login_required
def view_dashboard():
    print("Displaying dashboard...")


print("Attempt 1: Not logged in")
view_profile()

print("\nLogging in...")
is_logged_in = True

print("\nAttempt 2: Logged in")
view_profile()
view_dashboard()
