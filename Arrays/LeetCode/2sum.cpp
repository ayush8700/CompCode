// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution
{
public:
  vector<int> twoSum(vector<int> &nums, int target)
  {
    unordered_map<int, int> umap;

    for (int i = 0; i < nums.size(); i++)
    {
      int complement = target - nums[i];
      if (umap.find(complement) == umap.end())
        umap[nums[i]] = i;
      else
        return vector<int>{umap[complement], i};
    }

    return vector<int>{};
  }
};