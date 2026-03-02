class Solution {
public:
    int winningPlayerCount(int n, vector<vector<int>>& pick) {
        unordered_map<int,unordered_map<int,int>> hash; // player-> [ball,count] 
        // cutu mwahh 
        // love you
        for(auto data: pick){
            int player= data[0], ballColor=data[1];
            hash[player][ballColor]++;
        }
        int winnersCount=0;
        for(auto data: hash){
            int player=data.first;
            bool flag=false;
            auto smallHash= data.second;
            for(auto pair: smallHash){
                int color=pair.first, count=pair.second;
                if(count>player){
                    flag=true;
                    break;
                }
            }
            if(flag)winnersCount++;    
        }
        return winnersCount;
    }
};