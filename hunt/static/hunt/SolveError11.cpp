//Correct the Given Code

#include<iostream>

using naespace std;

class Hero:
{
    public:
	Hero(){
		cout>>"Constructor Executed!!"<<endl;
	}
	void printHello(){
		cout<<"Hello!!">>endl;
	}
}


int main()
{
	Hero h1;
	h1.printHello();
	return 0;
}
