#include <iostream>
#include <string>
#include <stdio.h>
#include <ctime>
#include <random>
using namespace std;


int main(void)
{
    class CodeRange
    {
        //用功能(建構時)設定為不可公開存取
        private:
        int num_min = 0;
        int num_max = 0;
        int num_ans = 0;
        //用建構式(功能)設定為可公開存取
        public:
        int range_min = 0;
        int range_max = 0;
        //建構式(建構子 = 預設(初始化)功能)
        CodeRange(int min, int max, int ans)
        {
            num_min = min;
            num_max = max;
            num_ans = ans;

            range_min = min;
            range_max = max;
        }
        //超出範圍
        bool Outofrange(int guess)
        {
            return guess > range_max+1 || guess < range_min-1;
        }
        //比答案大
        bool Bigger(int guess)
        {
            if(guess > num_ans)
            {
                range_max = guess;
                return true;
            }
            else return false;
        }
        //比答案小
        bool Smaller(int guess)
        {
            if(guess < num_ans)
            {
                range_min = guess;
                return true;
            }
            else return false;

        }
        //猜中答案
        bool Correct(int guess)
        {
            return guess == num_ans;
        }
    };
    
    //const常數:不常變得值(要定義一個值給她)
    const int min = 1;
    const int max = 100;
    int guess = 0;
    mt19937 rd(time(NULL));
    uniform_int_distribution<int> dis(min, max);
    int pass = dis(rd);
    CodeRange cr(min, max, dis(rd));

    do
    {
        cout << "請輸入" << cr.range_min << "-" << cr.range_max << ":" << endl;
        cin >> guess;

        //輸入錯誤
        if(cr.Outofrange(guess))
        {
            cout << "輸入錯誤";
            continue;
        }
        //比答案大
        if(cr.Bigger(guess))
        {
            cout << "安全";
            continue;
        }
        //比答案小
        if(cr.Smaller(guess))
        {
            cout << "安全";
            continue;
        }
        //猜中答案
        if(cr.Correct(guess))
        {
            cout << "中了，遊戲結束";
            break;
        }
    }while(!cr.Correct(guess));
    system("Pause");




    return 0;
}
