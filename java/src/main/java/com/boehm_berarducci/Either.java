package com.bb_encoding;
import java.util.function.*;

class Either<a, b> {

    private a left_value;

    private Either(a left_value){
        this.left_value = left_value;
    }

    public <r> r either(Function<a, r> case_left, Function<b, r> case_right) {
        return case_left.apply(left_value);
    }

    public static <a, b> Either<a, b> right(b right_value) {
        return new Either<a, b>() {
            public <r> r either(Function<a, r> case_left, Function<b, r> case_right) {
                return case_right.apply(right_value);
            }
        };        
    }

    public static <a, b> Either<a, b> left(a left_value) {
        return new Either<a, b>(left_value);
    }

    public static <a, b> Either<a, b> pure(b right_value) {
        return right(right_value);
    }

    public <c> Either<a, c> map(Function<b, c> function) {
        return bind(x -> pure(function.apply(x)));
    }

    public <c> Either<a, c> bind(Function<b, Either<a, c>> function) {
        return either(left, x -> function.apply(x));   
    }

    public <c> Either<a, c> over(Either<a, Function<b, c>> over_function) {
        return over_function.bind(f -> map(f));   
    }

    public String toString() {
        return either(x -> "Left " + x.toString(), x -> "Right " + x.toString());
    }

}