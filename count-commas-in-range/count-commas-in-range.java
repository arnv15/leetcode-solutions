class Solution {
    public int countCommas(int n) {
        if (String.valueOf(n).length() <= 3){
            return 0;
        }
        else {
            return n - 999;
        }
    }
}
