{-# LANGUAGE RankNTypes #-}

module Data.BoehmBerarducci.Maybe where


import           Prelude hiding (Just, Maybe, Nothing, maybe)

data Maybe a = Maybe {maybe :: forall r . r -> (a -> r) -> r}

nothing = Maybe const
just x  = Maybe (const ($ x))

instance (Show a) => (Show (Maybe a)) where
  show xs = maybe xs "Nothing" (\x -> "Just " ++ show x)

instance Functor Maybe where
  fmap f xs = maybe xs nothing (just . f)

instance Applicative Maybe where
  pure = just
  fs <*> xs = maybe fs nothing (`fmap` xs)

instance Monad Maybe where
  xs >>= f = maybe xs nothing f
