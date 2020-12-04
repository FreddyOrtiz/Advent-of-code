# include <fstream>
# include <iostream>
# include <vector>

using namespace std;

int main()
{
    ifstream file("input.txt");
	vector<int> v;
	while (file.eof() == false){
		int a;
		file >> a;
		v.push_back(a);
	}
	file.close();
	
	for(int a : v)
		for(int b : v)
			if(a + b == 2020)
				cout << a*b << endl;
}
