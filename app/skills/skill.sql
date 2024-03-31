DROP TABLE IF EXISTS `skills`;
DROP TABLE IF EXISTS `resources`;
DROP TABLE IF EXISTS `resource_links`;
DROP TABLE IF EXISTS `posts`;
DROP TABLE IF EXISTS `comments`;


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
    `skill_id` INTEGER NOT NULL,
    FOREIGN KEY (`skill_id`) REFERENCES skills(`id`)
);

CREATE TABLE resource_links (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `resource_id` INTEGER NOT NULL,
    `url` VARCHAR(255) NOT NULL,
    FOREIGN KEY (`resource_id`) REFERENCES resources(`id`)
);

-- Insert Resource Titles
INSERT INTO resources (title, skill_id) VALUES
('Programming', 1),
('Programming', 2),
('Web Development', 3),
('Programming', 4),
('Web Development', 5),
('Database Management', 6),
('Programming', 7),
('Design', 8),
('Photography', 9),
('Writing', 10),
('Music Production', 11),
('Writing', 12),
('Craftsmanship', 13),
('Personal Development', 14),
('Fitness', 15),
('Self-Care', 16),
('Communication', 17),
('Yoga', 18),
('Networking', 19),
('Job Skills', 20),
('Public Speaking', 21),
('Leadership', 22),
('Interview Skills', 23);

