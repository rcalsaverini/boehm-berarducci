{-# LANGUAGE FlexibleContexts #-}
{-# LANGUAGE ScopedTypeVariables #-}

module DataSpec.BoehmBerarducciSpec.EitherSpec (main, spec) where

import Data.BoehmBerarducci.Either
import Prelude hiding (Either, Left, Right, either)

import Test.Hspec
import Test.QuickCheck
import Control.Exception

main :: IO ()
main = hspec spec
 
isLeft x = either x (const True) (const False)
isRight x = either x (const False) (const True)

spec :: Spec
spec = do
    describe "left" $ do

        it "when bound, always returns a left" $ do
            property $ \ (x :: Int) (y :: Int) -> 
                left x == ((left x) >>= (\u -> right y))

        it "when fmapped, it is unchanged" $ do
            property $ \ (x :: Int) (y :: Int) -> 
                (fmap (const y) (left x)) `shouldBe` left x

    describe "right" $ do

        it "it is overwritten when bound to a function that returns another right" $ do
            property $ \ (x :: Int) (y :: Int) -> 
                right y == (((right x) :: (Either String Int)) >>= (\u -> right y))

        it "when fmapped, it's contents are mapped" $ do
            property $ \ (x :: Int) (y :: Int) -> 
                (fmap (const y) ((right x) :: (Either String Int))) `shouldBe` (right y)


    describe "either" $ do

        it "returns the left argument when applied on a left instance" $ do
            property $ \ (x :: Int) -> 
                either (left x) (const "Left") (const "Right") `shouldBe` "Left"

        it "returns the right argument when applied on a right instance" $ do
            property $ \ (x :: Int) -> 
                either (right x) (const "Left") (const "Right") `shouldBe` "Right"