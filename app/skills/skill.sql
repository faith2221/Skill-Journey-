DROP TABLE IF EXISTS `skills`;
DROP TABLE IF EXISTS `user_skills`;
DROP TABLE IF EXISTS `posts`;
DROP TABLE IF EXISTS `post_skills`;
DROP TABLE IF EXISTS `comments`;
DROP TABLE IF EXISTS `achievements`;

CREATE TABLE skills (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `user_id` INTEGER,
    `skill_name` VARCHAR(100) UNIQUE NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`)
);

CREATE TABLE resources (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `title` VARCHAR(255) NOT NULL,
    `skill_id` INEGER NOT NULL,
    FOREIGN KEY (`skill_id`) REFERENCES users(`id`)
);

CREATE TABLE resource_links (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `resource_id` INTEGER NOT NULL,
    `url` VARCHAR(255) NOT NULL,
    FOREIGN KEY (`resource_id`) REFERENCES resources(`id`)
);

-- Insert Resource Titles
INSERT INTO resources (title, skill_id) VALUES
('Python', 1),
('Javascript', 2),
('HTML/CSS', 3),
('Java', 4),
('C/C++', 5),
('SQL', 6),
('Ruby', 7),
('Graphic Design', 8),
('Photography', 9),
('Writing', 10),
('Music Production', 11),
('Storytelling', 12),
('Craftsmanship', 13),
('Cooking', 14),
('Time Management', 15),
('Workouts', 16),
('Traveling', 17),
('Self-Care', 18),
('Communication', 19),
('Yoga', 20),
('Networking', 21),
('Resume Writing', 22),
('Public Speaking', 23),
('Leadership', 24),
('Problem Solving', 24),
('Interview Skills', 26);

-- Insert resource links
INSERT INTO skills (skill_name) VALUES


CREATE TABLE posts (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `title` VARCHAR(255) NOT NULL,
    `image` VARCHAR(255) NOT NULL,
    `body` TEXT NOT NULL,
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `publish` DATE NULL,
    `user_id` INTEGER NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`)
);

CREATE TABLE post_skills (
    `post_id` INTEGER,
    `skill_id` INTEGER,
    PRIMARY KEY (`post_id`, `skill_id`),
    FOREIGN KEY (`post_id`) REFERENCES posts (`id`),
    FOREIGN KEY  (`skill_id`) REFERENCES skills (`id`)
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