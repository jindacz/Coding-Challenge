public class Roman{
    public static int romanToInt(String s){
        Map<Character, Integer> romanMap = new HashMap<>();
        romanMap.put('I', 1);
        romanMap.put('V', 5);
        romanMap.put('X', 10);
        romanMap.put('L', 50);
        romanMap.put('C', 100);
        romanMap.put('D', 500);
        romanMap.put('M', 1000);

        char lastChar = s.charAt(s.length() - 1);
        int result = romanMap.get(lastChar);

        for (int i = s.length() - 2; i >= 0; i--){
            // if char at the right is smaller than current char -> add the value to result
            char currentChar = s.charAt(i);
            char nextChar = s.charAt(i + 1);
            if (romanMap.get(currentChar) >= romanMap.get(nextChar)){
                result += romanMap.get(currentChar);
            } else {
                result -= romanMap.get(currentChar);
            }
        }

        return result;

    }
}

public static main(String[] args){
    int result = romanToInt("III")
    assertEquals(3, result)
}