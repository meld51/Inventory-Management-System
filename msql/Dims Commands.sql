-- Create Woodscrew Table
create table woodscrews(
	woodscrew_id int not null auto_increment,
    have_stock varchar(3),
    imperial_gauge int,
    metric_gauge decimal(3,2),
    head_dia decimal(4,2),
    countersink_drill decimal(3,1),
    shank_dia decimal(3,2),
    shank_clearance_drill decimal(2,1),
    softwood_pilot_dia decimal(2,1),
    hardwood_pilot_dia decimal(2,1),
    plug_size Varchar(255),
    masonry_drill Varchar(255),
    primary key (woodscrew_id)
);

insert into woodscrews
values (default, "No", 4,	3,	12.70,	12.0, 6.35,	7.0,	3.5,	4.0,	"Blue",	10, 30, "pozidriv");


