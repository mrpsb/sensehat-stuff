CREATE DATABASE `sensehat`;

CREATE TABLE `sensehat`.`readings` (
  `readDateTime` DATETIME NOT NULL COMMENT 'Date and time reading was taken',
  `humidity` FLOAT NULL COMMENT '%rH from Humidity sensor',
  `tempHumidity` FLOAT NULL COMMENT 'Temperature in C from Humidity Sensor',
  `tempPressure` FLOAT NULL COMMENT 'Temperature in C from Pressure sensor',
  `pressure` FLOAT NULL COMMENT 'Pressure in mb from pressure sensor',
  PRIMARY KEY (`readDateTime`)  COMMENT '',
  UNIQUE INDEX `readDateTime_UNIQUE` (`readDateTime` ASC)  COMMENT '');
