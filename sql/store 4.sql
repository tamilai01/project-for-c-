delimiter &&
drop procedure if exists singledelete;&&
create procedure singledelete
 (
 in tablename varchar(100),
 in columnname varchar(58))
 begin
set @statement= concat('alter table ',tablename,' add column ',columnname,' varchar \(58\)');
prepare stmt from @statement;
execute stmt ;                                          
 end &&
 delimiter ;
call singledelete ('std_det','ph_no');
select *from std_det;