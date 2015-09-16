#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &numbers, int target) {
        unordered_map<int, int> num_map; // {num, index}

        for (int index1=0; index1 < numbers.size(); ++index1) {
            int num1 = numbers[index1];
            int num_to_find = target - num1;
            auto iter = num_map.find(num_to_find);
            if (iter != num_map.cend()) {
                return vector<int> {iter->second, index1+1};
            }

            num_map[num1] = index1 + 1;
        }

    }
};

int main()
{
    vector<int> input_nums = {2, 7, 11, 15};


    Solution sol;
    vector<int> res = sol.twoSum(input_nums, 9);
    for (auto &r: res) {
        cout<< r << endl;
    }

    return 0;
}
