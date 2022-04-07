create table users (
uid integer primary key,
username text not null
);

create table user_statistics (
login_count integer,
user integer,
foreign key(user) references users(uid)
);