{-# LANGUAGE RankNTypes #-}

module Data.BoehmBerarducci.Either where

import Prelude hiding (Either, Left, Right, either)

newtype Either a b = Either {either :: forall r . (a -> r) -> (b -> r) -> r}

left :: a -> Either a b
left x = Either (\left' right' -> left' x)

right :: b -> Either a b
right x = Either (\left' right' -> right' x)

instance Functor (Either a) where
    fmap f xs = either xs left (right . f)

instance Applicative (Either a) where
  pure = right
  fs <*> xs = either fs left (\f -> fmap f xs)

instance Monad (Either a) where
    xs >>= f = either xs left (\x -> f x)

instance (Show a, Show b) => Show (Either a b) where
    show xs = either xs (\u -> "Left " ++ show u) (\u -> "Right " ++ show u)

instance (Eq a, Eq b) => Eq (Either a b) where
    xs == ys = either xs isLeftEqual isRightEqual where
        isLeftEqual x = either ys (\y -> x == y) (const False)
        isRightEqual x = either ys (const False) (\y -> x == y)