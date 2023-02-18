class Solution {
public:
    int climbStairs(int n) {
        if(n==1){
            return 1;
        }
        int a=0, b = 1, c;
        for(int i=0;i<n;i++){
            c = a+b;
            a = b;
            b = c;
        }
        return b;
        
    }
};