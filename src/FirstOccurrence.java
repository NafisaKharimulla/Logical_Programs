public class FirstOccurrence {
    public static void main(String[] args) {
        String str = "Programming";
        char target = 'g';

        int index = str.indexOf(target);
        System.out.println("First occurrence of " + target + " is at index " + index);
    }
}