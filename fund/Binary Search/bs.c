#include <stdio.h>

int binary_search(int target, int arr[], int len){
    int start = 0;
    int end = len - 1;
    int mid;

    while(start < end){
        mid = (start + end) / 2;

        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            start = mid + 1;
        } else if (arr[mid] > target) {
            end = mid;
        }
    }

    return (arr[start] == target) ? mid : -1;
}

int main(){
    int arr[] = {1,6,9,12,13,20,25,33,44,56,73};
    size_t len = sizeof(arr) / sizeof(arr[0]);

    int index = binary_search(75, arr, len);

    printf("the index of the target element is %d\n", index);

    return 0;
}