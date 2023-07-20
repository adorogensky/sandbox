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
}
