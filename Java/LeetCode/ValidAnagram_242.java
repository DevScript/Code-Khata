package LeetcodeFirstMonth;

import java.util.HashMap;

public class ValidAnagram_242 {
    /*
     * Runtime: 23 ms, faster than 22.84% of Java online submissions for Valid
     * Anagram.
     * Memory Usage: 46.2 MB, less than 23.74% of Java online submissions for Valid
     * Anagram.
     */
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char Character = s.charAt(i);
            if (map.containsKey(Character)) {
                map.put(Character, map.get(Character) + 1);
            } else {
                map.put(Character, 1);
            }
        }
        for (int j = 0; j < t.length(); j++) {
            char charToCheck = t.charAt(j);
            if (map.containsKey(charToCheck)) {
                if (map.get(charToCheck) > 0) {
                    map.put(charToCheck, map.get(charToCheck) - 1);
                } else {
                    return false;
                }
            } else {
                return false;
            }
        }
        return true;
    }

    // From Leetcode
    public class Solution {
        public boolean isAnagram(String s, String t) {
            int[] alphabet = new int[26];
            for (int i = 0; i < s.length(); i++)
                alphabet[s.charAt(i) - 'a']++;
            for (int i = 0; i < t.length(); i++) {
                alphabet[t.charAt(i) - 'a']--;
                if (alphabet[t.charAt(i) - 'a'] < 0)
                    return false;
            }
            for (int i : alphabet)
                if (i != 0)
                    return false;
            return true;
        }
    }

    public static void main(String[] args) {

    }
}