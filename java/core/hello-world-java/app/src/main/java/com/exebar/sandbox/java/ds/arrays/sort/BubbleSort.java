package com.exebar.sandbox.java.ds.arrays.sort;

public class BubbleSort implements ArraySort {
    public int[] sort(int... arr) {
        return sort(ArraySortDir.ASC, arr);
    }

    @Override
    public int[] sort(ArraySortDir dir, int... arr) {
        if (arr == null) return arr;
        for (int i = 0; i < arr.length - 1; i++)
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[i]) {
                    int swap = arr[i];
                    arr[i] = arr[j];
                    arr[j] = swap;
                }
            }
        return arr;
    }
}
