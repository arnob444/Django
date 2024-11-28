#include <bits/stdc++.h>
using namespace std;
int pageFaults(int p[], int n, int block)
{
    unordered_set<int> s;
    queue<int> indexes;

    int page_faults = 0;
    for (int i = 0; i < n; i++)
    {
        if (s.size() < block)
        {

            if (s.find(p[i]) == s.end())
            {
                s.insert(p[i]);
                page_faults++;
                indexes.push(p[i]);
            }
        }
        else
        {
            if (s.find(p[i]) == s.end())
            {
                int val = indexes.front();
                indexes.pop();
                s.erase(val);
                s.insert(p[i]);
                indexes.push(p[i]);
                page_faults++;
            }
        }
    }
    return page_faults;
}

int main()
{
    int p[] = {2, 3, 2, 1, 5, 2, 4, 5, 3, 2, 5, 2};
    int n = sizeof(p) / sizeof(p[0]);
    int block = 3;
    cout << pageFaults(p, n, block);
    return 0;
}
