DROP TABLE IF EXISTS `media`;
DROP TABLE IF EXISTS `comments`;

CREATE TABLE media (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `title` TEXT NOT NULL,
    `url` TEXT NOT NULL
);

-- Insert resource links
INSERT INTO media (title, url) VALUES
('Python', 'https://www.youtube.com/playlist?list=PLBlnK6fEyqRiueC_HzwFallNO76hfXBB7'),
('Python', 'https://cfm.ehu.es/ricardo/docs/python/Learning_Python.pdf'),
('Python', 'https://www.youtube.com/playlist?list=PLIrsP8dft12CSv-KEbiXq21JmR3LUr854'),
('C/C++', 'https://www.youtube.com/playlist?list=PLBlnK6fEyqRggZZgYpPMUxdY1CYkZtARR'),
('C/C++', 'https://dl.hellodigi.ir/dl.hellodigi.ir/dl/book/Sams%20Teach%20Yourself%20C%2B%2B%20in%2024%20Hours.pdf'),
('C/C++', 'https://www.youtube.com/watch?v=s0g4ty29Xgg&list=PLBlnK6fEyqRh6isJ01MBnbNpV3ZsktSyS'),
('Javascript', 'https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics'),
('Javascript', 'https://www.youtube.com/watch?v=dD2EISBDjWM&list=PLr6-GrHUlVf_ZNmuQSXdS197Oyr1L9sPB'),
('HTML/CSS', 'https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics'),
('HTML/CSS', 'https://www.cs.cmu.edu/afs/cs.cmu.edu/user/gchen/www/download/java/LearnJava.pdf'),
('HTML/CSS', 'https://www.youtube.com/watch?v=r59xYe3Vyks&list=PLS1QulWo1RIbfTjQvTdj8Y6yyq4R7g-Al'),
('Java', 'https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics'),
('Java', 'https://www.youtube.com/playlist?list=PLoC8Q0moRTSg1exJDE3-PhbAgC_Gk8OPQ'),
('SQL', 'https://www.youtube.com/playlist?list=PLsjUcU8CQXGFFAhJI6qTA8owv3z9jBbpd'),
('SQL', 'https://www.cs.cmu.edu/afs/cs.cmu.edu/user/gchen/www/download/java/LearnJava.pdf'),
('Ruby', 'https://www.youtube.com/watch?v=CIe1DxrSrhs&list=PLLAZ4kZ9dFpO90iMas70Tt4_wYjhLGkya'),
('Ruby', 'https://jmvidal.cse.sc.edu/library/thomas05a.pdf'),
('Graphic Design', 'https://www.youtube.com/watch?v=WONZVnlam6U&list=PLYfCBK8IplO4E2sXtdKMVpKJZRBEoMvpn'),
('Graphic Design', 'https://www.rcboe.org/cms/lib/GA01903614/Centricity/Domain/7052/Intro%20to%20graphic%20design.pdf'),
('Photography', 'https://soar.suny.edu/bitstream/handle/20.500.12648/7566/Intro%20To%20Digital%20Photography.pdf?sequence=1&isAllowed=y'),
('Photography', 'https://www.youtube.com/watch?v=NpUzGNe42Cg&list=PLBBCCB798B85DA47B'),
('Writing', 'https://www.youtube.com/watch?v=QXnsw4cn5wo&list=PLeVxAnFsasIqIc8b03kHA3tw-xfIwgO2M'),
('Writing', 'https://www.youtube.com/watch?v=pFbFEseC_Ow&pp=ygUpaW50cm9kdWN0aW9uIHRvIHdyaXRpbmcgIGFuZCBwb2V0cnlwb2V0cnk%3D'),
('Writing', 'https://www.youtube.com/watch?v=aG9el6hOjm8&list=PLh9mgdi4rNewA25FVJ-lawQ-yr-alF58z'),
('Writing', 'https://www.youtube.com/watch?v=QXnsw4cn5wo&list=PLeVxAnFsasIqIc8b03kHA3tw-xfIwgO2M'),
('Music Production', 'https://www.youtube.com/watch?v=damoEmoUquQ&list=PLzq2RsjgsUG6zWc1K2M9zrSQ2e8YxewOF'),
('Music Production', 'https://www.youtube.com/watch?v=BUjdnxgBgzM&pp=ygUtaW50cm9kdWN0aW9uIHRvIG1hc3RlcnkgIG9mICBtdXNpYyBwcm9kdWN0aW9u'),
('Storytelling', 'https://www.youtube.com/watch?v=Gvu4kdSBUz8&list=PLC91qyoSyKZVRsNL-jUKPvP5ZuWOxp76T'),
('Storytelling', 'https://www.youtube.com/watch?v=_7W3aAz21qk&pp=ygUpaW50cm9kdWN0aW9uIHRvIG1hc3RlcnkgIG9mICBzdG9yeXRlbGxpbmc%3D'),
('Craftmanship', 'https://www.youtube.com/watch?v=pA02XKvxa_o&list=PLwm6LvGc5xq34B3cxlbHPFFcwegOH0-Q4'),
('Craftmanship', 'https://www.youtube.com/@ElectricianU'),
('Time Management', 'https://www.youtube.com/watch?v=WXBA4eWskrc&pp=ygUadGltZSBtYW5hZ2VtZW50IG1vdGl2YXRpb24%3D'),
('Time Management', 'https://www.youtube.com/watch?v=FrIW53z1CtE&pp=ygUadGltZSBtYW5hZ2VtZW50IG1vdGl2YXRpb24%3D'),
('Time Management', 'https://www.youtube.com/watch?v=iDbdXTMnOmE&pp=ygUadGltZSBtYW5hZ2VtZW50IG1vdGl2YXRpb24%3D'),
('Workout Routines', 'https://www.youtube.com/@fit7eleven/videos?view=0&sort=dd&shelf_id=0'),
('Workout Routines', 'https://www.youtube.com/@ChloeTing'),
('Workout Routines', 'https://www.youtube.com/@BullyJuice'),
('Self-Care', 'https://www.youtube.com/watch?v=Eupk56SG76M&pp=ygUUc2VsZiBjYXJlIG1vdGl2YXRpb24%3D'),
('Self-Care', 'https://www.youtube.com/watch?v=CyVYnYKzjyg&pp=ygUUc2VsZiBjYXJlIG1vdGl2YXRpb24%3D'),
('Communication', 'https://www.youtube.com/watch?v=W-4IcNJIyM8&list=PLm_MSClsnwm-AIEbpyIxoTT8t7UzkHSYC'),
('Communication', 'https://www.youtube.com/watch?v=srn5jgr9TZo&list=PLOaeOd121eBEEWP14TYgSnFsvaTIjPD22'),
('Yoga Routines', 'https://www.youtube.com/@yogawithadriene#'),
('Yoga Routines', 'https://www.youtube.com/@MadFit'),
('Networking Skills', 'https://www.youtube.com/watch?v=-30m8D6gTrg&pp=ygUKTmV0d29ya2luZw%3D%3D'),
('Networking Skills', 'https://www.youtube.com/watch?v=jyoFvSPFDIo&list=PLCcteVWYyBtteZ69xEH2HG-hwK5ZuNvHc'),
('Resume Writing', 'https://www.youtube.com/watch?v=Tt08KmFfIYQ&pp=ygUOUmVzdW1lIFdyaXRpbmc%3D'),
('Resume Writing', 'https://www.youtube.com/watch?v=M5bASAr8Jg0&pp=ygUKTmV0d29ya2luZw%3D%3D'),
('Public Speaking', 'https://www.youtube.com/watch?v=xSp78RwcAS4&pp=ygUWcHVibGljIHNwZWFraW5nIHNraWxscw%3D%3D'),
('Public Speaking', 'https://www.youtube.com/watch?v=962eYqe--Yc&pp=ygUWcHVibGljIHNwZWFraW5nIHNraWxscw%3D%3D'),
('Leadership Skills', 'https://www.youtube.com/watch?v=eXDNkwIeOqA&pp=ygURbGVhZGVyc2hpcCBza2lsbHM%3D'),
('Leadership Skills', 'https://www.youtube.com/watch?v=vlpKyLklDDY&pp=ygURbGVhZGVyc2hpcCBza2lsbHM%3D'),
('Interview Skills', 'https://www.youtube.com/watch?v=sYV37t8vDgQ&pp=ygUQSW50ZXJ2aWV3IHNraWxscw%3D%3D'),
('Interview Skills', 'https://www.youtube.com/watch?v=GzYDwIFtxII&pp=ygUQSW50ZXJ2aWV3IHNraWxscw%3D%3D');

CREATE TABLE comments (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `content` TEXT NOT NULL,
    `url` VARCHAR(255),
    `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `user_id` INTEGER NOT NULL,
    `parent_comment_id` INTEGER,
    FOREIGN KEY (`user_id`) REFERENCES users (`id`)
);