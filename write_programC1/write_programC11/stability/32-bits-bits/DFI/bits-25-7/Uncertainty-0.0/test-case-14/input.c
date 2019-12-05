#include <dsverifier.h>

digital_system controller = { 
	.b = {  -45456.4327 , 37928.1361 , 25543.7663 , -38701.0881 , 16110.0087 , -2847.8579 , 182.2326 , 0.38487 },
	.b_uncertainty = {  0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 },
	.b_size =  8,
	.a = {  1 , 0.47737 , -1.4922 , -0.6236 , 0.64615 , 0.10413 , -0.12437 , 0.018243 },
	.a_uncertainty = {  0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 },
	.a_size =  8,
	.sample_time = 3.000000e-02
};

implementation impl = { 
	.int_bits = 25,
	.frac_bits = 7,
	.max =  1.000000,
	.min =  -1.000000
	};

digital_system plant = { 
	.b = {  0 , -0.0001492 , -0.00051649 , -7.2373e-05 },
	.b_uncertainty = {  0 , 0 , 0 , 0 },
	.b_size =  4,
	.a = {  1 , -7.8381 , 2.9258 , -0.25393 },
	.a_size =  4, 
	.a_uncertainty = {  0 , 0 , 0 , 0 }
	};

