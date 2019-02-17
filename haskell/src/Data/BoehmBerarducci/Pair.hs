{-# LANGUAGE RankNTypes #-}

module Data.BoehmBerarducci.Pair where

type Pair a b = forall r . (a -> b -> r) -> r

pair :: a -> b -> Pair a b
pair x y = \ f -> f x y

