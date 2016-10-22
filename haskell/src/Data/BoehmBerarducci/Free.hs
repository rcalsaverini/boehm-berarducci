{-# LANGUAGE RankNTypes #-}

module Data.BoehmBerarducci.Free where

import Control.Monad
-- data FreeBo f a = Pure a | Roll (f (Free f a))

data Free f a = Free {
    unfree :: forall r . (a -> r) -> (f r -> r) -> r
}

pureF :: a -> Free f a
pureF x = Free (\ pure' free' -> pure' x)

free :: (Functor f) => f (Free f a) -> Free f a
free fs = Free (\ pure' free' -> free' $ fmap (\f -> unfree f pure' free') fs )

instance Functor f => Functor (Free f) where
    fmap f fr = unfree fr (pureF . f) free

instance Functor f => Applicative (Free f) where
    pure = pureF
    fs <*> xs = unfree fs (<$> xs) free

instance Functor f => Monad (Free f) where
    xs >>= f = unfree xs f free

liftF :: (Functor f) => f r -> Free f r
liftF xs = free $ fmap pure xs

iter :: Functor f => (f a -> a) -> Free f a -> a
iter f xs = unfree xs id f

iterA :: (Applicative p, Functor f) => (f (p a) -> p a) -> Free f a -> p a
iterA f xs = unfree xs pure f

iterM :: (Monad m, Functor f) => (f (m a) -> m a) -> Free f a -> m a
iterM f xs = unfree xs pure f

hoistFree :: Functor g => (forall a. f a -> g a) -> Free f b -> Free g b
hoistFree f xs = unfree xs pure (free . f)

foldFree :: Monad m => (forall x . f x -> m x) -> Free f a -> m a
foldFree f xs = unfree xs pure (join . f)

retract :: Monad m => Free m a -> m a
retract xs = unfree xs pure join
