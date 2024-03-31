DROP TABLE IF EXISTS `users`;
DROP TABLE IF EXISTS `profiles`;

CREATE TABLE users (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `first_name` VARCHAR(50) NULL,
    `last_name` VARCHAR(50) NULL,
    `username` VARCHAR(50) UNIQUE NOT NULL,
    `email` VARCHAR(100) UNIQUE NOT NULL,
    `is_admin` BOOLEAN DEFAULT 0 NOT NULL,
    `is_staff` BOOLEAN DEFAULT 0 NOT NULL,
    `is_active` BOOLEAN DEFAULT 1 NOT NULL,
    `password_hash` VARCHAR(120) NOT NULL
);

CREATE TABLE profiles (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `user_id` INTEGER UNIQUE NOT NULL,
    `registration_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `bio` TEXT,
    `profile_picture_url` VARCHAR(255),
    `website_url` VARCHAR(255),
    `location` VARCHAR(100),
    FOREIGN KEY (`user_id`) REFERENCES users(`id`)
);