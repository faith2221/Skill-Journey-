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

INSERT INTO skills (skill_name) VALUES
('Python'),
('Javascript'),
('HTML/CSS'),
('Java'),
('C/C++'),
('SQL'),
('Ruby'),
('Graphic Design'),
('Photography'),
('Writing'),
('Music Production'),
('Storytelling'),
('Craftsmanship'),
('Cooking'),
('Time Management'),
('Workouts'),
('Traveling'),
('Self-Care'),
('Communication'),
('Yoga'),
('Networking'),
('Resume Writing'),
('Public Speaking'),
('Leadership'),
('Problem Solving'),
('Interview Skills');

CREATE TABLE user_skills (
    `user_id` INTEGER,
    `skill_id` INTEGER,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`),
    FOREIGN KEY (`skill_id`) REFERENCES skills(`id`),
    PRIMARY KEY (`user_id`, `skill_id`)
);

CREATE TABLE IF NOT EXISTS user_selected_skills (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `user_id` INTEGER NOT NULL,
    `skill_id` INTEGER NOT NULL,
    `selected_date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
     FOREIGN KEY (`user_id`) REFERENCES users(`id`),
     FOREIGN KEY (`skill_id`) REFERENCES skills(`id`) 
);

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