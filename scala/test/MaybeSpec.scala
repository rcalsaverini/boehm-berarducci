//> using scala 3.3.1
//> using dep org.scalatest::scalatest:3.2.17

package boehmberarducci

import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

class MaybeSpec extends AnyFlatSpec with Matchers:

  "Nothing" should "fold to the nothing branch" in {
    Nothing.fold("nothing")(_ => "just") shouldBe "nothing"
  }

  it should "be unchanged by map" in {
    Nothing.map((x: Int) => x + 1) shouldBe Nothing
  }

  it should "be unchanged by flatMap" in {
    Nothing.flatMap((x: Int) => Just(x + 1)) shouldBe Nothing
  }

  it should "return default from getOrElse" in {
    Nothing.getOrElse(42) shouldBe 42
  }

  "Just" should "fold to the just branch" in {
    Just(1).fold("nothing")(x => s"just $x") shouldBe "just 1"
  }

  it should "apply map to its value" in {
    Just(1).map(_ + 1) shouldBe Just(2)
  }

  it should "flatMap correctly" in {
    Just(2).flatMap(x => Just(x * 3)) shouldBe Just(6)
  }

  it should "flatMap to Nothing when f returns Nothing" in {
    Just(1).flatMap(_ => Nothing) shouldBe Nothing
  }

  it should "return its value from getOrElse" in {
    Just(99).getOrElse(0) shouldBe 99
  }
