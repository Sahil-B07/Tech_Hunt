#include<iostream>
//Find the value of a and b at end in given program

using namespace std;
	
int main()
{
    int a= 2;
    int b = 6;
    int c = 4;
    
    int result;
    
    result = a = b;
    b = a = result;

    return 0;
}
