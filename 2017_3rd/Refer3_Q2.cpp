#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <string.h>

using namespace std;

#define NUM 200
#define SQR(v) ((v) * (v))

int clr[NUM], len[NUM], dp[NUM][NUM][NUM];

void max_gem_score(vector<string> gem_grps, int score, int &max_score)
{
    if (gem_grps.size() <= 1)
    {
        int final_score = score + SQR(gem_grps.at(0).size());
        max_score = max(max_score, final_score);
    }
    else if (gem_grps.size() <= 2)
    {
        int final_score = score + SQR(gem_grps.at(0).size()) + SQR(gem_grps.at(1).size());
        max_score = max(max_score, final_score);
    }
    else
    {
        for (vector<string>::iterator it = gem_grps.begin() + 1; it < gem_grps.end() - 1; it++)
        {
            vector<string> gem_grps_dup = gem_grps;
            int sub_score = score + it->size() * it->size();

            gem_grps.erase(it);

            for (vector<string>::iterator it = gem_grps.begin() + 1; it < gem_grps.end(); it++)
                if (it->at(0) == (it - 1)->at(0))
                {
                    *(it - 1) += *it;
                    gem_grps.erase(it);
                }
            max_gem_score(gem_grps, sub_score, max_score);

            gem_grps = gem_grps_dup;
        }
    }
}

int max_clr_score(int a, int b, int rest)
{
    if (dp[a][b][rest] != -1)
        return dp[a][b][rest];

    dp[a][b][rest] = max_clr_score(a, b-1, 0) + (len[b] + rest) * (len[b] + rest);

    for (int i = a; i < b; i++)
        if (clr[i] == clr[b])
        {
            dp[a][i][rest + len[b]] = max_clr_score(a, i, rest + len[b]);
            dp[i + 1][b - 1][0] = max_clr_score(i + 1, b - 1, 0);
            dp[a][b][rest] = max(dp[a][b][rest], dp[a][i][rest + len[b]] + dp[i + 1][b - 1][0]);
        }

    return dp[a][b][rest];
}

int main(void)
{
    string input, gem;
    vector<string> gem_grps;
    int max_score = 0;

    cin >> input;

    gem = input.at(0);
    for (string::iterator it = input.begin() + 2; it < input.end(); it += 2)
    {
        if (*it != *(it - 2))
        {
            gem_grps.push_back(gem);
            gem = *it;
        }
        else
            gem += *it;
    }
    gem_grps.push_back(gem);

    int n = gem_grps.size();

    if (n < 12)
        max_gem_score(gem_grps, 0, max_score);
    else
    {
        memset(dp, -1 , sizeof(dp));

        for (int i = 0; i < n; i++)
        {
            clr[i + 1] = gem_grps.at(i).at(0);
            len[i + 1] = gem_grps.at(i).size();
        }

        for (int i = 1; i <= n; i++)
            dp[i][i-1][0] = 0;

        max_score = max_clr_score(1, n, 0);
    }

    cout << max_score << endl;

    return 0;
}
