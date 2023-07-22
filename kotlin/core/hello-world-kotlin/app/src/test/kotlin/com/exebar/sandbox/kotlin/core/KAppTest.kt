/*
 * This Kotlin source file was generated by the Gradle 'init' task.
 */
package com.exebar.sandbox.kotlin.core

import org.junit.jupiter.api.DisplayName
import java.util.UUID
import kotlin.test.Test
import kotlin.test.assertEquals
import kotlin.test.assertNull
import kotlin.test.assertTrue

class KAppTest {
    @Test
    @DisplayName("App has a greeting")
    fun greeting() {
        val testGreeting = "Hello Kotlin World";
        val kApp = KApp(testGreeting)
        assertEquals(testGreeting, kApp.greeting)
    }

    @Test
    @DisplayName("App doesn't have to have a greeting")
    fun no_greeting() {
        val kApp = KApp(null)
        assertNull(kApp.greeting)
    }

    @Test
    @DisplayName("String template")
    fun string_template() {
        val x = 1.0
        assertEquals("x = 1.0", "x = $x")
    }

    @Test
    @DisplayName("String template expressions")
    fun string_template_expressions() {
        assertEquals("1+1=2", "1+1=${1+1}")
    }

    @Test
    @DisplayName("if expression")
    fun if_expression() {
        fun max(a: Int, b: Int) = if (a > b) a else b
        assertEquals(5, max(3, 5));
    }

    @Test
    @DisplayName("for-loop")
    fun for_loop() {
        for (fruit in listOf("apples", "bananas", "blueberries")) {
            println(fruit)
        }
    }

    @Test
    @DisplayName("indexed for-loop")
    fun for_loop_indexed() {
        val fruit = listOf("apples", "bananas", "blueberries")
        for (fruitIdx in fruit.indices) {
            println("fruit[${fruitIdx}] = ${fruit[fruitIdx]}")
        }
    }

    @Test
    @DisplayName("for-loop traversing range")
    fun range_for_loop() {
        for (i in 1..5) {
            println(i)
        }
    }

    @Test
    @DisplayName("for-loop traversing range with step")
    fun range_for_loop_with_step() {
        for (i in 1..5 step 2) {
            println(i)
        }
    }

    @Test
    @DisplayName("for-loop traversing range backwards")
    fun backwards_range_for_loop() {
        for (i in 5 downTo 1) {
            println(i)
        }
    }

    @Test
    @DisplayName("for-loop traversing range backwards with step")
    fun backwards_range_step_for_loop() {
        for (i in 5 downTo 1 step 2) {
            println(i)
        }
    }

    @Test
    @DisplayName("for-loop")
    fun while_loop() {
        var i = 0
        val fruitList = listOf("apples", "bananas", "blueberries")
        while (i < fruitList.size) {
            println("fruit[$i] = ${fruitList[i]}")
            i++
        }
    }
}
