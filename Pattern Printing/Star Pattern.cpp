#include<iostream>

using namespace std;

int main()

{ 

  int p,c,f=1;

  cout<<"Pattern is:"<<endl;

  for(p=1;p<=4;p++)

     {

       for(c=1;c<=p;c++,f++)

         cout<<"*"<<" ";

           cout<<endl;

     }

return 0;


}
