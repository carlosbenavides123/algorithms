import java.util.ArrayList;
import java.util.*;

class Main{

    public static void main(String[] args) {
        List<String> myList = new ArrayList<>();
        myList.add("nm");
        myList.add("flew");
        myList.add("eagle");
        myList.add("dog");
        myList.add("opxzvasre");
        System.out.print(longestPhrase(myList));
    }
public static int longestPhrase(List<String> words) {
    if (words == null || words.size() == 0) {
        return 0;
    }

    int[] max = new int[1];
    findLongestPhrase(words, "", 0, max);
    return max[0];
}

private static void findLongestPhrase(List<String> words, String current, int index, int[] max) {
    boolean hasUniqueCharacters = hasUniqueCharacters(current);
    System.out.println(current);
    if (hasUniqueCharacters) {

        System.out.println(current);
        System.out.println("IN HERE");
        max[0] = Math.max(max[0], current.length());
    }
    if (index == words.size() || !hasUniqueCharacters) {
        return;
    }

    for (int i = index; i < words.size(); i++) {
        findLongestPhrase(words, current + words.get(i), i + 1, max);
    }
}

private static boolean hasUniqueCharacters(String phrase) {
    Set<Character> used = new HashSet<>();
    for (char c: phrase.toCharArray()) {
        if (used.contains(c)) {
            return false;
        }
        used.add(c);
    }

    return true;
}
}
