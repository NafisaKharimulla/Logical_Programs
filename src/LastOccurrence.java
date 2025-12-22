public class LastOccurrence {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 2, 5, 2};
        int target = 2;
        int index = -1;

        for (int i = arr.length - 1; i >= 0; i--) {
            if (arr[i] == target) {
                index = i;
                break;
            }
        }

        System.out.println("Last occurrence index = " + index);
    }
}
