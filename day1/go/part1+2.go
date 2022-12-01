package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func main() {
	data, err := os.Open("../input.txt")

	if err != nil {
		log.Fatal(err)
	}

	defer func(data *os.File) {
		err := data.Close()
		if err != nil {
			log.Fatal(err)
		}
	}(data)

	scanner := bufio.NewScanner(data)

	calories := 0
	elfCount := 0
	elves := map[int]int{}
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			elves[elfCount] = calories
			calories = 0
			elfCount = elfCount + 1
		} else {
			intLine, _ := strconv.Atoi(line)
			calories = calories + intLine
		}
	}
	keys := make([]int, 0, len(elves))
	for k := range elves {
		keys = append(keys, k)
	}
	sort.Slice(keys, func(i, j int) bool {
		return elves[keys[i]] > elves[keys[j]]
	})

	fmt.Println("Top calories:", elves[keys[0]])
	fmt.Println("Top 3 calories:", elves[keys[0]]+elves[keys[1]]+elves[keys[2]])

}
