#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
    while(t--){
        long long n,ans=0,c=0,k,temp;
        
        cin>>n;
        k=n;
        if(n==1||n==2){
            ans=0;
        }
        else if(n%2!=0){
            ans=n/2;
        }
        else{
            while(n%2==0){
            n=n/2;
            c++;
            }
            temp=pow(2,c);
            ans=(k/temp)/2;
           }
        cout<<ans<<"\n";
    }
	return 0;
}

