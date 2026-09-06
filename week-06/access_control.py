import functools

# Simulated session state
current_session = {
    "username": "rajneesh",
    "is_logged_in": False
}

def login_required(func):
    """Decorator ensuring a user is authenticated before executing the function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Check login status
        if current_session.get("is_logged_in"):
            return func(*args, **kwargs)
        
        # Block execution and notify caller
        print(f"[Access Denied] You must be logged in to execute '{func.__name__}()'.")
        return None

    return wrapper

# --- Protected System Functions ---

@login_required
def view_salary():
    """Displays employee compensation."""
    print("Salary Details: Base Salary: $135,000 | Bonus: Eligible")

@login_required
def view_personal_details():
    """Displays employee profile and contact information."""
    print("Personal Details: Employee ID: EMP-4091 | Location: Auckland, NZ")

@login_required
def download_report():
    """Triggers generation and download of system compliance reports."""
    print("Report Download: Generating Q3_Security_Audit.pdf... Download complete.")

# --- Verification & Testing ---

if __name__ == "__main__":
    print("=== Test 1: User is Logged Out ===")
    current_session["is_logged_in"] = False
    view_salary()
    view_personal_details()
    download_report()

    print("\n=== Test 2: User Logs In ===")
    current_session["is_logged_in"] = True
    view_salary()
    view_personal_details()
    download_report()