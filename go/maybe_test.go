package main

import "testing"

func TestNothing(t *testing.T) {
	result := nothing.maybe("Nothing", func(x a) r { return "Just" })
	if result != "Nothing" {
		t.Errorf("expected Nothing, got %v", result)
	}
}

func TestJust(t *testing.T) {
	j := just(42)
	result := j.maybe(0, func(x a) r { return x })
	if result != 42 {
		t.Errorf("expected 42, got %v", result)
	}
}

func TestJustString(t *testing.T) {
	j := just("hello")
	result := j.maybe("nothing", func(x a) r { return x })
	if result != "hello" {
		t.Errorf("expected hello, got %v", result)
	}
}
