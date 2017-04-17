package main
import "os"
import "strconv"

func main() {
	pid := os.Getpid()
	f, _ := os.OpenFile("test" + strconv.Itoa(pid), os.O_WRONLY | os.O_CREATE | os.O_TRUNC, 0644)
	f.WriteString("The test is successful\n")
	f.Close()
}