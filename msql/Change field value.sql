-- Update values
select * from woodscrews
where woodscrew_id = 11;


update woodscrews
set have_stock = "Yes", 
head_dia = 9.92, 
countersink_drill = 10.0, 
shank_dia =4.76, 
shank_clearance_drill = 5.5,
softwood_pilot_dia = 3.0,
hardwood_pilot_dia =3.0,
plug_size = "Brown",
masonry_drill = 7
where woodscrew_id = 11;