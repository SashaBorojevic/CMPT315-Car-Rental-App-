--Inserting customers into table...
insert into Customer values(1001, 'Wanda', 'Maximoff', '02-10-1976', '111 Scarlet Lane', null, 'T2E3R8', 'Calgary', 'AB', 'Canada', 'ilovevision@hotmail.com', 0);
insert into Customer values(2002, 'Jonah', 'Hill', '12-20-1983', '22 Jump Street', null, 'V5T3L1', 'Vancouver', 'BC', 'Canada', 'superbadboy69@hotmail.com', 0);
insert into Customer values(3003, 'Scooby', 'Doo', '09-13-1969', '32 Crystal Cove Crescent', null, 'T8N5J3', 'Edmonton', 'AB', 'Canada', 'shaggyandscoob@gmail.com', 0);
insert into Customer values(4004, 'Severus', 'Snape', '01-09-1960', 'Hogwarts Castle', 'P394', 'SW1A0AA', 'Higlands', 'HM', 'Scotland', 'lovelylily33@gmail.com', 0);
insert into Customer values(5005, 'James', 'Halpert', '10-01-1978', '2897 Dunder Drive', null, '18576', 'Scranton', 'PA', 'USA', 'goldenfaceismyname@live.ca', 0);
insert into Customer values(6006, 'Meredith', 'Grey', '11-10-1969', '613 Harper Lane', null, '98168', 'Seattle', 'WA', 'USA', 'pickmechooseme@hotmail.com', 0);
insert into Customer values(7007, 'Elanor', 'Rigby', '08-05-1966', '124 Penny Lane', null, 'M4C6G7', 'Toronto', 'ON', 'Canada', 'allthelonelypeople@live.ca', 0);
insert into Customer values(8008, 'Scout', 'Finch', '03-04-1927', '06 Mockingbird Drive', '46D', '36490', 'Maycomb', 'AL', 'USA', 'booraadleyy@gmail.com', 0);
insert into Customer values(9009, 'Britney', 'Spears', '12-02-1981', 'BB1 More Time Blvd', '123', '39655', 'McComb', 'MI', 'USA', 'freebritney2021@live.ca', 0);

--Inserting branches into table...
Insert into Branch values(0001, '1122 Sriracha Blvd', null, 'T5R2R9', 'Edmonton', 'AB', 'Canada');
Insert into Branch values(0002, '3113 Monroe Street', null, 'T2G6Y5', 'Calgary', 'AB', 'Canada');
Insert into Branch values(0003, '2110 Bread Pudding Blvd', '86A', 'V1P4F9', 'Kelowna', 'BC', 'Canada');
Insert into Branch values(0004, '3377 Evangelista Lane', null, 'V5T8L8', 'Vancouver', 'BC', 'Canada');
Insert into Branch values(0005, '550 Blueberry Blvd', '97G', 'S0K6J5', 'Saskatoon', 'SK', 'Canada');
Insert into Branch values(0006, '8920 Raptor Crescent', null, 'M4X5T5', 'Toronto', 'TO', 'Canada');

--Inserting employees into table...
insert into Employee values(1111, 'John', 'Malkovich', 0001, 50000);
insert into Employee values(2222, 'Edward', 'Cullen', 0002, 60000);
insert into Employee values(3333, 'Hayao', 'Miyazaki', 0002, 55000);
insert into Employee values(4444, 'Johnny', 'Depp', 0003, 70000);
insert into Employee values(5555, 'Donnie', 'Darko', 0001, 68000);
insert into Employee values(6666, 'Lucifer', 'Helman', 0004, 66600);
insert into Employee values(7777, 'Lucky', 'Charm', 0003, 77000);
insert into Employee values(8888, 'Shrek', 'Green', 0001, 62000);
insert into Employee values(9999, 'Jerry', 'Seinfeld', 0005, 90000);

--Inserting vehicle types into table...
insert into VehicleType values(0011, 'Compact', 50.00, 300.00, 1150.00);
insert into VehicleType values(0022, 'Midsize', 60.00, 360.00, 1350.00);
insert into VehicleType values(0033, 'SUV', 65.00, 390.00, 1450.00);
insert into VehicleType values(0044, 'Convertable', 75.00, 475.00, 1850.00);

--Inserting vehicles into table...
insert into Vehicle values(0111, 0011, 0001);
insert into Vehicle values(0112, 0022, 0001);
insert into Vehicle values(0113, 0033, 0001);
insert into Vehicle values(0114, 0044, 0001);
insert into Vehicle values(0222, 0011, 0002);
insert into Vehicle values(0223, 0022, 0002);
insert into Vehicle values(0224, 0033, 0002);
insert into Vehicle values(0225, 0044, 0002);
insert into Vehicle values(0333, 0011, 0003);
insert into Vehicle values(0334, 0022, 0003);
insert into Vehicle values(0335, 0033, 0003);
insert into Vehicle values(0336, 0044, 0003);
insert into Vehicle values(0444, 0011, 0004);
insert into Vehicle values(0445, 0022, 0004);
insert into Vehicle values(0446, 0033, 0004);
insert into Vehicle values(0447, 0044, 0004);
insert into Vehicle values(0555, 0011, 0005);
insert into Vehicle values(0556, 0022, 0005);
insert into Vehicle values(0557, 0033, 0005);
insert into Vehicle values(0558, 0044, 0005);
insert into Vehicle values(0666, 0011, 0006);
insert into Vehicle values(0667, 0022, 0006);
insert into Vehicle values(0668, 0033, 0006);
insert into Vehicle values(0669, 0044, 0006);

--Inserting customer phone numbers...
insert into CustPhone values(1001, 4038996767);
insert into CustPhone values(2002, 6047763432);
insert into CustPhone values(3003, 7808075544);
insert into CustPhone values(4004, 1122477633);
insert into CustPhone values(5005, 5709996465);
insert into CustPhone values(6006, 2067773267);
insert into CustPhone values(7007, 4169984456);
insert into CustPhone values(8008, 4057433355);
insert into CustPhone values(9009, 6017334878);
