#include <iostream>
using namespace std;

void merge(int arr1[], int arr2[], int arrSize)
{
    int size = arrSize * 2, med1, med2;
    int i = 0, j = 0, k = 0, *mergeArray = new int[size];

    while (i < arrSize && j < arrSize)
    {
        if (arr1[i] < arr2[j])
        {
            mergeArray[k] = arr1[i];
            k++;
            i++;
        }
        else
        {
            mergeArray[k] = arr2[j];
            k++;
            j++;
        }
    }

    while (i < arrSize)
    {
        mergeArray[k] = arr1[i];
        k++;
        i++;
    }

    while (j < arrSize)
    {
        mergeArray[k] = arr2[j];
        k++;
        j++;
    }

    if (size % 2 != 0)
    {
        med1 = ((size + 1) / 2) - 1;
        cout << mergeArray[med1] << endl;
    }
    else
    {
        med1 = ((size + 1) / 2) - 1;
        med2 = ((size + 1) / 2);
        cout << mergeArray[med1] << ", " << mergeArray[med2] << endl;
    }
}

int main()
{
    int arr1[5] = {80, 85, 86, 87, 100};
    int arr2[5] = {2, 60, 69, 70, 86};
    int size = 5;
    merge(arr1, arr2, size);
    return 0;
}
