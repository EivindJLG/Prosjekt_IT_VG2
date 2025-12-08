CREATE TABLE IF NOT EXISTS produkter (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    category VARCHAR(100),
    price DECIMAL(10,2),
    description TEXT,
    image_url VARCHAR(255),
    stock INT DEFAULT 0
);

INSERT INTO produkter (name, category, price, description, image_url, stock)
VALUES
(
    "PC Core Stasjonær Gaming-PC",
    "Prebuilt",
    11499.00,
    "Windows 11, Geforce RTX 5050",
    "frontend/static/bilder/PC_Core.png",
    5
);