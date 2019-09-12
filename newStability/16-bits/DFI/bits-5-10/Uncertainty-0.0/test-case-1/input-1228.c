#include <dsverifier.h>

digital_system controller = { 
	.b = {  0.0039062 , 0.00097656 },
	.b_uncertainty = {  0 , 0 },
	.b_size =  2,
	.a = {  0.31348 , -0.00097656 },
	.a_uncertainty = {  0 , 0 },
	.a_size =  2,
	.sample_time = 2.000000e-01
};

implementation impl = { 
	.int_bits = 5,
	.frac_bits = 10,
	.max =  1.000000,
	.min =  -1.000000
	};

digital_system plant = { 
	.b = { 0.76, -0.66584 },
	.b_uncertainty = {  0 , 0 },
	.b_size =  2,
	.a = { 0, 0.0010339 },
	.a_size =  2, 
	.a_uncertainty = {  0 , 0 }
	};

