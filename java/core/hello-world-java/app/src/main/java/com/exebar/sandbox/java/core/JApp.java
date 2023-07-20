package com.exebar.sandbox.java.core;

public class JApp {

    private final String greeting;

    JApp(String greeting) {
        this.greeting = greeting;
    }

    public String getGreeting() {
        return this.greeting;
    }

    public static void main(String[] args) {
        System.out.println(
            new JApp("Hello Java World!").getGreeting()
        );
    }
}
