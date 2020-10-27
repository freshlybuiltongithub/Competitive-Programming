#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
    while(t--){
        int n;
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++){
            cin>>a[i];   
        }   
        long long j=5,f=0;
        int c1=0,c2=0;
        if(a[0]==5){
            c1=1;
            for(int i=1;i<n;i++){
               
                if(a[i]==5)
                c1++;
                else if(a[i]==10&&c1>0){
                    c2++;
                    c1--;
                }
                else if(a[i]==15&&(c1>=2||c2>0)){
                    
                    if(c2>0)
                    c2--;
                    else if(c1>=2)
                    c1=c1-2;
                }
                else
                {
                    f=1;
                    break;
                }   
            }
             if(f==0)
        cout<<"YES\n";
        else
        cout<<"NO\n";
        }
        else{
            cout<<"NO\n";
        }      
    }
	return 0;
}

