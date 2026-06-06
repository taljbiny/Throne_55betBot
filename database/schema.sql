CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telegram_id BIGINT UNIQUE,
    username VARCHAR(255),
    balance DECIMAL(10,2) DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telegram_id BIGINT,
    type ENUM('deposit','withdraw','create_account'),
    amount DECIMAL(10,2) DEFAULT 0,
    status ENUM('pending','done','failed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE bot_wallet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    balance DECIMAL(15,2) DEFAULT 0
);

CREATE TABLE admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    telegram_id BIGINT UNIQUE
);
