package main

import (
	"fmt"
	"log"
)

func main() {
    config, err := ParseConfig()
    if err != nil {
        log.Fatalf("failed to parse microm configuration: %v", err)
    }
    fmt.Printf("%+v\n", *config)
    
    // BuildProject
    
    // Pass project into user input
    StartUserInput()
}