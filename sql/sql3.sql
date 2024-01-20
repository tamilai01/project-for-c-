delimiter &&
drop procedure if exists singledelete;&&
create procedure singledelete
 (
 in tablename varchar(100),
 
in idname varchar(10),
in idparam int)
begin
set @statement= concat('delete ','from ' ,tablename,' where ',idname,'=',idparam);
prepare stmt from @statement;
execute stmt ;
 end &&
 delimiter ;
call singledelete('std_det', 'gender',3);
select *from std_det;