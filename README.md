# Password Manager

A secure and efficient password manager built with Python and MySQL. This password manager aims to help users save and manage their passwords securely, suggest strong passwords, and ensure overall password security through various features.

## Features

- **Save Passwords**: Save user passwords along with the platform information.
- **Suggest Strong Passwords**: Generate and suggest strong passwords for users.
- **Retrieve User Passwords**: Retrieve stored passwords for users.
- **Password Hashing**: Encode or hash passwords before storing them in the database.
- **Strength Analysis**: Analyze the strength of stored passwords.
- **Breach Monitoring**: Notify users if their passwords are found in known data breaches.
- **Password Reuse Alerts**: Alert users when they reuse passwords across multiple sites.
- **Password Sharing**: Securely share passwords with trusted contacts.
- **Password Encryption**: Encrypt passwords before storing them.
- **Emergency Access**: Provide trusted contacts with emergency access to the account in case of an emergency.
- **Store Passwords in MySQL Database**: Store all user passwords in a MySQL database.

## Installation

1. **Clone the Repository**:

   ```git
   git clone https://github.com/yourusername/password-manager.git
   cd password-manager
   ```

2. **Install Dependencies**:

   ```bash
   pip install mysql-connector-python bcrypt
   ```

3. **Setup MySQL Database**:

   - Ensure MAMP is installed and running.
   - Create a database named `pwuser` and the necessary tables:

   ```sql
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       username VARCHAR(50) NOT NULL UNIQUE,
       password_hash VARCHAR(255) NOT NULL,
       email VARCHAR(100) NOT NULL UNIQUE,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );

   CREATE TABLE passwords (
       id INT AUTO_INCREMENT PRIMARY KEY,
       user_id INT NOT NULL,
       site_name VARCHAR(100) NOT NULL,
       site_url VARCHAR(255),
       site_username VARCHAR(50),
       site_password VARCHAR(255) NOT NULL,
       created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
       FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
   );
   ```

## Usage

1. **Run the Application**:

   ```bash
   python password_manager.py
   ```

2. **Create a New User**:

   - Follow the prompts to create a new user account.

3. **Login**:

   - Login with your credentials to access the password manager.

4. **Store a New Password**:
   - After logging in, choose the option to store a new password and follow the prompts.

## Planned Features

- **Unlimited Number of Passwords**: Allow users to store an unlimited number of passwords.
- **Retrieve User Passwords**: Implement functionality to retrieve and display stored passwords for users.
- **Encode or Hash Passwords**: Ensure all passwords are securely hashed before storage.
- **Breach Monitoring**: Integrate with third-party APIs to monitor and notify users of password breaches.
- **Password Reuse Alerts**: Implement alerts to notify users of password reuse across different sites.
- **Password Sharing**: Develop a secure method for users to share passwords with trusted contacts.
- **Password Encryption**: Add an extra layer of security by encrypting passwords before storing them.
- **Emergency Access**: Provide a feature for trusted contacts to gain emergency access to the account.

## Contribution

Contributions are welcome! Please fork this repository and submit pull requests for any features or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [bcrypt](https://github.com/pyca/bcrypt)
- [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/)
- [getpass](https://docs.python.org/3/library/getpass.html)
