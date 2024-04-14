DROP TABLE IF EXISTS `media`;
DROP TABLE IF EXISTS `posts`;
DROP TABLE IF EXISTS `comments`;

CREATE TABLE media (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `type` TEXT NOT NULL,
    `link` TEXT NOT NULL
);

-- Insert resource links
INSERT INTO media (type, link) VALUES
('video', 'https://www.youtube.com/playlist?list=PLBlnK6fEyqRiueC_HzwFallNO76hfXBB7'),
('book', 'https://cfm.ehu.es/ricardo/docs/python/Learning_Python.pdf'),
('video', 'https://www.youtube.com/playlist?list=PLIrsP8dft12CSv-KEbiXq21JmR3LUr854'),
('video', 'https://www.youtube.com/playlist?list=PLBlnK6fEyqRggZZgYpPMUxdY1CYkZtARR'),
('book', 'https://dl.hellodigi.ir/dl.hellodigi.ir/dl/book/Sams%20Teach%20Yourself%20C%2B%2B%20in%2024%20Hours.pdf'),
('video', 'https://www.youtube.com/watch?v=s0g4ty29Xgg&list=PLBlnK6fEyqRh6isJ01MBnbNpV3ZsktSyS'),
('book', 'https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics'),
('video', 'https://www.youtube.com/watch?v=dD2EISBDjWM&list=PLr6-GrHUlVf_ZNmuQSXdS197Oyr1L9sPB'),
('book', 'https://www.cs.cmu.edu/afs/cs.cmu.edu/user/gchen/www/download/java/LearnJava.pdf');


CREATE TABLE posts (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `title` VARCHAR(255) NOT NULL,
    `content` TEXT NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `publish` DATE default CURRENT_TIMESTAMP,
    `url` VARCHAR(255),
    `user_id` INTEGER NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`)
);

CREATE TABLE comments (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `content` TEXT NOT NULL,
    `url` VARCHAR(255),
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `user_id` INTEGER NOT NULL,
    `post_id` INTEGER NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users (`id`),
    FOREIGN KEY (`post_id`) REFERENCES posts (`id`)  
);