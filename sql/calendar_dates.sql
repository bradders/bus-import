CREATE TABLE `calendar_dates` (
	id INT(11) PRIMARY KEY AUTO_INCREMENT,
    service_id varchar(255),
    `date` VARCHAR(8),
    date_timestamp INT(11),
    exception_type INT(2), 
	created datetime,
	updated datetime,
    KEY `service_id` (service_id),
    KEY `date_timestamp` (date_timestamp),
    KEY `exception_type` (exception_type)    
);