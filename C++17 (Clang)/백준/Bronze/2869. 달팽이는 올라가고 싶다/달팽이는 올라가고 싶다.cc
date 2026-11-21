#include <iostream>
using namespace std;

int main() {
	int A, B, V;
	int res= 0, dis = 0;
	cin >> A;
	cin >> B;
	cin >> V;
	
	res = (V - B) / (A - B);
	if ((V - B) % (A - B) > 0)
		res++;
	cout << res;
}