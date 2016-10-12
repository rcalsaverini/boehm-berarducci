package com.bb_encoding;
import java.util.function.*;

class Main {

    static Maybe<Integer> nothing = Maybe.nothing();
    static Maybe<Integer> val = Maybe.just(1);
    static Maybe<Function<Integer, Integer>> fun = Maybe.just(x -> x + 1);

    static Function<Integer, Maybe<Double>> seven_div = (x -> 
        x == 0 ? Maybe.nothing() : Maybe.just(7.0 / x)
    );

    public static void main(String[] args){
        System.out.println("I'm a Simple Program");
        System.out.println(nothing);
        System.out.println(
            val.map(x -> x + 81)
               .map(x -> x.toString())
               .map(x -> x.length())
               .over(fun)
               .bind(seven_div)
        );
    }
}
