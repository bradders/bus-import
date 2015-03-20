CREATE TABLE `route_colors` (
	id INT(11) PRIMARY KEY AUTO_INCREMENT,
    route_id VARCHAR(255),
    route_color VARCHAR(255), 
	created datetime,
	updated datetime
);

LOCK TABLES `route_colors` WRITE;
/*!40000 ALTER TABLE `route_colors` DISABLE KEYS */;

INSERT INTO `route_colors` (`id`, `route_id`, `route_color`, `created`, `updated`)
VALUES
	(1,'1-Whistler','f7931d',NULL,NULL),
	(2,'2-Whistler','004b8d',NULL,NULL),
	(3,'3-Whistler','8ec640',NULL,NULL),
	(4,'4-Whistler','50701A',NULL,NULL), 
	(5,'5-Whistler','8d143a',NULL,NULL),
	(6,'6-Whistler','fec20f',NULL,NULL),
	(7,'7-Whistler','b2a97e',NULL,NULL),
	(8,'8-Whistler','77AD98',NULL,NULL),
	(9,'99-Whistler','5C86BE',NULL,NULL),
	(10,'100-Whistler','34B233',NULL,NULL);

/*!40000 ALTER TABLE `route_colors` ENABLE KEYS */;
UNLOCK TABLES;
