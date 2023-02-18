class Solution {
public:
    int reverse(long long int x) {
       long long int flag = 0,rev=0,r;
        if(x<0){
            x = x*-1;
            flag=1;
        }
        while(x>0){
            r=x%10;
            x=x/10;
            rev=rev*10+r;
        }
        if(rev>INT_MAX)
            return 0;
        
        if(flag == 1)
            return rev*-1;
        else
            return rev;
        
    }
};