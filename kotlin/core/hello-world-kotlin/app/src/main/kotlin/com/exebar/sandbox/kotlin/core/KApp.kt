package com.exebar.sandbox.kotlin.core

class KApp (
    var greeting: String?
)

fun main() {
    println(
        KApp("Hello Kotlin World!").greeting
    )
}