//輸入輸出的程式庫
#include <iostream>
//標準字串的程式庫
#include <string>
//時間程式庫
#include <ctime>
//亂數程式庫
#include <random>
//使用 標準程式庫 std
using namespace std;
//清單程式庫
#include <list>
//演算程式庫
#include <algorithm>

#include <stdio.h>

//選號機(副程式):放入球數，選幾顆球
list<int> Generator(int max, int count)
{
    list<int> numbers;
    mt19937 rg(time(NULL));
    uniform_int_distribution<int> dis(1, max);

    for(int i=0; i<count;)// i++)
    {
        int num = dis(rg);
        //過濾重複號碼(如果未收尋到，返回為後一個元素)(要用find函數要導入algorithm程式庫)
        if(find(numbers.begin(), numbers.end(), num) == numbers.end())
        {
            numbers.push_back(num);
            i++;
        }
    }
    return numbers;
}


//選單結構(主程式)
int main()
{
    int game_num = 0;
    bool quit = false;
    list<int> result;

    do
    {
        cout << "*****遊戲號碼*****" << endl
             << "0. 結束遊戲" << endl
             << "1. 大樂透" << endl
             << "2. 威力彩" << endl
             << endl << "請輸入號碼:" ;

        cin >> game_num;

        switch (game_num)
        {
            case 0:
                quit = true;
                break;
            case 1:
                //入球規則
                result = Generator(49, 6);
                //output
                cout << endl << "本期大樂透號碼抽出：";
                //遍歷集合物件所有元素
                for(int i : result)
                {
                    cout << " " << i << " ";
                }
                cout << endl << endl << "------------------------------" << endl;
                break;
            case 2:

                
                //第一區
                 //入球規則
                result = Generator(38, 6);
                //output
                cout << endl << "本期威力彩號碼抽出" << endl << "第一區 抽出：";
                //遍歷集合物件所有元素
                for(int i : result)
                {
                    cout << " " << i << " ";
                }

                result = Generator(8, 1);
                cout << endl << "第二區 抽出：";
                for(int i : result)
                {
                    cout << " " << i << " ";
                }

                cout << endl << endl << "------------------------------" << endl;
                break;

            default:
                cout << endl << "輸入錯誤！！！" << endl;
                cout << endl << "------------------------------" << endl << endl;
                break;
        }
    } while (!quit);
    system("Pause");

    return 0;
}