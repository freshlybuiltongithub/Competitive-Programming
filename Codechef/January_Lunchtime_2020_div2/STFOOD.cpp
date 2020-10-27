#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
    while(t--){
        int n;
        cin>>n;
        long int max=0;
        for(int i=0;i<n;i++){
            int s,p,v;
            cin>>s>>p>>v;
            if(max<(p/(s+1))*v)
            max=(p/(s+1))*v;
           
        }
        cout<<max<<"\n";
        //cout<<int(7.9);
    }
	return 0;
}

