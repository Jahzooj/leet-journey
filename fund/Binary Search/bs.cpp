#include <iostream>
#include <vector>

using namespace std;

int binary_search(int target, vector<int> vec){
    int start = 0;
    int end = vec.size() - 1;
    int mid;

    while (start <= end) {
        mid = (start + end) / 2;
        if (start == end) {
            return (vec.at(start) == target) ? start : -1;
        }

        if (vec.at(mid) == target) {
            return mid;
        } else if (target < vec.at(mid)) {
            end = mid;
        } else if (target > vec.at(mid)) {
            start = mid + 1;
        }
    }
}


int main(){
    vector<int> vec = {8,12,15,18,22,25,34,36,40,55};

    int index = binary_search(0, vec);
    printf("the index of the target element is %d\n", index);

    return 0;
}