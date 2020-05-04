#include <bits/stdc++.h>
using namespace std;
int sum(int n){
    int sum = 0;
    while(n>0){
        int temp = n % 10;
        sum += temp * temp ;
        n /= 10;
    }
    return sum;
}
bool isHappy(int n){
    if (sum(n) == 1 ){
        return true;
    }   
    else
        return false; 
}
int main(){
    int n;
    cin >> n;
    cout << isHappy(n);
}

