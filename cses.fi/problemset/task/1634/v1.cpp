#include <bits/stdc++.h>

#define forr(i, from, to) for (int i = from; i < to; i++)

using namespace std;
const int MAXN = 1e6 + 1;

int main()
{
    int n, target, c;

    cin >> n >> target;

    vector<int> coins(n, 0);
    forr(i, 0, n) cin >> coins[i];

    vector<int> dp(target + 1, MAXN);
    dp[0] = 0;

    forr(i, 0, n)
    {
        c = coins[i];

        forr(x, c, target + 1)
        {
            dp[x] = min(1 + dp[x - c], dp[x]);
        }
    }

    cout << (dp[target] == MAXN ? -1 : dp[target]) << "\n";

    return 0;
}
