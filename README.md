# PRODIGY_SD_3
Here’s a **README.md** file for the Contact Manager program:

```markdown
# Contact Manager

A simple GUI-based program to manage contact information. This program allows users to add, view, edit, and delete contacts. Contacts are stored persistently in a JSON file, ensuring data is saved even after the program is closed.

---

## Features

- **Add Contact:** Enter the name, phone number, and email address to create a new contact.
- **View Contacts:** See a list of all saved contacts.
- **Edit Contact:** Update the details of an existing contact.
- **Delete Contact:** Remove unwanted contacts from the list.
- **Persistent Storage:** Contacts are saved in a `contacts.json` file for future use.

---

## Requirements

- Python 3.6 or higher
- `tkinter` (comes pre-installed with Python)

---

## Installation

1. Clone the repository or download the `contact_manager.py` file.
2. Ensure Python is installed on your system:
   ```bash
   python --version
   ```

---

## Usage

1. Run the program:
   ```bash
   python contact_manager.py
   ```
2. Use the graphical interface to:
   - **Add Contact:** Fill in the name, phone number, and email fields, then click `Add Contact`.
   - **Edit Contact:** Select a contact from the list, modify the details, and click `Edit Contact`.
   - **Delete Contact:** Select a contact and click `Delete Contact`.
   - **Clear Fields:** Reset all input fields for a new entry.

---

## How It Works

- **Contact Storage:** Contacts are stored in a JSON file named `contacts.json`. This ensures all added contacts are available when you reopen the program.
- **List View:** A scrollable list displays all saved contacts. Selecting a contact populates the input fields with its details for easy editing or deletion.
- **Validation:** Ensures all fields are filled before adding or updating a contact.

---

## Example

1. **Initial Screen:**  
   - Shows empty input fields and a list of existing contacts.

2. **Adding a Contact:**  
   - Enter `John Doe`, `1234567890`, and `john.doe@example.com`. Click `Add Contact`.

3. **Editing a Contact:**  
   - Select `John Doe` from the list, update the phone number to `9876543210`, and click `Edit Contact`.

4. **Deleting a Contact:**  
   - Select `John Doe` and click `Delete Contact`. Confirm the action in the popup dialog.

---

## Screenshots

1. **Main Interface:**  
   ![Main Interface](https://via.placeholder.com/500x300?text=Main+Interface)

2. **Add/Edit/Delete Contact:**  
   ![Add/Edit/Delete](https://via.placeholder.com/500x300?text=Add+Edit+Delete)

---

## File Details

- `contact_manager.py`: Main program file.
- `contacts.json`: File for storing contact data (automatically created if not present).

---

## Contributing

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

## Author

**Your Name**  
[GitHub Profile](https://github.com/sksahil0324)   
```
