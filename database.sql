-- Create users table
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
);

-- Create passwords table
CREATE TABLE passwords (
    password_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    password VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create platforms table
CREATE TABLE platforms (
    platform_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    password_id INT,
    platform VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (password_id) REFERENCES passwords(password_id)
);

--passwords should include site_username and url for future practice.