"""
Design Patterns Implementation in Python

This module demonstrates various creational design patterns
with practical examples and use cases.
"""

import threading
from abc import ABC, abstractmethod
from typing import Any, Dict, List
import copy


# SINGLETON PATTERN
class Singleton:
    """
    Singleton pattern ensures only one instance of a class exists.
    
    Use cases:
    - Database connection pools
    - Logger instances
    - Configuration settings
    - Cache managers
    """
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.data = {}
            self.initialized = True
    
    def set_data(self, key: str, value: Any):
        self.data[key] = value
    
    def get_data(self, key: str) -> Any:
        return self.data.get(key)


class DatabaseConnection(Singleton):
    """Example: Database connection singleton"""
    
    def __init__(self):
        super().__init__()
        if not hasattr(self, 'connected'):
            self.connected = False
            self.connection_string = ""
    
    def connect(self, connection_string: str):
        if not self.connected:
            self.connection_string = connection_string
            self.connected = True
            print(f"Connected to database: {connection_string}")
        else:
            print("Already connected to database")
    
    def execute_query(self, query: str):
        if self.connected:
            print(f"Executing query: {query}")
            return f"Result for: {query}"
        else:
            raise Exception("Not connected to database")


# FACTORY METHOD PATTERN
class Product(ABC):
    """Abstract product interface"""
    
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Product A operation"


class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Product B operation"


class Creator(ABC):
    """Abstract creator class"""
    
    @abstractmethod
    def factory_method(self) -> Product:
        pass
    
    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: Working with {product.operation()}"


class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()


# Real-world Factory example: UI Button Factory
class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass
    
    @abstractmethod
    def on_click(self) -> str:
        pass


class WindowsButton(Button):
    def render(self) -> str:
        return "Rendered Windows button"
    
    def on_click(self) -> str:
        return "Windows button clicked"


class MacButton(Button):
    def render(self) -> str:
        return "Rendered Mac button"
    
    def on_click(self) -> str:
        return "Mac button clicked"


class ButtonFactory:
    @staticmethod
    def create_button(os_type: str) -> Button:
        if os_type.lower() == "windows":
            return WindowsButton()
        elif os_type.lower() == "mac":
            return MacButton()
        else:
            raise ValueError(f"Unsupported OS type: {os_type}")


# BUILDER PATTERN
class House:
    """Complex object to be built"""
    
    def __init__(self):
        self.foundation = None
        self.walls = None
        self.roof = None
        self.windows = 0
        self.doors = 0
        self.garage = False
    
    def __str__(self):
        return (f"House with {self.foundation} foundation, "
                f"{self.walls} walls, {self.roof} roof, "
                f"{self.windows} windows, {self.doors} doors"
                f"{', with garage' if self.garage else ''}")


class HouseBuilder:
    """Builder for constructing House objects"""
    
    def __init__(self):
        self.house = House()
    
    def set_foundation(self, foundation: str):
        self.house.foundation = foundation
        return self
    
    def set_walls(self, walls: str):
        self.house.walls = walls
        return self
    
    def set_roof(self, roof: str):
        self.house.roof = roof
        return self
    
    def add_windows(self, count: int):
        self.house.windows = count
        return self
    
    def add_doors(self, count: int):
        self.house.doors = count
        return self
    
    def add_garage(self):
        self.house.garage = True
        return self
    
    def build(self) -> House:
        return self.house


class HouseDirector:
    """Director that knows how to build specific house types"""
    
    @staticmethod
    def build_simple_house(builder: HouseBuilder) -> House:
        return (builder
                .set_foundation("concrete")
                .set_walls("brick")
                .set_roof("tile")
                .add_windows(4)
                .add_doors(1)
                .build())
    
    @staticmethod
    def build_luxury_house(builder: HouseBuilder) -> House:
        return (builder
                .set_foundation("reinforced concrete")
                .set_walls("stone")
                .set_roof("slate")
                .add_windows(10)
                .add_doors(3)
                .add_garage()
                .build())


# PROTOTYPE PATTERN
class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Document(Prototype):
    """Document that can be cloned"""
    
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content
        self.metadata = {}
    
    def clone(self):
        """Create a deep copy of the document"""
        cloned = Document(self.title, self.content)
        cloned.metadata = copy.deepcopy(self.metadata)
        return cloned
    
    def set_metadata(self, key: str, value: Any):
        self.metadata[key] = value
    
    def __str__(self):
        return f"Document: {self.title}\nContent: {self.content}\nMetadata: {self.metadata}"


