DROP TABLE IF EXISTS `skills`;
DROP TABLE IF EXISTS `user_skills`;
DROP TABLE IF EXISTS `posts`;
DROP TABLE IF EXISTS `post_skills`;
DROP TABLE IF EXISTS `comments`;
DROP TABLE IF EXISTS `achievements`;

CREATE TABLE skills (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` VARCHAR(100) UNIQUE NOT NULL,
    `description` TEXT NOT NULL,
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO skills (name, description) VALUES
('Programming: Python', 'Beginner-friendly programming language; start with basic syntax and gradually advance to building applications and automation scripts'), 
('Programming: Javascript', 'Entry-level web development language; begin with DOM(Document Object Model) manipulation and progress to creating interactive websites and web applications'), 
('Programming: HTML/CSS', 'Fundamentals of web development; learn to structure web pages with HTML and style them with CSS'),
('Programming: Java', 'Introduction to object-oriented programming; learn the basics of Java and work towards developing simple desktop and mobile applications'), 
('Programming: C/C++', 'Core concepts of computer science; start with understanding data types and control structures, then move on to developing small-scale software projects'), 
('Programming: SQL', 'Introduction to database management; learn to write and execute SQL queries to retrieve, manipulate, and manage data'),
('Creative: Graphic Design', 'Introduction to visual communication; explore design principles, typography, and layout to create visually appealing graphics'), 
('Creative: Photography', 'Beginners guide to photography; learn about composition, lighting, and camera settings to capture memorable images.'), 
('Creative: Writing', 'Introduction to creative writing; explore different genres and styles of writing to express your thoughts and ideas'),
('Creative: Music Production', 'Introduction to music creation; learn to compose, record, and produce music using digital audio workstations (DAW)software'),
('Creative: Storytelling', 'Fundamentals of storytelling; develop narrative skills and learn techniques to engage and captivate audiences '),
('Creative: Craftsmanship', 'Introduction to DIY crafts; explore various crafting techniques and materials to create handmade projects'),
('Lifestyle: Cooking', 'Beginner-friendly cooking skills; start with basic recipes and techniques, gradually expanding to explore different cuisines and cooking methods'), 
('Lifestyle: Time Management', 'Introduction to time management principles; learn strategies for prioritizing tasks, setting goals, and managing distractions'),
('Lifestyle: Gardening', 'Beginner guide to gardening; learn about plant care, garden design, and managing distractions'), 
('Lifestyle: Workouts', 'Introduction to fitness; start with basic exercises and routines, gradually increasing intensity and variety as fitness improves'),
('Lifestyle: Traveling', 'Beginner guide to travel planning; learn about destination research, budgeting, and travel safety'),
('Lifestyle: Self-Care', 'Introduction to self care practices; explore mindfulness, stress management, and self-compassion techniques for improved well-being'),
('Lifestyle: Communication', 'Introduction to effective communication;learn to express ideas clearly, listen actively, and build reports with others'), 
('Lifestyle: Yoga', 'Beginner-friendly yoga practice; start with basic poses and breathing exercises, gradually progressing to more advanced sequences and meditation') ,
('Career: Networking', 'Introduction to professional networking; learn strategies for building and nurturing professional relationships for career advancement'),
('Career: Resume Writing', 'Beginner guide to crafting resumes; learn to highlight skills, experiences, and achievements effectively to stand out to employers'),
('Career: Public Speaking', 'Introduction to public speaking skills; learn techniques for overcoming stage fright, organizing presentations, and engaging audiences'),
('Career: Leadership', 'Introduction to leadership principles; learn to inspire and motivate others, communicate vision, and lead by example'),
('Career: Problem Solving', 'Introduction to problem-solving skills; learn to analyze issues, brainstorm solutions, and implement effective problem-solving strategies'),
('Career: Professional Development', 'Introduction to lifelong learning and growth; explore opportunities for skill development, career advancement, and personal growth'),
('Career: Interview Skills', ' Introduction to job interview preparation; learn techniques for researching companies, answering common interview questions, and showcasing skills and experiences');

CREATE TABLE user_skills (
    `user_id` INTEGER,
    `skill_id` INTEGER,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`),
    FOREIGN KEY (`skill_id`) REFERENCES skills(`id`),
    PRIMARY KEY (`user_id`, `skill_id`)
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