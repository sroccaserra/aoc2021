module XXSpec
    where

import Test.Hspec

main = hspec spec

spec = describe "A failing test"$ do
    it "fails" $ do
        1 `shouldBe` 2
