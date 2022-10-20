use [FinalProj];

drop table Rental;
drop table CustPhone;
drop table Customer;
drop table Vehicle;
drop table VehicleType;
drop table Employee;
drop table Branch;

create table   Customer(cID int primary key   NOT NULL,
                        fName     varchar(10) NOT NULL,
				  	    lName     varchar(15) NOT NULL,
				 	    DOB       varchar(10) NOT NULL,
				 	    street    varchar(30) NOT NULL,
				 	    suite     varchar( 6),
				 	    zipCode   varchar(10) NOT NULL,
				 	    city      varchar(35) NOT NULL,
				 	    province  varchar( 2) NOT NULL,
						country   varchar(60) NOT NULL,
						email     varchar(60) NOT NULL,
					    gsObtain  varchar(10));

create table  CustPhone(cID       int NOT NULL, 
                        phoneNum  varchar(15) NOT NULL,
						primary key (cID, phoneNum),
					    foreign key(cID) references Customer(cID));

create table     Branch(bID int primary key    NOT NULL,
                        street     varchar(30) NOT NULL,
					    suite      varchar( 6),
					    zipCode    varchar( 6) NOT NULL,
					    city       varchar(35) NOT NULL,
					    state_prov varchar( 2) NOT NULL,
						country    varchar(60) Not NULL);

create table Employee(eID int primary key NOT NULL,
                        fName     varchar(10) NOT NULL,
					    lName     varchar(15) NOT NULL,
					    branch    int NOT NULL,
					    salary    float NOT NULL,
					    foreign key(branch) references Branch(bID));

create table VehicleType(tID int primary key,
                         tName       varchar(20),
						 costDaily   float,
						 costWeekly  float,
						 costMonthly float);

create table    Vehicle(vID int primary key,
                        tID int,
					    locIN int,
					    foreign key(locIN) references Branch(bID),
					    foreign key(tID)  references VehicleType(tID));

create table      Rental(rID         int primary key NOT NULL IDENTITY(1,1),
                         reqBy       int NOT NULL,
						 procBy      int,
						 vID         int,
						 dateFrom    varchar(20) NOT NULL,
						 dateTo      varchar(20) NOT NULL,
						 pickUpLoc   int NOT NULL,
						 dropOffLoc  int,
						 dropOffDate varchar(10),
						 vTypeReq    int NOT NULL,
						 foreign key(reqBy) references Customer(cID),
						 foreign key(procBy) references Employee(eID),
						 foreign key(vID) references Vehicle(vID),
						 foreign key(pickUpLoc) references Branch(bID),
						 foreign key(dropOffLoc) references Branch(bID),
						 foreign key(vTypeReq) references vehicleType(tID));

--select * from Branch;
--select * from Customer;
--select * from CustPhone;
--select * from Employee;
--select * from Rental;
--select * from Vehicle;
--select * from VehicleType;
