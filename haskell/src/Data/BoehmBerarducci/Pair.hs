{-# LANGUAGE RankNTypes #-}

module Data.BoehmBerarducci.Pair where

newtype Pair a b = Pair {foldPair :: forall r . (a -> b -> r) -> r}

pair :: a -> b -> Pair a b
pair x y = Pair (\ f -> f x y)

fst :: Pair a b -> a
fst ab = foldPair ab (\f s -> f)

snd :: Pair a b -> b
snd ab = foldPair ab (\f s -> s)