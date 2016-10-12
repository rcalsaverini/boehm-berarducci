module DataSpec.BoehmBerarducciSpec.EitherSpec (main, spec) where

import Data.BoehmBerarducci.Either
import Test.Hspec

main :: IO ()
main = hspec spec

spec :: Spec
spec = do
  describe "either" $ do
    it "fails" $ do
      1 `shouldBe` 0
