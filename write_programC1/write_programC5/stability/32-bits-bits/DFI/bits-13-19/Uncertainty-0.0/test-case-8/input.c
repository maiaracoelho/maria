#include <dsverifier.h>

digital_system controller = { 
	.b = {  -4.6566e-10 , 1 , -1 },
	.b_uncertainty = {  0 , 0 , 0 },
	.b_size =  3,
	.a = {  1 , -4.6566e-10 , 4.6566e-10 },
	.a_uncertainty = {  0 , 0 , 0 },
	.a_size =  3,
	.sample_time = 1.000000e-03
};

implementation impl = { 
	.int_bits = 13,
	.frac_bits = 31,
	.max =  1.000000,
	.min =  -1.000000
	};

digital_system plant = { 
	.b = {  0 , 5e-05 , 5e-05 },
	.b_uncertainty = {  0 , 0 , 0 },
	.b_size =  3,
	.a = {  1 , -2 , 1 },
	.a_size =  3, 
	.a_uncertainty = {  0 , 0 , 0 }
	};

