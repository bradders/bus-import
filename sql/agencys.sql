CREATE TABLE `agencys` (
	id INT(11) PRIMARY KEY AUTO_INCREMENT,
    agency_id VARCHAR(11), 
    agency_name VARCHAR(255),
    agency_url VARCHAR(255),
    agency_timezone VARCHAR(50), 
	agency_lang VARCHAR(255), 
	created datetime,
	updated datetime
);