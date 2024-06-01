class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxsf = nums.at(0);
        int minsf = nums.at(0);
        int maxans = *std::max_element(nums.begin(),nums.end());

        int t;
        for (auto n = nums.begin() + 1; n != nums.end(); n++){
            if ((*n) == 0){
                maxsf = 1;
                minsf = 1;
                continue;
            }

            t = maxsf * (*n);
            maxsf = std::max((*n), std::max((*n) * minsf, t));
            minsf = std::min((*n), std::min((*n) * minsf, t));

            maxans = (std::max(maxsf, minsf) > maxans) ? std::max(maxsf, minsf) : maxans;
        }

        return maxans;
    }
};