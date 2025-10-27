CREATE DATABASE BigBasket;
USE BigBasket;

-- GSINT required state codes
CREATE TABLE indian_state_codes
(
    state_code TINYINT(2) UNSIGNED PRIMARY KEY,
    state VARCHAR(40) UNIQUE NOT NULL
);
INSERT INTO indian_state_codes VALUES
    (01, 'JAMMU AND KASHMIR'),
    (02, 'HIMACHAL PRADESH'),
    (03, 'PUNJAB'),
    (04, 'CHANDIGARH'),
    (05, 'UTTARAKHAND'),
    (06, 'HARYANA'),
    (07, 'DELHI'),
    (08, 'RAJASTHAN'),
    (09, 'UTTAR PRADESH'),
    (10, 'BIHAR'),
    (11, 'SIKKIM'),
    (12, 'ARUNACHAL PRADESH'),
    (13, 'NAGALAND'),
    (14, 'MANIPUR'),
    (15, 'MIZORAM'),
    (16, 'TRIPURA'),
    (17, 'MEGHALAYA'),
    (18, 'ASSAM'),
    (19, 'WEST BENGAL'),
    (20, 'JHARKHAND'),
    (21, 'ODISHA'),
    (22, 'CHHATTISGARH'),
    (23, 'MADHYA PRADESH'),
    (24, 'GUJARAT'),
    (25, 'DAMAN AND DIU'),
    (26, 'DADRA AND NAGAR HAVELI'),
    (27, 'MAHARASHTRA'),
    (28, 'ANDHRA PRADESH (OLD)'),
    (29, 'KARNATAKA'),
    (30, 'GOA'),
    (31, 'LAKSHADEEP'),
    (32, 'KERALA'),
    (33, 'TAMIL NADU'),
    (34, 'PUDUCHERRY'),
    (35, 'ANDAMAN AND NICOBAR ISLANDS'),
    (36, 'TELANGANA'),
    (37, 'ANDHRA PRADESH (NEW)')
;

CREATE TABLE customer_information
(
    customer_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY ,
    customer_name VARCHAR(80) NOT NULL,

    customer_email VARCHAR(100) NOT NULL UNIQUE,
    customer_mobile_number BIGINT UNSIGNED NOT NULL UNIQUE
        CHECK (customer_mobile_number BETWEEN 6000000000 and 9999999999),
    customer_address VARCHAR(255) DEFAULT NULL,
    password_hash VARCHAR(128) NOT NULL,
    signup_date DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE transactions_table
(
    transaction_id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY ,
    customer_id BIGINT UNSIGNED NOT NULl,

    transaction_mode ENUM('ONLINE', 'OFFLINE') DEFAULT 'OFFLINE' NOT NULL,
    payment_mode ENUM('CREDIT', 'DEBIT', 'UPI', 'CASH') DEFAULT 'CASH' NOT NULl,
    delivery_status ENUM('Y', 'N') DEFAULT 'N' NOT NULL,
    transaction_city TINYINT UNSIGNED NOT NULL
        CHECK (transaction_city BETWEEN 1 AND 37),

    order_amount DECIMAL(10,2) NOT NULL
        CHECK (order_amount > 0),
    order_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (customer_id) REFERENCES customer_information(customer_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (transaction_city) REFERENCES indian_state_codes(state_code)
);
