#include<iostream>

using namespace std;

int main(int argc, char **argv) {
    int test_case;
    int T;
    int n, minD, cnt, x;
    int *A;

    cin >> T;
    for (test_case = 1; test_case <= T; ++test_case) {
        minD = 100000, cnt = 0;
        cin >> n;
        A = new int(n);
        for (int i = 0; i < n; i++) {
            cin >> A[i];
            x = (A[i] > 0?A[i]:-1*A[i]);
            -1 * A[i];
            if (minD > x) {
                minD = x, cnt = 1;
            } else if (minD == x) {
                cnt += 1;
            }
        }
        cout << "#" << test_case << " " << minD <<" "<< cnt << endl;
    }
    return 0;
}