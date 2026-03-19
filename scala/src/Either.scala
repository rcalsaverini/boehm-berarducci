//> using scala 3.3.1

package boehmberarducci

trait Either[+A, +B]:
  def fold[R](left: A => R)(right: B => R): R

  def map[C](f: B => C): Either[A, C] =
    fold[Either[A, C]](x => Left(x))(x => Right(f(x)))

  def flatMap[AA >: A, C](f: B => Either[AA, C]): Either[AA, C] =
    fold[Either[AA, C]](x => Left(x))(f)

case class Left[A](value: A) extends Either[A, Nothing]:
  def fold[R](left: A => R)(right: Nothing => R): R = left(value)

case class Right[B](value: B) extends Either[Nothing, B]:
  def fold[R](left: Nothing => R)(right: B => R): R = right(value)
