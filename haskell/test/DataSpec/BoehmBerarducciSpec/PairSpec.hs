{-# LANGUAGE FlexibleContexts #-}
{-# LANGUAGE ScopedTypeVariables #-}

module DataSpec.BoehmBerarducciSpec.PairSpec (main, spec) where

import Data.BoehmBerarducci.Pair
import Prelude hiding (fst, snd)

import Test.Hspec
import Test.QuickCheck
import Control.Exception

main :: IO ()
main = hspec spec

spec :: Spec
spec = do
    describe "fst" $ do

        it "it returns the first element of a newly created pair" $ do
            property $ \ (x :: Int) (y :: Int) -> 
                (fst $ pair x y) == x

    describe "snd" $ do

        it "it returns the first element of a newly created pair" $ do
            property $ \ (x :: Int) (y :: Int) -> 
                (snd $ pair x y) == y
