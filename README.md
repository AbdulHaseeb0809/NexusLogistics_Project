# 📦 NexusLogistics Engine (OOP Project)

A professional Logistics Management System built with **Python** to demonstrate the 4 pillars of Object-Oriented Programming. This system manages different delivery types (Express & Standard) while ensuring data security and code scalability.

---

## 🚀 OOP Pillars Implemented

### 1. Abstraction
- Created a blueprint using `ABC` (Abstract Base Class).
- Every delivery type is forced to implement its own `calculate_shipping()` method.

### 2. Encapsulation
- Tracking IDs are kept **private** (`__tracking_id`) to prevent unauthorized tampering.
- Used the `@property` decorator to provide safe, read-only access.

### 3. Inheritance
- Specialized classes like `Express_Delivery` and `Standard_Delivery` inherit from `Base_Delivery`.
- This keeps the code **DRY** (Don't Repeat Yourself).

### 4. Polymorphism
- A single loop in `main.py` handles different delivery objects.
- Python dynamically calls the correct shipping calculation based on the object type.

---

## 📂 Project Structure
```text
NexusLogistics_Project/
├── models/
│   ├── __init__.py
│   ├── base.py            # Abstraction & Encapsulation
│   └── delivery_types.py   # Inheritance & Overriding
├── main.py                # Polymorphism & Execution
└── README.md              # Documentation

🖥️ Sample Output
Bash
--- NexusLogistics Shipping Summary ---
Fetching Tracking id Safely...
item : laptop | ID : NEXUS-123 | Cost : &7500
Fetching Tracking id Safely...
item : Book | ID : NEXUS-123 | Cost : &2500
Fetching Tracking id Safely...
item : Mobile | ID : NEXUS-123 | Cost : &4500