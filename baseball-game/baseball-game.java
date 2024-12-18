import java.util.Stack;
class Solution {
    public int calPoints(String[] operations) {
        Stack<Integer> stk = new Stack<>();
        for (int i = 0; i < operations.length; i++){
            String str = operations[i];
            char chr = str.charAt(0);
            if (Character.isDigit(chr) || chr == '-'){
                stk.push(Integer.parseInt(str));
            }
            else if (!stk.isEmpty()){
                if (chr == 'C'){
                    stk.pop();
                }
                else if (chr == 'D'){
                    int a = stk.peek();
                    stk.push(2 * a);
                }
                else if (chr == '+' && stk.size() > 1){
                    int a = stk.pop();
                    int b = stk.peek();
                    stk.push(a);
                    stk.push(a+b);
                }
            }
        }
        int sum = 0;
        while(!stk.isEmpty()){
            sum += stk.pop();
        }
        return sum;
    }
}
