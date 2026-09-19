from abc import ABC, abstractmethod


# ==========================================
# PART 1: Abstract Products
# ==========================================
class Button(ABC):
    @abstractmethod
    def render(self):
        """Render the button on the screen."""
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self):
        """Render the checkbox on the screen."""
        pass


# ==========================================
# PART 2: Concrete Products (Windows & Mac)
# ==========================================
class WindowsButton(Button):
    def render(self):
        print("[Windows] Rendering a rectangular, sharp-cornered button.")


class WindowsCheckbox(Checkbox):
    def render(self):
        print("[Windows] Rendering a square checkbox with a blue checkmark.")


class MacButton(Button):
    def render(self):
        print("[macOS] Rendering a rounded, pill-shaped aqua button.")


class MacCheckbox(Checkbox):
    def render(self):
        print("[macOS] Rendering a rounded checkbox with a smooth checkmark.")


# ==========================================
# PART 3: Abstract Factory
# ==========================================
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        """Create a button component matching the OS."""
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        """Create a checkbox component matching the OS."""
        pass


# ==========================================
# PART 4: Concrete Factories
# ==========================================
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# ==========================================
# PART 5: Client Code
# ==========================================
class Application:
    """
    The client interacts ONLY with GUIFactory, Button, and Checkbox interfaces.
    It never imports or mentions WindowsButton, MacButton, etc.
    """
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def render_ui(self):
        print("Rendering user interface...")
        self.button.render()
        self.checkbox.render()


# ==========================================
# PART 6: Execution / OS Detection
# ==========================================
def get_factory_for_os(os_name: str) -> GUIFactory:
    """Simulates runtime OS configuration."""
    os_name = os_name.strip().lower()
    if os_name == "windows":
        return WindowsFactory()
    elif os_name in ("mac", "macos", "darwin"):
        return MacFactory()
    else:
        raise ValueError(f"Unsupported operating system: {os_name}")


if __name__ == "__main__":
    # Test 1: Simulating running on Windows
    print("=== Launching on Windows ===")
    current_factory = get_factory_for_os("windows")
    app = Application(current_factory)
    app.render_ui()

    print()

    # Test 2: Simulating running on macOS
    print("=== Launching on macOS ===")
    current_factory = get_factory_for_os("macos")
    app = Application(current_factory)
    app.render_ui()