class Solution {
public:
    string frequencySort(string s) {
        vector<pair<int,char>> characters(62,{0,0});
        for(char x: s){
            if(x>='a' && x<='z'){
                characters[x-'a'].second=x;
                characters[x-'a'].first++;
            }else if(x>='A' && x<='Z'){
                characters[x-'A'+26].first++;
                characters[x-'A'+26].second=x;
            }else if(x>='0' && x<='9'){
                characters[x-'0'+52].first++;
                characters[x-'0'+52].second=x;
            }   
        }
        
        sort(characters.begin(), characters.end(), [](pair<int,char> a, pair<int,char> b){
            return a.first>b.first;
        });
        
        string ans="";
        for(auto data: characters){
            if(data.first>0){
                int count=data.first;
                cout<<data.second<<" "<<count<<endl;
                while(count--)ans+=data.second;
            }
        }
        return ans;
    }
};