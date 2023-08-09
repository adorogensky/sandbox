package com.exebar.sandbox.java.ds.arrays.sort;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class ArraySortAscTests {

    private final ArraySort arraySort = new BubbleSort();
    private final int[] NULL_ARRAY = null;

    private static int[] arrayOf(int... arr) {
        return arr;
    }

    @Test
    public void sort_null_array() {
        assertNull(arraySort.sort(NULL_ARRAY));
    }

    @Test
    public void sort_empty_array() {
        assertArrayEquals(arrayOf(), arraySort.sort(arrayOf()));
    }

    @Test
    public void sort_1_element_array() {
        assertArrayEquals(arrayOf(1), arraySort.sort(1));
    }

    @Test
    public void sort_2_equal_elements_array() {
        assertArrayEquals(arrayOf(2, 2), arraySort.sort(2, 2));
    }
    @Test
    public void sort_2_elements_sorted_array() {
        assertArrayEquals(arrayOf(1, 2), arraySort.sort(1, 2));
    }

    @Test
    public void sort_2_elements_unsorted_array() {
        assertArrayEquals(arrayOf(1, 2), arraySort.sort(2, 1));
    }

    @Test
    public void sort_5_elements_unsorted_array() {
        assertArrayEquals(
            arrayOf(1, 2, 3, 4, 5),
            arraySort.sort(2, 5, 1, 3, 4)
        );
    }
}
