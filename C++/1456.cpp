// Maximum Number of Vowels in a Substring of Given Length
// Medium

#include <map>
#include <string>

using namespace std;

int maxVowels(string s, int k) {
    
    int arr[s.length()];

    int i = 0;
    for ( auto &ch : s ) {
        switch (ch)
        {
            case 'a':
                arr[i] = 1;
                break;
            case 'e':
                arr[i] = 1;
                break;
            case 'i':
                arr[i] = 1;
                break;
            case 'o':
                arr[i] = 1;
                break;
            case 'u':
                arr[i] = 1;
                break;
            default:
                arr[i] = 0;
                break;
        } i += 1;
    }
    
    int max_vowels = 0, sum_vowels = 0;
    for ( int i = 0; i < k; i++ )
        max_vowels += arr[i];
    sum_vowels = max_vowels;

    int j;
    for ( int i = 1; i < s.length()-k+1; i++ ) {
        j = i + k - 1;
        sum_vowels = sum_vowels - arr[i - 1] + arr[j];
        if ( max_vowels < sum_vowels )
            max_vowels = sum_vowels;
    }

    return max_vowels;
}