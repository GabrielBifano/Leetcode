// Move Zeroes
// Easy

#include <vector>

using namespace std;

void moveZeroes(vector<int>& nums) {
    
    int insert_here = 0;
    int z_counter   = 0;

    for ( int i = 0; i < nums.size(); i++ ) {
        if ( nums[i] == 0 ) {
            z_counter += 1;
            continue;
        }
        nums[insert_here] = nums[i];
        insert_here += 1;
    }

    for ( int i = insert_here; i < nums.size(); i++ )
        nums[i] = 0;
}