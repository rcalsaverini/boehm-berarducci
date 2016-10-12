package com.maybe;
import java.util.function.*;

class Main {

    static Maybe<Integer> nothing = Maybe.nothing();
    static Maybe<Integer> val = Maybe.just(1);
    static Maybe<Function<Integer, Integer>> fun = Maybe.just(x -> x + 1);

    public static void main(String[] args){
        System.out.println("I'm a Simple Program");
        System.out.println(nothing);
        System.out.println(
            val.map(x -> x + 81)
               .map(x -> x.toString())
               .map(x -> x.length())
               .over(fun)
        );
    }
}
