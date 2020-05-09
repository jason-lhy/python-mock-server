create table expectations (
    id varchar(64) not null primary key,
    path text not null,
    method varchar(10) not null,
    arguments json null,
    response json null
);