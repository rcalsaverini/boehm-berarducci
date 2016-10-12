{-# LANGUAGE RankNTypes #-}

import Prelude hiding (Maybe, Just, Nothing, maybe)

{- 
data Maybe a = Nothing | Just a

maybe :: Maybe a -> r -> (a -> r) -> r
maybe Nothing x _ = x
maybe (Just x) _ f = f x
-}

data Maybe a = Maybe {maybe :: forall r . r -> (a -> r) -> r}

nothing = Maybe (\nothing' just' -> nothing')
just x  = Maybe (\nothing' just' -> just' x)

instance (Show a) => (Show (Maybe a)) where
  show xs = maybe xs "Nothing" (\x -> "Just " ++ show x)
  
instance Functor Maybe where
  fmap f xs = maybe xs nothing (\us -> just $ f us)
  
instance Applicative Maybe where
  pure = just
  fs <*> xs = maybe fs nothing (\f -> fmap f xs)

instance Monad Maybe where
  xs >>= f = maybe xs nothing f

safeHead [] = nothing
safeHead (x:xs) = just x

main = print $ just "omobó" >>= safeHead
