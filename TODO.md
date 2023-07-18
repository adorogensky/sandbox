# TODO
* fix kotlin app run problem in java-kotlin project in intellij (hello-world-kotlin module)
* why intellij's "build and run using gradle" and "run tests using gradle" dont work?
* add ng-rx
* android modules and priorities

# PRIORITIES
create stats for 7 work days
* use numbers 0, 1, 2 and 3 for languages/libararies i used to identify how much "read up" time i needed to solve tech challenges
* 0 - means no time or almost no time
* 1 - means some time
* 2 - means approx 2x of what 1 means
* 3 - means approx 3x of what 1 means
* use decimals from 1 to 2.5 to identify how much i think i will benefit from learning this language/library in the short and long run average
* ``value score = read up score * benefit``, e.g
  * angular = 2 * 1.4 = 2.8
  * javascript = 2 * 1.5 = 3.0
  * css = 3 * 1.8 = 5.4
  * java = 0 * 1.0 = 0.0

* angular
  * javascript: work
  * typescript: work
  * ngrx: work
  * karma: work
  * jasmine: work
* html-view
  * html: work
  * css: work
  * bootstrap
* android
  * why: android app development naturally appealing
  * what: screen layouts, presentation
* kotlin (vs java)
  * why: work and android dev
  * what: basic language structure, coroutines, java-kotlin gap
* java
  * why: work, future work projects, interviews
  * what: classic algorithms and computational problems (leetcode)

# NEXT PRIORITIES
* python
  * why:
    * lightweight
    * versataile
      * server
      * linux desktop
      * dev ops and scripting
      * data science
      * well adopted across varying software platforms: Linux, Windows, MacOS
    * concise
    * popular and improving
  * what: basic language structure

# UNPROCESSED
* refactor
  * data class Greeting(text="..")
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
  
      
nvm ls-remote
nvm => node => npm => ng ecosystem
    
do i need to update npm?
What | Version
-- | --
Angular CLI | 16.1.4
Node | 18.16.1
Package Manager | npm 9.5.1
OS | linux x64

Package                     | Version
----------------------------|-------------------------
@angular-devkit/architect   | 0.1601.4 (cli-only)
@angular-devkit/core        | 16.1.4 (cli-only)
@angular-devkit/schematics  | 16.1.4 (cli-only)
@schematics/angular         | 16.1.4 (cli-only)


android: disconnect phone<p>
adb kill-server<p>
sudo adb start-server<p>
turn on and off usb debugging on phone


