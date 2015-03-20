CREATE TABLE `stop_times` (
	id INT(11) PRIMARY KEY AUTO_INCREMENT,
    trip_id INT(11),
	area_id INT(11),
	arrival_time TIME,
	departure_time TIME,
	stop_id INT(11),
	stop_sequence INT(11),
	pickup_type INT(2),
	drop_off_type INT(2),
	created datetime,
	updated datetime,
	KEY `trip_id` (trip_id),
	KEY `area_id` (area_id),
	KEY `stop_id` (stop_id),
	KEY `stop_sequence` (stop_sequence),
	KEY `pickup_type` (pickup_type),
	KEY `drop_off_type` (drop_off_type)
);