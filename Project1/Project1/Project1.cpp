#include <iostream>
#include <math.h>
#include <ctime>
#include <fstream>
#include <string>
using namespace std;

bool itWork = true;

void arrayGen()
{
    string userInput, manualInput;
    long long arraySize = 0;
    unsigned int start_time;
    unsigned int end_time;
    double search_time;
    cout << "Type\n(int - 1/double - 2/char - 3)(or exit)\n";
    cin >> userInput;

    if (userInput == "1") {

        cout << "Size\n(10/100/1000/10 000/100 000 000)\n";
        cin >> arraySize;
        cout << "Manual input(yes/no)\n";
        cin >> manualInput;

        start_time = clock();

        int* arr = new int[arraySize];
        for (int i = 0; i < arraySize; i++) {
            if (manualInput == "yes") {
                cin >> arr[i];
            }
            else if (manualInput == "no") {
                arr[i] = rand();
                cout << arr[i] << " ";
            }
        }



        end_time = clock();
    }
    else if (userInput == "2") {

        cout << "Size\n(10/100/1000/10 000/100 000 000)\n";
        cin >> arraySize;
        start_time = clock();

        float* arr = new float[arraySize];
        for (int i = 0; i < arraySize; i++) {
            if (manualInput == "yes") {
                cin >> arr[i];
            }
            else if (manualInput == "no") {
                float a = rand() / 3.0;
                arr[i] = a;
                cout << arr[i] << " ";;
            }

        }

        end_time = clock();
    }
    else if (userInput == "3") {

        cout << "Size\n(10/100/1000/10 000/100 000 000)\n";
        cin >> arraySize;
        start_time = clock();

        char* arr = new char[arraySize];
        for (int i = 0; i < arraySize; i++) {
            if (manualInput == "yes") {
                cin >> arr[i];
            }
            else if (manualInput == "no") {
                arr[i] = rand();
                cout << arr[i] << " ";
            }
        }

        end_time = clock();
    }
    else if (userInput == "exit") {
        itWork = false;
        start_time = 0;
        end_time = 0;
    }
    else {
        cout << "incorect word" << endl;
        arrayGen();
    }

    ofstream fout;

    fout.open("cppLogs.txt", ios_base::app);

    search_time = (end_time - start_time) / 1000.0;
    if (userInput != "exit") {
        cout << "\nSize: " << arraySize << " Type: " << userInput << " Time: " << search_time << "\n";
        fout << "Size: " << arraySize << " Type: " << userInput << " Time: " << search_time << "\n";
    }
}

int main()
{
    while (itWork) {
        arrayGen();
    }
}