project: cj
goal 1: create **fast** console template editor for java programmers on linux users
goal 2: integrate with gdb

[alex@zion lib]$ time cp /home/alex/.sdkman/candidates/java/17.0.7-amzn/lib/src.zip /tmp/
real	0m0.049s
user	0m0.002s
sys	0m0.047s
[alex@zion lib]$ time unzip -d /tmp/src /tmp/src.zip
real	0m7.122s
user	0m4.873s
sys	0m2.097s
[alex@zion lib]$ time unzip -l /tmp/src.zip
...
    14995  04-13-2023 18:19   jdk.zipfs/jdk/nio/zipfs/ZipUtils.java
    12088  04-13-2023 18:19   jdk.zipfs/module-info.java
---------                     -------
201267337                     15076 files
real	0m1.122s
user	0m0.337s
sys	0m0.420s

implementation: c, vim style editor that has command and edit mode
example commands:
c Hello == c hello: create class Hello
          pc Hello: create public class Hello
	      psvm: create public static void main()
	        fd: jump to function definition
               sop: add System.out.println()
         sop hello: add System.out.println(hello) // if hello variable is defined
         sop hello: add System.out.println("hello") // if hello variable is not defined

public class Hello {
  public static void main(String[] args) {
    System.out.println();
  }
}



