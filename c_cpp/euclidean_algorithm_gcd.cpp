#include<bits/stdc++.h>
using namespace std;
int32_t main(void) {
	int a = 3768, b = 1701, x = a, y = b;

	while (a % b > 0) {
		int temp = a % b;
		a = b;
		b = temp;
	}


	cout << b << " is the GCD of " << x << " and " << y;

}


//  a     b
// 126 = 12 * 10 + 6
// 12 = 6 * 2 + 0
// here after one operation , a becomes b and b becomes a%b until a%b becomes 0.