class DocumentManager:
    """Manages document prototypes"""
    
    def __init__(self):
        self._prototypes = {}
    
    def register_prototype(self, name: str, prototype: Document):
        self._prototypes[name] = prototype
    
    def create_document(self, prototype_name: str, title: str = None) -> Document:
        if prototype_name not in self._prototypes:
            raise ValueError(f"Prototype {prototype_name} not found")
        
        doc = self._prototypes[prototype_name].clone()
        if title:
            doc.title = title
        return doc


# ABSTRACT FACTORY PATTERN
class GUIFactory(ABC):
    """Abstract factory for creating GUI components"""
    
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_checkbox(self):
        pass


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendered Windows checkbox"


class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "Rendered Mac checkbox"


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


class Application:
    """Application that uses abstract factory"""
    
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None
    
    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()
    
    def render_ui(self) -> str:
        return f"{self.button.render()}, {self.checkbox.render()}"


# Example usage and demonstration
if __name__ == "__main__":
    print("=== Creational Design Patterns Demo ===\n")
    
    # 1. Singleton Pattern
    print("1. SINGLETON PATTERN")
    print("-" * 30)
    
    # Test singleton behavior
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    
    print(f"Same instance: {db1 is db2}")  # Should be True
    
    db1.connect("postgresql://localhost:5432/mydb")
    print(f"DB2 connected: {db2.connected}")  # Should be True
    
    result = db2.execute_query("SELECT * FROM users")
    print(f"Query result: {result}")
    
    print()
    
    # 2. Factory Method Pattern
    print("2. FACTORY METHOD PATTERN")
    print("-" * 30)
    
    # Test button factory
    windows_button = ButtonFactory.create_button("windows")
    mac_button = ButtonFactory.create_button("mac")
    
    print(windows_button.render())
    print(windows_button.on_click())
    print(mac_button.render())
    print(mac_button.on_click())
    
    print()
    
    # 3. Builder Pattern
    print("3. BUILDER PATTERN")
    print("-" * 30)
    
    # Build different types of houses
    builder = HouseBuilder()
    
    simple_house = HouseDirector.build_simple_house(builder)
    print(f"Simple house: {simple_house}")
    
    builder = HouseBuilder()  # Reset builder
    luxury_house = HouseDirector.build_luxury_house(builder)
    print(f"Luxury house: {luxury_house}")
    
    # Build custom house
    builder = HouseBuilder()
    custom_house = (builder
                   .set_foundation("steel")
                   .set_walls("glass")
                   .set_roof("green")
                   .add_windows(20)
                   .add_doors(2)
                   .build())
    print(f"Custom house: {custom_house}")
    
    print()
    
    # 4. Prototype Pattern
    print("4. PROTOTYPE PATTERN")
    print("-" * 30)
    
    # Create document manager and register prototypes
    doc_manager = DocumentManager()
    
    # Create prototype documents
    report_prototype = Document("Monthly Report Template", "Report content template...")
    report_prototype.set_metadata("type", "report")
    report_prototype.set_metadata("format", "PDF")
    
    letter_prototype = Document("Business Letter Template", "Dear [Name],\n\nContent...\n\nSincerely,")
    letter_prototype.set_metadata("type", "letter")
    letter_prototype.set_metadata("format", "DOC")
    
    # Register prototypes
    doc_manager.register_prototype("report", report_prototype)
    doc_manager.register_prototype("letter", letter_prototype)
    
    # Create documents from prototypes
    january_report = doc_manager.create_document("report", "January Report")
    january_report.content = "January sales were excellent..."
    
    client_letter = doc_manager.create_document("letter", "Client Welcome Letter")
    client_letter.content = "Dear Client,\n\nWelcome to our service!\n\nSincerely,"
    
    print("Original report prototype:")
    print(report_prototype)
    print("\nCloned January report:")
    print(january_report)
    
    print()
    
    # 5. Abstract Factory Pattern
    print("5. ABSTRACT FACTORY PATTERN")
    print("-" * 30)
    
    # Create applications for different platforms
    windows_factory = WindowsFactory()
    windows_app = Application(windows_factory)
    windows_app.create_ui()
    print(f"Windows UI: {windows_app.render_ui()}")
    
    mac_factory = MacFactory()
    mac_app = Application(mac_factory)
    mac_app.create_ui()
    print(f"Mac UI: {mac_app.render_ui()}")
    
    print("\n=== Pattern Benefits ===")
    print("✓ Singleton: Controlled instance creation and global access")
    print("✓ Factory Method: Loose coupling and easy extensibility")
    print("✓ Builder: Step-by-step construction of complex objects")
    print("✓ Prototype: Efficient object cloning and customization")
    print("✓ Abstract Factory: Consistent object families creation")