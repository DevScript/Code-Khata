package LeetcodeFirstMonth;

import java.util.HashMap;

public class ransomNote_383 {
    /*
    Runtime: 35 ms, faster than 20.68% of Java online submissions for Ransom Note.
Memory Usage: 51.7 MB, less than 32.36% of Java online submissions for Ransom Note.
     */
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> map = new HashMap<>();
        for(int i = 0; i < magazine.length(); i++){
            char Character = magazine.charAt(i);
            if(map.containsKey(Character)){
                map.put(Character, map.get(Character) + 1);
            }
            else {
                map.put(Character, 1);
            }
        }
        for(int j = 0; j < ransomNote.length(); j++){
            char charToCheck = ransomNote.charAt(j);
            if(map.containsKey(charToCheck)){
                if(map.get(charToCheck) > 0){
                    map.put(charToCheck, map.get(charToCheck) - 1);
                }
                else {
                    return false;
                }
            }
            else {
                return false;
            }
        }
        return true;
    }

    //Another solutin from Leetcode
    public class Solution {
        public boolean canConstruct(String ransomNote, String magazine) {
            int[] arr = new int[26];
            for (int i = 0; i < magazine.length(); i++) {
                arr[magazine.charAt(i) - 'a']++;
            }
            for (int i = 0; i < ransomNote.length(); i++) {
                if(--arr[ransomNote.charAt(i)-'a'] < 0) {
                    return false;
                }
            }
            return true;
        }
    }

    public static void main(String[] args) {

    }
}