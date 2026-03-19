//> using scala 3.3.1

package boehmberarducci

trait Maybe[+A]:
  def fold[R](nothing: => R)(just: A => R): R

  def map[B](f: A => B): Maybe[B] =
    fold[Maybe[B]](Nothing)(x => Just(f(x)))

  def flatMap[B](f: A => Maybe[B]): Maybe[B] =
    fold[Maybe[B]](Nothing)(f)

  def getOrElse[B >: A](default: => B): B =
    fold[B](default)(identity)

case object Nothing extends Maybe[Nothing]:
  def fold[R](nothing: => R)(just: Nothing => R): R = nothing

case class Just[A](value: A) extends Maybe[A]:
  def fold[R](nothing: => R)(just: A => R): R = just(value)
