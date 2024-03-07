#include <chrono>

#include "bigint.h"
#include "test_bignums.h"



int main()
{{{ 
	TestBigInt::full_suite();
	BenchmarkBigInt::full_suite();

	return 0;
}}}

