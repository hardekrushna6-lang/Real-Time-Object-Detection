CREATE DATABASE IF NOT EXISTS object_detection;

USE object_detection;

CREATE TABLE IF NOT EXISTS detections (
    id INT AUTO_INCREMENT PRIMARY KEY,
    object_name VARCHAR(100) NOT NULL,
    confidence DECIMAL(6,4) NOT NULL,
    detected_at DATETIME NOT NULL
);
