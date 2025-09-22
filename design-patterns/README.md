# Design Patterns

Implementation of classic software design patterns with examples and use cases.

## 🏗️ Pattern Categories

### Creational Patterns
- **Singleton** - Ensure only one instance exists
- **Factory Method** - Create objects without specifying exact classes
- **Abstract Factory** - Create families of related objects
- **Builder** - Construct complex objects step by step
- **Prototype** - Clone objects instead of creating new ones

### Structural Patterns
- **Adapter** - Allow incompatible interfaces to work together
- **Decorator** - Add behavior to objects dynamically
- **Facade** - Provide simplified interface to complex subsystem
- **Observer** - Define one-to-many dependency between objects
- **Strategy** - Define family of algorithms and make them interchangeable

### Behavioral Patterns
- **Command** - Encapsulate requests as objects
- **State** - Allow object to change behavior when state changes
- **Template Method** - Define skeleton of algorithm in base class
- **Visitor** - Separate algorithms from object structure
- **Chain of Responsibility** - Pass requests along chain of handlers

## 🎯 When to Use Each Pattern

| Pattern | Use Case | Benefits |
|---------|----------|----------|
| Singleton | Database connections, logging | Controlled access to single instance |
| Factory | Creating UI components | Loose coupling, easy to extend |
| Observer | Event systems, MVC | Loose coupling between subjects and observers |
| Strategy | Payment processing, sorting | Runtime algorithm selection |
| Decorator | UI enhancements, middleware | Add responsibilities without inheritance |

## 📁 Structure

```
design-patterns/
├── creational/      # Creational pattern implementations
├── structural/      # Structural pattern implementations
├── behavioral/      # Behavioral pattern implementations
├── examples/        # Real-world usage examples
└── tests/           # Pattern testing and validation
```

## 🚀 Quick Examples

Each pattern includes:
- **Intent**: What problem it solves
- **Structure**: UML diagram and participants
- **Implementation**: Working code examples
- **Real-world usage**: Practical applications
- **Pros and Cons**: Benefits and drawbacks