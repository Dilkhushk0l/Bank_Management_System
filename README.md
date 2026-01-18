# Bank_Management_System
Bank_Management_System – Python OOP-Based Banking Application
Bank_Management_System is a console-based banking application developed using Python. It demonstrates how core programming concepts—especially functions and object-oriented programming (OOP)—can be applied to build a real-world system for managing bank accounts.



How Python Functions Are Used
Modular Design: Each operation
(e.g., creating an account, saving data) is encapsulated in a separate function, promoting code reuse and clarity.



Input Validation: Functions handle user input and ensure data like age and PIN meet required conditions.



Data Persistence: A dedicated function (save_data) writes account information to a JSON file, ensuring data is stored between sessions.




How OOP Concepts Are Applied
Class Definition (Bank): The entire system is structured around a Bank class, which encapsulates data and behavior related to banking operations.

Encapsulation: Account data and methods are bundled within the class, keeping the internal state protected and organized.

Instance Methods: Operations like create_account, save_data, and generate_account_number are defined as methods that act on the class instance.

Constructor (__init__): Initializes the system by loading existing data or starting fresh if no file is found.
