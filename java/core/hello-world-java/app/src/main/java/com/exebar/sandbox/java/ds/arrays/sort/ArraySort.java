package com.exebar.sandbox.java.ds.arrays.sort;

public interface ArraySort {
    /**
     * Sorts input array of integers in ascending or descending order.
     * Returns a reference to the input array
     */
    int[] sort(int... arr);

    int[] sort(ArraySortDir dir, int... arr);
}
