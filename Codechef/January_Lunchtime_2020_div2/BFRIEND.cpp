#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
    while(t--){
        long n,a,b,c;
         cin>>n>>a>>b>>c;
         long m=INT_MAX,min=0;
         int a1[n];
         for(long i=0;i<n;i++){
            cin>>a1[i]; 
            if((abs(a1[i]-b)+abs(a1[i]-a))<m){
            min=i;
            m=(abs(a1[i]-b)+abs(a1[i]-a));
         }}
         cout<<(abs(a1[min]-b)+abs(a1[min]-a))+c<<"\n";
         
    }
	return 0;
}

