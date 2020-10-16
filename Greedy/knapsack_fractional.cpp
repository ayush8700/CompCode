// Given weights and values of n items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack.

#include <iostream>
#include <algorithm>

using namespace std;

struct Item
{
  int value;
  int weight;

  // Item(int v, int w)
  // {
  //     value = v;
  //     weight = w;
  // }

  Item(int v, int w) : value(v), weight(w) {}
};

bool compare(Item i1, Item i2)
{
  float ratio_vw = i1.value / i1.weight,
        ratio_vw2 = i2.value / i2.weight;

  return ratio_vw > ratio_vw2;
}

int frac_knapsack(int weight, Item item_list[], int n)
{
  int cur_weight = 0;
  float final_value = 0;

  sort(item_list, item_list + n, compare);

  for (int i = 0; i < n; i++)
  {
    if (cur_weight + item_list[i].weight <= weight)
    {
      cur_weight += item_list[i].weight;
      final_value += item_list[i].value;
    }
    else
    {
      int remaining_weight = weight - cur_weight;
      final_value += item_list[i].value * remaining_weight / item_list[i].weight;
    }
  }

  return final_value;
}

int main()
{
  int weight = 50;
  // Item item_list[] = {Item(50, 10), Item(20, 20), Item(40, 30)};
  Item item_list[] = {{50, 10}, {20, 20}, {40, 30}};

  int n = sizeof(item_list) / sizeof(item_list[0]);

  cout << "Maximum value = " << frac_knapsack(weight, item_list, n);
}