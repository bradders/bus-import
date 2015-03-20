CREATE TABLE `routes` (
	id INT(11) PRIMARY KEY AUTO_INCREMENT,
    route_id varchar(255),
	area_id INT(11),
	route_short_name VARCHAR(50),
	route_long_name VARCHAR(255),
	route_type INT(2),
	route_text_color VARCHAR(255),
	route_color VARCHAR(255),
	route_desc VARCHAR(255), 
	created datetime,
	updated datetime,
	KEY `route_id` (route_id),
	KEY `route_type` (route_type), 
	KEY `area_id` (area_id)
);