#include <iostream>

using namespace std;

char s[19];

int a[19];

int p[13] = { 0,31,28,31,30,31,30,31,31,30,31,30,31 };

long long h1[19], h2[19], h3[19], h4[19], h5[19];

int pp1(int x) {

    return x / 10000 * 2 + x / 1000 % 10 * 10 + x / 100 % 10 * 9 + x / 10 % 10 * 8 + x % 10 * 7;

}

int pp2(int x) {

    return x / 10000 * 6 + x / 1000 % 10 * 5 + x / 100 % 10 * 4 + x / 10 % 10 * 3 + x % 10 * 2;

}

int mod(int x) {

    return x >= 10 ? 19 - x : x;
}

int yue(int x, int y) {

    if (((x % 4 == 0 && x % 100) || x % 400 == 0) && y == 2)

        return 29;

    return p[y];

}

int pd1(int a) {

    for (int i = 7; i >= 4; i--) {

        if ((s[i] != 'B') && ((s[i] - '0') != a % 10))

            return 0; a /= 10;

    }

    return 1;

}

int pd2(int a) {

    for (int i = 3; i >= 2; i--, a /= 10)

        if ((s[i] != 'B') && ((s[i] - '0') != a % 10))

            return 0;

    return 1;

}

int pd3(int a) {

    for (int i = 1; i >= 0; i--, a /= 10)

        if ((s[i] != 'B') && (s[i] - '0') != a % 10)

            return 0;

    return 1;

}

int scd(int a, int b, int c) {

    int h = 0;

    for (int i = 3; i <= 6 && a; i++, a /= 10)h += a % 10 * i;

    for (int i = 7; i <= 8 && b; i++, b /= 10)h += b % 10 * i;

    for (int i = 9; i <= 10 && c; i++, c /= 10)h += c % 10 * i;

    return h % 19;

}

int main() {

    cin >> s;

    for (int i = 1; i <= 9999; i++)

        if (pd1(i)) {

            for (int j = 1; j <= 12; j++)

                if (pd2(j)) {

                    for (int k = 1; k <= yue(i, j); k++)

                        if (pd3(k)) {

                            h1[scd(i, j, k)]++;

                        }

                }

        }

    if (s[18] == 'B') {

        long long count = 1, sss = 0;

        for (int i = 8; i<18; i++)

            if (s[i] == 'B')

                count *= 10;

        for (int i = 0; i<19; i++)

            sss += h1[i];

        cout << count*sss;
        return 0;

    }

    int ka, ff;

    for (ka = 0; ka <= 99999; ka++) {

        ff = 1;

        for (int i = 4, j = ka; i >= 0; j /= 10, i--)

            if ((s[i + 8] != 'B') && (j % 10 != s[i + 8] - '0'))

                ff = 0;

        if (ff) {

            h2[pp1(ka) % 19]++;
        }

    }

    for (ka = 0; ka <= 99999; ka++) {

        ff = 1;

        for (int i = 4, j = ka; i >= 0; j /= 10, i--)

            if ((s[i + 13] != 'B') && (j % 10 != s[i + 13] - '0'))

                ff = 0;

        if (ff) {

            h3[pp2(ka) % 19]++;
        }

    }

    for (int i = 0; i<19; i++)

        for (int j = 0; j<19; j++)

            h4[(i + j) % 19] += h2[i] * h3[j];

    for (int i = 0; i<19; i++)

        for (int j = 0; j<19; j++)

            h5[(i + j) % 19] += h4[i] * h1[j];

    cout << h5[s[18] - '0'] + h5[19 - s[18] + '0'];
}
