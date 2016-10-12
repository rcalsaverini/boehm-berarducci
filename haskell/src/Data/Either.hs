{-# LANGUAGE RankNTypes #-}

module Data.Either where

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