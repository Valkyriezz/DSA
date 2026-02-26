class Solution {
private:
    void addOne(string &s){
        int carry=0;
        for(int i=s.length()-1; i>=0; i--){
            if(s[i]=='1'){
                s[i]='0';
                carry=1;
            }else{
                s[i]='1';
                carry=0;
                break;
            }
        }
        if(carry) s= '1' + s;
    }
public:
    int numSteps(string s) {
        int count=0;
        while(s!="1"){
            // check for odd or even
            if(s.back()=='0'){
                // means even hai
                s.pop_back(); // right shift basically
            }else addOne(s);
            count++;
        }
        return count;
    }
};