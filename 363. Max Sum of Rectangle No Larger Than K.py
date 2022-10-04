class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k1) {
        int m = matrix.length, n = matrix[0].length;
        int res = Integer.MIN_VALUE;
        for (int i=0; i < m; i++) {
            int[] list1 = new int[n];
            for (int j=i; j < m; j++) {
                for (int r=0; r < n; r++) {
                    list1[r] += matrix[j][r];
                }
                TreeSet<Integer> treeset = new TreeSet<>();
                // new - pre <= k -> pre >= new - k
                treeset.add(0);
                int total = 0;
                for (int k = 0; k < n; k++) {
                    total += list1[k];
                    Integer x = treeset.ceiling(total - k1);
                    if (x != null) {
                        res = Math.max(res, total - x);
                    }
                    treeset.add(total);
                }
            }
        }
        return res;
    }
}