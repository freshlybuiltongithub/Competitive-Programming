#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
    while(t--){
        int n;
        cin>>n;
        int c=0;
        int k=n,j=0,t=0,l=n,i=1,p=0,m1[n][n],y;
        while(i<=n*n){
            for(int m=j;m<k;m++){
                m1[j][m]=i++;
              
            }
            for( y=j+1;y<l;y++ ){
                m1[y][l-1]=i++;
              
            }
         l--;
            for(int x=l-1;x>=p;x--){
                m1[y-1][x]=i++;
                
            }
            for(int z=l-1;z>j;z--)
            {
                m1[z][j]=i++;
            }
            j++;
            k--;
            p++;
        }
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                cout<<m1[i][j]<<" ";
            }
            cout<<"\n";
        }
    
        
        
    }
	return 0;
}

