package com.maybe;
import java.util.function.*;

class Maybe<a> {

    private Maybe(){};
    
    public static <a> Maybe<a> just(a x) {
        return new Maybe<a>() {
            public <r> r maybe(r case_nothing, Function<a, r> case_just) {
                return case_just.apply(x);
            }
        };
    }

    public static <a> Maybe<a> nothing() {
        return new Maybe<>();
    }



    public <r> r maybe(r case_nothing, Function<a, r> case_just) {
        return case_nothing;
    }

    public String toString() {
        return maybe("Nothing", x -> "Just " + x.toString());
    }

    public <b> Maybe<b> map(Function<a, b> function) {
        return bind(x -> just(function.apply(x)));
    }

    public <b> Maybe<b> bind(Function<a, Maybe<b>> function) {
        return maybe(nothing(), x -> function.apply(x));   
    }

    public <b> Maybe<b> over(Maybe<Function<a, b>> maybe_function) {
        return maybe_function.bind(f -> map(f));   
    }
}
