drop database if exists autotrade;
create database autotrade;
use autotrade;

create table ok_kline (
    `id` varchar(50) not null,
    `amount` varchar(50) not null,
    `open` varchar(50) not null,
    `close` varchar(50) not null,
    `high` varchar(50) not null,
    `low` varchar(50) not null,
    `time_stamp` real not null,
    key `idx_time_stamp` (`time_stamp`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table huobi_kline (
    `id` varchar(50) not null,
    `amount` varchar(50) not null,
    `open` varchar(50) not null,
    `close` varchar(50) not null,
    `high` varchar(50) not null,
    `low` varchar(50) not null,
    `time_stamp` real not null,
    key `idx_time_stamp` (`time_stamp`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table ok_multi_day_line (
    `id` varchar(50) not null,
    `five_days_line` varchar(50) not null,
    `ten_days_line` varchar(50) not null,
    `twenty_days_line` varchar(50) not null,
    `sixty_days_line` varchar(50) not null,
    `time_stamp` real not null,
    key `idx_time_stamp` (`time_stamp`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table huobi_multi_day_line (
    `id` varchar(50) not null,
    `five_days_line` varchar(50) not null,
    `ten_days_line` varchar(50) not null,
    `twenty_days_line` varchar(50) not null,
    `sixty_days_line` varchar(50) not null,
    `time_stamp` real not null,
    key `idx_time_stamp` (`time_stamp`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table ok_trade_history (
    `id` varchar(50) not null,
    `amount` varchar(50) not null,
    `create_at` real not null,
    `canceled_at` real not null,
    `place_price` varchar(50) not null,
    `order_id` varchar(50) not null,
    `finished_at` real not null,
    `field_amount` varchar(50) not null,
    `symbol` varchar(50) not null,
    `state` varchar(50) not null,
    `trade_type` varchar(50) not null,
    `field_cash_amount` varchar(50) not null,
    unique key `idx_order_id` (`order_id`),
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;

create table huobi_trade_history (
    `id` varchar(50) not null,
    `amount` varchar(50) not null,
    `create_at` real not null,
    `canceled_at` real not null,
    `place_price` varchar(50) not null,
    `order_id` varchar(50) not null,
    `finished_at` real not null,
    `field_amount` varchar(50) not null,
    `symbol` varchar(50) not null,
    `state` varchar(50) not null,
    `trade_type` varchar(50) not null,
    `field_cash_amount` varchar(50) not null,
    unique key `idx_order_id` (`order_id`),
    key `idx_created_at` (`created_at`),
    primary key (`id`)
) engine=innodb default charset=utf8;