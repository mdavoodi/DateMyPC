drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  pickup text not null,
  datetime text not null
);
