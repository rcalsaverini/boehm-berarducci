//> using scala 3.3.1
//> using dep org.scalatest::scalatest:3.2.17

package boehmberarducci

import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

class EitherSpec extends AnyFlatSpec with Matchers:

  "Left" should "fold to the left branch" in {
    Left("err").fold(e => s"left: $e")(_ => "right") shouldBe "left: err"
  }

  it should "be unchanged by map" in {
    Left("err").map((x: Int) => x + 1) shouldBe Left("err")
  }

  it should "be unchanged by flatMap" in {
    Left("err").flatMap((x: Int) => Right(x + 1)) shouldBe Left("err")
  }

  "Right" should "fold to the right branch" in {
    Right(42).fold(_ => "left")(x => s"right: $x") shouldBe "right: 42"
  }

  it should "apply map to its value" in {
    Right(1).map(_ + 1) shouldBe Right(2)
  }

  it should "flatMap correctly" in {
    Right(2).flatMap(x => Right(x * 3)) shouldBe Right(6)
  }

  it should "flatMap to Left when f returns Left" in {
    Right(1).flatMap(_ => Left("oops")) shouldBe Left("oops")
  }
