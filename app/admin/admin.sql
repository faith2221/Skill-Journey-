DROP TABLE IF EXISTS `backups`;

CREATE TABLE backups(
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `backup_name` TEXT NOT NULL,
    `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `status` TEXT NOT NULL
);