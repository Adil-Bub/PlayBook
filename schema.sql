drop table if exists posts;
create table posts (
    id integer primary key autoincrement,
    name text not null,
    content text not null,
    Timestamp DATETIME default (datetime(current_timestamp, 'localtime'))
);
