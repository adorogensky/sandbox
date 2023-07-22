# Kotlin
[Comparison to Java](https://kotlinlang.org/docs/comparison-to-java.html)

* main() and println()
* classes
  * properties: declaration, body
  * final by default
  * open are those that can be inherited
* types
  * no primitives unlike java
  * inferred
  * nullable
* string templates and expressions
* ``if`` expression
* ``for`` loop
  * over list
  * over list indicies
  * over range 
  * over range with step
  * over range backwards
  * over range backwards with step
* ``while`` loop
* ``when`` expression
* why not allow empty class declaration if all class properties declared nullable?
* refactor
  * null safety typed features
  * 3 links at the end: strings, collections, nullability
  * kotlin generics
  * invariant kotlin arrays
  * kotlin doesnt have wildcard types it has use-site variance and type projections
  * kotlin doesnt have checked exceptions, all exceptions are unchecked
  * kotlin doesnt have any primitive types
  * kotlin doesnt have static member, instead use these
    * companion objects
    * top-level functions
    * extension functions
    * @JvmStatic
  * a ? b : c === if(a) b else c
  * unique kotlin features
    * lambda expressions + inline functions
    * extension functions
    * null safety
    * smart casts
    * string templates
    * properties
    * primary constructors
    * 1st class delegation
    * type inference for variable and property types
    * singletons
    * declaration-site & type projections
    * range expressions
    * operator overloading
    * companion objects
    * data classes
    * separate interfaces for read-only and mutable collections
    * coroutines
