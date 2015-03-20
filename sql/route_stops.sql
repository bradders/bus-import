CREATE TABLE `route_stops` (
	id INT(11) PRIMARY KEY AUTO_INCREMENT,
    route_id VARCHAR(255),
    stop_id INT(11), 
	created datetime,
	updated datetime
);