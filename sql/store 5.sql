use ai_tamil;
create table std_det2(sno int not null primary key auto_increment,
name varchar(50),
email varchar(50),
gender varchar(50),
qualification varchar(50)
);
delimiter \\
create procedure insert_table2 ( in snoparameter int,
in nameparameter varchar(50),
in emailparameter varchar(50),
in genderparameter varchar(50),
in qualificationparameter varchar(50)
)
begin
insert into std_det2(sno,name,email,gender,qualification) values (sno,nameparameter,emailparameter,genderparameter,qualificationparameter);
end \\
delimiter ;
select*from std_det2;
call insert_table2(1,'srinidhi','sri@gmail.com','female','bsc');
call insert_table2(2,'tamil','tamil@gmail.com','female','bsc');
call insert_table2(3,'snega','snega@gmail.com','female','bsc');
call insert_table2(4,'punitha','punitha@gmail.com','female','bcom');

