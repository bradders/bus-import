CREATE TABLE `trips` (
	id INT(11) PRIMARY KEY AUTO_INCREMENT,
    route_id VARCHAR(255),
	service_id VARCHAR(255),
	area_id INT(11),
	trip_id INT(11),
	trip_headsign VARCHAR(255),
	block_id INT(11),
	created datetime,
	updated datetime,
	KEY `trip_id` (route_id),
	KEY `route_id` (route_id),
	KEY `service_id` (service_id),
	KEY `area_id` (area_id),
	KEY `block_id` (block_id)
);