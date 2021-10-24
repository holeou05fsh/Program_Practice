#include <iostream>
#include <string>
#include <stdio.h>
#include <random>
#include <ctime>
using namespace std;


int main(void)
{
    int min = 1;
    int max = 100;
    int range_min = min;
    int range_max = max;

    mt19937 rd(time(NULL));
    uniform_int_distribution<int> dis(min, max);
    int pass = dis(rd);
    //cout << pass << endl;

    int guess = 0;

    do
    {
        cout << "請輸入" << range_min << "-"<< range_max << ":" << endl;
        cin >> guess;

        //輸入錯誤範圍
        if(guess > range_max+1 || guess < range_min-1)
        {
            cout << "輸入錯誤。" << endl;
            continue;
        }
        //比答案大
        if(guess > pass)
        {
            range_max = guess;
            cout << "安全。" << endl;
            continue;
        }
        //比答案小
        if(guess < pass)
        {
            range_min = guess;
            cout << "安全。" << endl;
            continue;
        }
        //猜中
        if(guess == pass)
        {
            cout << "中了，遊戲結束";
            break;
        }

    } while (guess != pass);
    system("pause");



    return 0;
}