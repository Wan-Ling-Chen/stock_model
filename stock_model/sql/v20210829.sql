CREATE TABLE `stock_daily_prices`(
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `symbol` VARCHAR(20) NOT NULL,
    `price_date` DATETIME NOT NULL,
    `open_price` DECIMAL(11,6) NULL,
    `high_price` DECIMAL(11,6) NULL,
    `low_price` DECIMAL(11,6) NULL,
    `close_price` DECIMAL(11,6) NULL,
    `adj_close_price` DECIMAL(11,6) NULL,
    `volume` BIGINT(20) NULL,
    `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
    `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP(),
    `updated_by` VARCHAR(30) NULL,
    PRIMARY KEY(`id`),
    INDEX `idx_price_date` (`price_date`) USING BTREE,
    INDEX `idx_symbol` (`symbol`) USING BTREE
) ENGINE = InnoDB DEFAULT CHARSET = utf8;