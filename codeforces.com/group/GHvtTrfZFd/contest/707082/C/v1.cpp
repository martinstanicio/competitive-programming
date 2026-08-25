#include <bits/stdc++.h>

#define forr(i, from, to) for (ll i = from; i < to; i++)

using namespace std;
using ll = long long;
using dd = long double;

int main()
{
  ll players, bid, multiplicity, min_multiplicity, max_multiplicity;
  vector<ll> bids;

  cin >> players;

  forr(i, 0, players)
  {
    cin >> bid;
    bids.push_back(bid);
  }

  ll _gcd = gcd(bids[0], bids[1]);

  forr(i, 2, players)
      _gcd = gcd(_gcd, bids[i]);

  forr(i, 0, players)
  {
    bid = bids[i];
    bid /= _gcd;

    while (bid % 2 == 0)
      bid /= 2;

    while (bid % 3 == 0)
      bid /= 3;

    if (bid > 1)
    {
      cout << "No" << '\n';

      return 0;
    }
  }

  cout << "Yes" << '\n';

  return 0;
}
