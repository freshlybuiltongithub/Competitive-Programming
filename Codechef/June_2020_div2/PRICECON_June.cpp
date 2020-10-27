#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
    while(t--){
        int n,k;
        cin>>n>>k;
        int x,d=0;
        for(int i=0;i<n;i++){
            cin>>x;
            if(x>k)
            d+=x-k;
        }
        cout<<d<<endl;
    }
	return 0;
}

