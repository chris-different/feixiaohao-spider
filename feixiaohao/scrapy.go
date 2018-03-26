package main


import "os/exec"
import "fmt"
import "io/ioutil"
func check(e error){
	if e != nil{
		panic(e)
	}
}

func main() {

	cmd := exec.Command("python3","/root/feixiaohao-spider/feixiaohao/start.py")
	cmdOut, err := cmd.StdoutPipe()
	check(err)
	cmd.Run()
	fmt.Println("爬虫爬取完成")
	cmdBytes, _ := ioutil.ReadAll(cmdOut)
	fmt.Println(string(cmdBytes))

}
