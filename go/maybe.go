package main

import (
	"fmt"
)


type a interface {}
type r interface {}

type Maybe struct {
    maybe   func(r, func(a) r) r
}

var nothing Maybe = Maybe{func(n r, j func(a) r) r {return n}}

func just(x a) Maybe {
    return Maybe{func(n r, j func(a) r) r {return j(x)}}
}

func (maybe Maybe) String() string {
    return maybe.maybe("Nothing", func(x a) r {return fmt.Sprintf("Just %v", x)}).(string)
}

func (maybe Maybe) Map(func(a) b) 

func main() {	
	var x = just(1)
	fmt.Println(x)
}