-- Insert resource links
INSERT INTO resource_links (resource_id, url) VALUES
(1, 'https://www.youtube.com/playlist?list=PLBlnK6fEyqRiueC_HzwFallNO76hfXBB7'),
(1, 'https://cfm.ehu.es/ricardo/docs/python/Learning_Python.pdf'),
(1, 'https://www.youtube.com/playlist?list=PLIrsP8dft12CSv-KEbiXq21JmR3LUr854'),
(2, 'https://www.youtube.com/playlist?list=PLBlnK6fEyqRggZZgYpPMUxdY1CYkZtARR'),
(2, 'https://dl.hellodigi.ir/dl.hellodigi.ir/dl/book/Sams%20Teach%20Yourself%20C%2B%2B%20in%2024%20Hours.pdf'),
(2, 'https://www.youtube.com/watch?v=s0g4ty29Xgg&list=PLBlnK6fEyqRh6isJ01MBnbNpV3ZsktSyS'),
(3, 'https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics'),
(3, 'https://www.youtube.com/watch?v=dD2EISBDjWM&list=PLr6-GrHUlVf_ZNmuQSXdS197Oyr1L9sPB'),
(3, 'https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics'),
(4, 'https://www.cs.cmu.edu/afs/cs.cmu.edu/user/gchen/www/download/java/LearnJava.pdf'),
(4, 'https://www.youtube.com/watch?v=r59xYe3Vyks&list=PLS1QulWo1RIbfTjQvTdj8Y6yyq4R7g-Al'),
(5, 'https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics'),
(5, 'https://www.youtube.com/playlist?list=PLoC8Q0moRTSg1exJDE3-PhbAgC_Gk8OPQ'),
(6, 'https://www.youtube.com/playlist?list=PLsjUcU8CQXGFFAhJI6qTA8owv3z9jBbpd'),
(6, 'https://www.cs.cmu.edu/afs/cs.cmu.edu/user/gchen/www/download/java/LearnJava.pdf'),
(7, 'https://www.youtube.com/watch?v=CIe1DxrSrhs&list=PLLAZ4kZ9dFpO90iMas70Tt4_wYjhLGkya'),
(7, 'https://jmvidal.cse.sc.edu/library/thomas05a.pdf'),
(8, 'https://www.youtube.com/watch?v=WONZVnlam6U&list=PLYfCBK8IplO4E2sXtdKMVpKJZRBEoMvpn'),
(8, 'https://www.rcboe.org/cms/lib/GA01903614/Centricity/Domain/7052/Intro%20to%20graphic%20design.pdf'),
(9, 'https://soar.suny.edu/bitstream/handle/20.500.12648/7566/Intro%20To%20Digital%20Photography.pdf?sequence=1&isAllowed=y'),
(9, 'https://www.youtube.com/watch?v=NpUzGNe42Cg&list=PLBBCCB798B85DA47B'),
(10, 'https://www.youtube.com/watch?v=QXnsw4cn5wo&list=PLeVxAnFsasIqIc8b03kHA3tw-xfIwgO2M'),
(10, 'https://www.youtube.com/watch?v=pFbFEseC_Ow&pp=ygUpaW50cm9kdWN0aW9uIHRvIHdyaXRpbmcgIGFuZCBwb2V0cnlwb2V0cnk%3D'),
(10, 'https://www.youtube.com/watch?v=aG9el6hOjm8&list=PLh9mgdi4rNewA25FVJ-lawQ-yr-alF58z'),
(10, 'https://www.youtube.com/watch?v=QXnsw4cn5wo&list=PLeVxAnFsasIqIc8b03kHA3tw-xfIwgO2M'),
(11, 'https://www.youtube.com/watch?v=damoEmoUquQ&list=PLzq2RsjgsUG6zWc1K2M9zrSQ2e8YxewOF'),
(11, 'https://www.youtube.com/watch?v=BUjdnxgBgzM&pp=ygUtaW50cm9kdWN0aW9uIHRvIG1hc3RlcnkgIG9mICBtdXNpYyBwcm9kdWN0aW9u'),
(12, 'https://www.youtube.com/watch?v=Gvu4kdSBUz8&list=PLC91qyoSyKZVRsNL-jUKPvP5ZuWOxp76T'),
(12, 'https://www.youtube.com/watch?v=_7W3aAz21qk&pp=ygUpaW50cm9kdWN0aW9uIHRvIG1hc3RlcnkgIG9mICBzdG9yeXRlbGxpbmc%3D'),
(13, 'https://www.youtube.com/watch?v=pA02XKvxa_o&list=PLwm6LvGc5xq34B3cxlbHPFFcwegOH0-Q4'),
(13, 'https://www.youtube.com/@ElectricianU'),
(14, 'https://www.youtube.com/watch?v=WXBA4eWskrc&pp=ygUadGltZSBtYW5hZ2VtZW50IG1vdGl2YXRpb24%3D'),
(14, 'https://www.youtube.com/watch?v=FrIW53z1CtE&pp=ygUadGltZSBtYW5hZ2VtZW50IG1vdGl2YXRpb24%3D'),
(14, 'https://www.youtube.com/watch?v=iDbdXTMnOmE&pp=ygUadGltZSBtYW5hZ2VtZW50IG1vdGl2YXRpb24%3D'),
(15, 'https://www.youtube.com/@fit7eleven/videos?view=0&sort=dd&shelf_id=0'),
(15, 'https://www.youtube.com/@ChloeTing'),
(15, 'https://www.youtube.com/@BullyJuice'),
(16, 'https://www.youtube.com/watch?v=Eupk56SG76M&pp=ygUUc2VsZiBjYXJlIG1vdGl2YXRpb24%3D'),
(16, 'https://www.youtube.com/watch?v=CyVYnYKzjyg&pp=ygUUc2VsZiBjYXJlIG1vdGl2YXRpb24%3D'),
(17, 'https://www.youtube.com/watch?v=W-4IcNJIyM8&list=PLm_MSClsnwm-AIEbpyIxoTT8t7UzkHSYC'),
(17, 'https://www.youtube.com/watch?v=srn5jgr9TZo&list=PLOaeOd121eBEEWP14TYgSnFsvaTIjPD22'),
(18, 'https://www.youtube.com/@yogawithadriene#'),
(18, 'https://www.youtube.com/@MadFit'),
(19, 'https://www.youtube.com/watch?v=-30m8D6gTrg&pp=ygUKTmV0d29ya2luZw%3D%3D'),
(19, 'https://www.youtube.com/watch?v=jyoFvSPFDIo&list=PLCcteVWYyBtteZ69xEH2HG-hwK5ZuNvHc'),
(20, 'https://www.youtube.com/watch?v=Tt08KmFfIYQ&pp=ygUOUmVzdW1lIFdyaXRpbmc%3D'),
(20, 'https://www.youtube.com/watch?v=M5bASAr8Jg0&pp=ygUKTmV0d29ya2luZw%3D%3D'),
(21, 'https://www.youtube.com/watch?v=xSp78RwcAS4&pp=ygUWcHVibGljIHNwZWFraW5nIHNraWxscw%3D%3D'),
(21, 'https://www.youtube.com/watch?v=962eYqe--Yc&pp=ygUWcHVibGljIHNwZWFraW5nIHNraWxscw%3D%3D'),
(22, 'https://www.youtube.com/watch?v=eXDNkwIeOqA&pp=ygURbGVhZGVyc2hpcCBza2lsbHM%3D'),
(22, 'https://www.youtube.com/watch?v=vlpKyLklDDY&pp=ygURbGVhZGVyc2hpcCBza2lsbHM%3D'),
(23, 'https://www.youtube.com/watch?v=sYV37t8vDgQ&pp=ygUQSW50ZXJ2aWV3IHNraWxscw%3D%3D'),
(23, 'https://www.youtube.com/watch?v=GzYDwIFtxII&pp=ygUQSW50ZXJ2aWV3IHNraWxscw%3D%3D');

CREATE TABLE posts (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `title` VARCHAR(255) NOT NULL,
    `image` VARCHAR(255) NOT NULL,
    `body` TEXT NOT NULL,
    `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `publish` DATE NULL,
    `url` VARCHAR(255),
    `user_id` INTEGER NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users(`id`)
);
CREATE TABLE comments (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `body` TEXT NOT NULL,
    `url` VARCHAR(255),
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `user_id` INTEGER NOT NULL,
    `post_id` INTEGER NOT NULL,
    FOREIGN KEY (`user_id`) REFERENCES users (`id`),
    FOREIGN KEY (`post_id`) REFERENCES posts (`id`)  
);