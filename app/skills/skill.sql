DROP TABLE IF EXISTS `skills`;
DROP TABLE IF EXISTS `achievements`;
DROP TABLE IF EXISTS `badges`;
DROP TABLE IF EXISTS `tags`;
DROP TABLE IF EXISTS `posts`;
DROP TABLE IF EXISTS `tagged_items`;
DROP TABLE IF EXISTS `comments`;

CREATE TABLE skills (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(100) UNIQUE NOT NULL,
    `description` TEXT NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE achievements (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `skill_id` INTEGER NOT NULL,
    `user_id` INTEGER NOT NULL,
    `achievement_id` INTEGER NOT NULL,
    `achievement_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`skill_id`) REFERENCES skills(`id`),
    FOREIGN KEY (`user_id`) REFERENCES users(`id`),
    FOREIGN KEY (`achievement_id`) REFERENCES achievements(`id`)
);

CREATE TABLE badges (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `description` TEXT NOT NULL,
    `image_url` VARCHAR(255),
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE tags (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE posts (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `title` VARCHAR(255) NOT NULL,
    `image` VARCHAR(255) NOT NULL,
    `slug` VARCHAR(50) UNIQUE NOT NULL,
    `body` TEXT NOT NULL,
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `publish` DATE NULL,
    `user_id` INTEGER NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`)
);

CREATE TABLE tagged_items (
    `post_id` INTEGER NOT NULL,
    `tag_id` INTEGER NOT NULL,
    FOREIGN KEY (`post_id`) REFERENCES posts (`id`),
    FOREIGN KEY (`tag_id`) REFERENCES tags (`id`)
);

CREATE TABLE comments (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `body` TEXT NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `user_id` INTEGER NOT NULL,
    `post_id` INTEGER NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users (`id`),
    FOREIGN KEY (`post_id`) REFERENCES posts (`id`)  
);