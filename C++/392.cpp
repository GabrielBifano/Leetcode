// Is Subsequence
// Easy

#include <string>

using namespace std;

bool isSubsequence(string s, string t) {
        
    int subseq_char = 0;
    int subseq_size = s.length();
    if (subseq_size == 0) return true;
    for(auto &l : t) {
        if ( l == s[subseq_char] ){
            subseq_char ++;
            if ( subseq_char == subseq_size ) {
                return true;
            }
        }
    }
    return false;
}