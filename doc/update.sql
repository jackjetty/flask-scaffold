CREATE DATABASE IF NOT EXISTS demo  DEFAULT CHARACTER SET utf8mb4  DEFAULT COLLATE utf8mb4_general_ci;


CREATE TABLE `user` (
  `id` bigint NOT NULL,
  `account` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `password` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `state` smallint DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  `name` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;


INSERT INTO demo.`user` (id,account,password,state,create_time,update_time,name) VALUES 
(1640596342009110528,'admin','$2b$12$oQpyQsuTJ8YJl6t5ULvS2ehptAyiJfeGkqpcJqjEP41vsAk69Yz5G',1,'2023-03-28 14:07:04.000',NULL,'管理员')
;